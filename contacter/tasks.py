import logging
from datetime import timedelta

from celery import shared_task
from django.conf import settings
from django.db.models import F, Q, Max
from django.db.transaction import atomic
from django.utils import timezone

from .models import Conversation, PRIORITY_CHOICES
from .services import send_message as _send_message, check_responses

logger = logging.getLogger(__name__)


@shared_task
def update_messages():
    """
    Send messages for any conversations which haven't been responded to for a while.
    """
    # Stale conversations are any which haven't been responded to, haven't reached their max priority,
    # and haven't been updated for MESSAGE_INTERVAL minutes.
    stale_time_threshold = timezone.now() - timedelta(minutes=settings.MESSAGE_INTERVAL)
    stale_conversations = Conversation.objects.filter(
        Q(sent=None) | Q(sent__lt=stale_time_threshold),
        responded=None,
        status__lt=F('priority')
    )

    if not stale_conversations.exists():
        logger.info('No messages to send.')
        return

    # Check whether any services have received a response.
    if Conversation.objects.filter(sent=None).exists():
        logger.debug('One or more messages have not yet been sent. Skipping response check.')
        response_time = None
    else:
        last_message_sent = Conversation.objects.aggregate(Max('sent'))['sent__max']
        response_time = check_responses(since=last_message_sent)

    if response_time:
        # Update all un-responded conversations with response time.
        logger.info('Response received!')
        Conversation.objects.filter(responded=None).update(responded=response_time)
        return
    else:
        # Start sub-task for each stale conversation.
        for conversation_id in stale_conversations.values_list('id', flat=True):
            send_message.delay(conversation_id)


@shared_task
def send_message(conversation_id):
    with atomic():
        conversation = Conversation.objects.get(id=conversation_id)
        logger.info(f'Updating: {conversation}')

        # Get next status
        match_found = False
        for priority_choice in PRIORITY_CHOICES:
            if match_found:
                new_status = priority_choice
                break
            if priority_choice[0] == conversation.status:
                match_found = True
        else:
            raise Exception(f'Next status not found: {conversation.status}')

        logger.debug(f'New status: {new_status}')

        # Send message using appropriate service
        _send_message(new_status[1], conversation.message)

        # Update conversation status and sent timestamp
        conversation.status = new_status[0]
        conversation.sent = timezone.now()
        conversation.save()
