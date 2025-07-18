# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .action_component import ActionComponent


class ListItem(UncheckedBaseModel):
    """
    A list item component that can be rendered in a list.
    """

    type: typing.Literal["item"] = pydantic.Field(default="item")
    """
    The type of component you are rendering.
    """

    id: str = pydantic.Field()
    """
    A unique identifier for the item.
    """

    title: str = pydantic.Field()
    """
    The text shown as the title for the item.
    """

    subtitle: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text shown underneath the item's title.
    """

    tertiary_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text shown next to the subtitle, separates by a bullet.
    """

    rounded_image: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Rounds the corners of the image. Default is `false`.
    """

    disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Styles all list items and prevents the action. Default is `false`.
    """

    action: typing.Optional[ActionComponent] = pydantic.Field(default=None)
    """
    This can be a Submit Action, URL Action, or Sheets Action.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
