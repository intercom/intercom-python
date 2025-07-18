# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class Event(UncheckedBaseModel):
    """
    The event object enables Intercom to know more about the actions that took place in your app. Currently, you can only tell us when an app's flow has been completed.
    """

    type: typing.Literal["completed"] = pydantic.Field(default="completed")
    """
    What action took place. The only value currently accepted is `completed`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
