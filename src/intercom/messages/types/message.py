# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.unchecked_base_model import UncheckedBaseModel
from .message_message_type import MessageMessageType


class Message(UncheckedBaseModel):
    """
    Message are how you reach out to contacts in Intercom. They are created when an admin sends an outbound message to a contact.
    """

    type: str = pydantic.Field()
    """
    The type of the message
    """

    id: str = pydantic.Field()
    """
    The id representing the message.
    """

    created_at: int = pydantic.Field()
    """
    The time the conversation was created.
    """

    subject: str = pydantic.Field()
    """
    The subject of the message. Only present if message_type: email.
    """

    body: str = pydantic.Field()
    """
    The message body, which may contain HTML.
    """

    message_type: MessageMessageType = pydantic.Field()
    """
    The type of message that was sent. Can be email, inapp, facebook or twitter.
    """

    conversation_id: str = pydantic.Field()
    """
    The associated conversation_id
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
