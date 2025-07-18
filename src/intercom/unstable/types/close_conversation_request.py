# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.unchecked_base_model import UncheckedBaseModel


class CloseConversationRequest(UncheckedBaseModel):
    """
    Payload of the request to close a conversation
    """

    type: typing.Literal["admin"] = "admin"
    admin_id: str = pydantic.Field()
    """
    The id of the admin who is performing the action.
    """

    body: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optionally you can leave a message in the conversation to provide additional context to the user and other teammates.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
