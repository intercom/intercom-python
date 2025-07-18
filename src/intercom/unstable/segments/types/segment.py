# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel
from .segment_person_type import SegmentPersonType


class Segment(UncheckedBaseModel):
    """
    A segment is a group of your contacts defined by the rules that you set.
    """

    type: typing.Optional[typing.Literal["segment"]] = pydantic.Field(default=None)
    """
    The type of object.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier representing the segment.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the segment.
    """

    created_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The time the segment was created.
    """

    updated_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The time the segment was updated.
    """

    person_type: typing.Optional[SegmentPersonType] = pydantic.Field(default=None)
    """
    Type of the contact: contact (lead) or user.
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of items in the user segment. It's returned when `include_count=true` is included in the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
