import imaplib
import logging
from datetime import date
from email import message_from_bytes
from email.utils import parsedate_to_datetime

from django.conf import settings
from django.core.mail import EmailMessage
from django.utils.timezone import localtime
from pytz import utc
from twilio.rest import Client

from .models import EMAIL, TEXT

logger = logging.getLogger(__name__)


def check_responses(since):
    """
    Look for replies across all services.

    Args:
        since: Datetime after which to check messages.
    Returns:
        datetime response received, or None.

    """
    since_str = localtime(since).strftime("%-I:%M:%S %p")
    logger.info(f'Checking for responses since {since_str}...')
    for service in SERVICES.values():
        response_time = service.check(since)
        if response_time:
            return response_time
    else:
        return None


def send_message(message_type, message):
    """
    Send message using appropriate service.

    Args:
        message_type: Slug used to look up service class
        message: Message string

    """
    logger.info(f'Sending message using {message_type}...')

    # Look up message class and send message.
    SERVICES[message_type].send(message)

    logger.info('Message sent.')


class Email:
    @staticmethod
    def check(since):
        conn = imaplib.IMAP4_SSL(settings.EMAIL_HOST)
        conn.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        conn.select('INBOX')

        # Format today as string
        today_string = date.today().strftime("%d-%b-%Y")

        # Search inbox (IMAP doesn't allow searching by timestamp)
        result, data = conn.search(None, f'(SENTSINCE {today_string} FROM {settings.CHRIS_EMAIL})')

        if not data:
            logger.debug('No emails found today.')
            return None

        # Look for emails since since
        for email_id in data[0].split():
            msg_string = conn.fetch(email_id, '(RFC822)')[1][0][1]
            msg = message_from_bytes(msg_string)
            response_time_naive = parsedate_to_datetime(msg['Date'])
            response_time = utc.localize(response_time_naive)
            if response_time > since:
                return response_time
        else:
            logger.debug('No new emails found.')
            return None

    @staticmethod
    def send(message):
        email = EmailMessage(settings.EMAIL_SUBJECT, message, to=[settings.CHRIS_EMAIL])
        email.send()
        logger.debug(f'Email sent to {settings.CHRIS_EMAIL}.')


class Text:
    @staticmethod
    def check(since):
        logger.warning('Text checking not yet implemented.')  # TODO: Publish app on Heroku and register Twilio webhook?

    @staticmethod
    def send(message):
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=f"{message}\n{settings.TEXT_SIGNATURE}",
            from_=settings.TWILIO_PHONE,
            to=settings.CHRIS_PHONE)
        logger.debug(f'Text sent to {settings.CHRIS_PHONE}.')


SERVICES = {
    EMAIL: Email,
    TEXT: Text,
}
