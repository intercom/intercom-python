# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..companies.types.company import Company
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .cursor_pages import CursorPages


class CompanyScroll(UncheckedBaseModel):
    """
    Companies allow you to represent organizations using your product. Each company will have its own description and be associated with contacts. You can fetch, create, update and list companies.
    """

    type: typing.Literal["list"] = pydantic.Field(default="list")
    """
    The type of object - `list`
    """

    data: typing.List[Company]
    pages: typing.Optional[CursorPages] = None
    total_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of companies
    """

    scroll_param: typing.Optional[str] = pydantic.Field(default=None)
    """
    The scroll parameter to use in the next request to fetch the next page of results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
