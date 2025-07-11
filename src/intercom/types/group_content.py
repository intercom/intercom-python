# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class GroupContent(UncheckedBaseModel):
    """
    The Content of a Group.
    """

    type: typing.Literal["group_content"] = pydantic.Field(default="group_content")
    """
    The type of object - `group_content` .
    """

    name: str = pydantic.Field()
    """
    The name of the collection or section.
    """

    description: str = pydantic.Field()
    """
    The description of the collection. Only available for collections.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
