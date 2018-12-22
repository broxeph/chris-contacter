import logging

from .models import EMAIL, TEXT

logger = logging.getLogger(__name__)


def check_responses(since):
    """
    Look for replies across all services.

    Args:
        since: Timestamp after which to check messages.
    Returns:
        datetime response received, or None.

    """
    logger.info(f'Checking for responses since {since}...')
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
        logger.warning('Email checking not yet implemented.')

    @staticmethod
    def send(message):
        raise NotImplementedError('Email sending not yet implemented. Message not sent.')


class Text:
    @staticmethod
    def check(since):
        logger.warning('Text checking not yet implemented.')  # TODO: Publish app on Heroku and register Twilio webhook?

    @staticmethod
    def send(message):
        raise NotImplementedError('Text sending not yet implemented. Message not sent.')


SERVICES = {
    EMAIL: Email,
    TEXT: Text,
}
