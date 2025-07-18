# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.unchecked_base_model import UncheckedBaseModel
from .addressable_list import AddressableList


class ContactTags(UncheckedBaseModel):
    """
    An object containing tags meta data about the tags that a contact has. Up to 10 will be displayed here. Use the url to get more.
    """

    data: typing.Optional[typing.List[AddressableList]] = pydantic.Field(default=None)
    """
    This object represents the tags attached to a contact.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    url to get more tag resources for this contact
    """

    total_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Int representing the total number of tags attached to this contact
    """

    has_more: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether there's more Addressable Objects to be viewed. If true, use the url to view all
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
