# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from .contact_reference import ContactReference


class ContactArchived(ContactReference):
    """
    archived contact object
    """

    archived: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the contact is archived or not.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
