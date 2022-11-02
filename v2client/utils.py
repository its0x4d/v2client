import re
import uuid

from google.protobuf.message import Message

from api.v2ray.common.serial.typed_message_pb2 import TypedMessage


def to_typed_message(message: Message) -> TypedMessage:
    """
    Convert a protobuf message to a TypedMessage.
    V2Ray requires TypedMessage for some API calls.
    :param message: A protobuf message.
    :return: A TypedMessage.
    """
    return TypedMessage(type=message.DESCRIPTOR.full_name, value=message.SerializeToString())


def is_email_valid(email: str) -> bool:
    """
    Check if an email is valid.
    :param email: An email address.
    :return: True if the email is valid, False otherwise.
    """
    return re.match(r"[a-zA-Z\d_.+-]+@[a-zA-Z\d-]+\.[a-zA-Z\d-.]+$", email) is not None


def random_uuid() -> str:
    """
    Generate a random UUID.
    :return: A UUID.
    """
    return str(uuid.uuid4())

