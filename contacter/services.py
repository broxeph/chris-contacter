import logging

from .models import CHAT, EMAIL, TEXT, CALL

logger = logging.getLogger(__name__)


def send_message(message_type, message):
    """
    Look up message service and send message.
    """
    logger.info(f'Sending message using {message_type}...')
    SERVICES[message_type](message)


def send_chat(message):
    logger.info(f'Sending chat: {message}')


def send_email(message):
    raise NotImplementedError


def send_text(message):
    raise NotImplementedError


def send_call(message):
    raise NotImplementedError


SERVICES = {
    CHAT: send_chat,
    EMAIL: send_email,
    TEXT: send_text,
    CALL: send_call,
}
