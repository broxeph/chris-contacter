from datetime import timedelta

from celery import shared_task
from django.conf import settings
from django.db.models import F, Q
from django.db.transaction import atomic
from django.utils import timezone

from .models import Conversation


@shared_task
def send_messages():
    """
    Send messages for any conversations which haven't been responded to for a while.
    """
    # Stale conversations are any which haven't been responded to, haven't reached their max priority,
    # and haven't been updated for [an hour].
    stale_time_threshold = timezone.now() - timedelta(minutes=settings.MESSAGE_INTERVAL)
    stale_conversation_ids = Conversation.objects.filter(
        Q(sent=None) | Q(sent__lt=stale_time_threshold),
        responded=None,
        status__lt=F('priority')
    ).values_list('id', flat=True)

    for conversation_id in stale_conversation_ids:
        send_message.delay(conversation_id)


@shared_task
def send_message(conversation_id):
    with atomic():
        conversation = Conversation.objects.get(id=conversation_id)
        print(f'Updating: {conversation}')


