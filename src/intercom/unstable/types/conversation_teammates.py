# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.unchecked_base_model import UncheckedBaseModel
from .reference import Reference


class ConversationTeammates(UncheckedBaseModel):
    """
    The list of teammates who participated in the conversation (wrote at least one conversation part).
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the object - `admin.list`.
    """

    teammates: typing.Optional[typing.List[Reference]] = pydantic.Field(default=None)
    """
    The list of teammates who participated in the conversation (wrote at least one conversation part).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
