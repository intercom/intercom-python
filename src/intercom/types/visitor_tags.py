# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .visitor_tags_tags_item import VisitorTagsTagsItem


class VisitorTags(UncheckedBaseModel):
    type: typing.Optional[typing.Literal["tag.list"]] = pydantic.Field(default=None)
    """
    The type of the object
    """

    tags: typing.Optional[typing.List[VisitorTagsTagsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
