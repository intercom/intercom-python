# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..companies.types.company import Company
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .pages_link import PagesLink


class ContactAttachedCompanies(UncheckedBaseModel):
    """
    A list of Company Objects
    """

    type: typing.Literal["list"] = pydantic.Field(default="list")
    """
    The type of object
    """

    companies: typing.List[Company] = pydantic.Field()
    """
    An array containing Company Objects
    """

    total_count: int = pydantic.Field()
    """
    The total number of companies associated to this contact
    """

    pages: typing.Optional[PagesLink] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
