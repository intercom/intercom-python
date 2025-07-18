# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from ..subscription_types.types.subscription_type import SubscriptionType


class SubscriptionTypeList(UncheckedBaseModel):
    """
    A list of subscription type objects.
    """

    type: typing.Literal["list"] = pydantic.Field(default="list")
    """
    The type of the object
    """

    data: typing.List[SubscriptionType] = pydantic.Field()
    """
    A list of subscription type objects associated with the workspace .
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
