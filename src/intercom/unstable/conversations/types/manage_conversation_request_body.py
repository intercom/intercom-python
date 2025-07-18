# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel, UnionMetadata
from ...types.assign_conversation_request_type import AssignConversationRequestType


class ManageConversationRequestBody_Close(UncheckedBaseModel):
    message_type: typing.Literal["close"] = "close"
    type: typing.Literal["admin"] = "admin"
    admin_id: str
    body: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ManageConversationRequestBody_Snoozed(UncheckedBaseModel):
    message_type: typing.Literal["snoozed"] = "snoozed"
    admin_id: str
    snoozed_until: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ManageConversationRequestBody_Open(UncheckedBaseModel):
    message_type: typing.Literal["open"] = "open"
    admin_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ManageConversationRequestBody_Assignment(UncheckedBaseModel):
    message_type: typing.Literal["assignment"] = "assignment"
    type: AssignConversationRequestType
    admin_id: str
    assignee_id: str
    body: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ManageConversationRequestBody = typing_extensions.Annotated[
    typing.Union[
        ManageConversationRequestBody_Close,
        ManageConversationRequestBody_Snoozed,
        ManageConversationRequestBody_Open,
        ManageConversationRequestBody_Assignment,
    ],
    UnionMetadata(discriminant="message_type"),
]
