# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .content_object import ContentObject


class CanvasObject(UncheckedBaseModel):
    """
    You have to respond to the majority of requests with a canvas object. This will tell us what UI to show for your app.

    A canvas can either be static (meaning we send you the next request only when an action takes place) or live (meaning we send you the next request when someone views the app).

    - A static canvas needs a ContentObject which will contain the components to show.
    - A live canvas needs a `content_url` which we we will make the Live Canvas requests to when the app is viewed. This is only possible for apps viewed or used in the Messenger.
    """

    content: ContentObject = pydantic.Field()
    """
    The content object that will be shown as the UI of the app. Max Size is 64KB.
    """

    content_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL which we make Live Canvas requests to. You must respond to these with a content object. Max size is 64KB.
    """

    stored_data: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Optional Stored Data that you want to be returned in the next sent request. Max Size is 64KB.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
