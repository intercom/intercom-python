# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from ...core.unchecked_base_model import UncheckedBaseModel
from .multiple_filter_search_request_operator import MultipleFilterSearchRequestOperator


class MultipleFilterSearchRequest(UncheckedBaseModel):
    """
    Search using Intercoms Search APIs with more than one filter.
    """

    operator: typing.Optional[MultipleFilterSearchRequestOperator] = pydantic.Field(default=None)
    """
    An operator to allow boolean inspection between multiple fields.
    """

    value: typing.Optional["MultipleFilterSearchRequestValue"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .multiple_filter_search_request_value import MultipleFilterSearchRequestValue  # noqa: E402, F401, I001

update_forward_refs(MultipleFilterSearchRequest)
