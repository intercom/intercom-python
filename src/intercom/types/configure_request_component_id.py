# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..admins.types.admin import Admin
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .canvas_object import CanvasObject
from .context import Context


class ConfigureRequestComponentId(UncheckedBaseModel):
    workspace_id: str = pydantic.Field()
    """
    The workspace ID of the teammate. Attribute is app_id for V1.2 and below.
    """

    workspace_region: str = pydantic.Field()
    """
    The Intercom hosted region that this app is located in.
    """

    component_id: str = pydantic.Field()
    """
    The id of the component clicked by the teammate to trigger the request.
    """

    admin: Admin = pydantic.Field()
    """
    The Intercom teammate configuring the app.
    """

    context: Context = pydantic.Field()
    """
    The context of where the app is added, where the user last visited, and information on the Messenger settings.
    """

    current_canvas: CanvasObject = pydantic.Field()
    """
    The current canvas the teammate can see.
    """

    input_values: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field()
    """
    A list of key/value pairs of data, inputted by the teammate on the current canvas.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
