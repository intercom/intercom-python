# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .action_component import ActionComponent
from .single_select_component_save_state import SingleSelectComponentSaveState
from .single_select_option import SingleSelectOption


class SingleSelectComponent(UncheckedBaseModel):
    """
    A single-select component is used to capture a choice from up to 10 options that you provide. You can submit the value of the select option by:

    - Adding an `action` to the single-select component
    - Using a ButtonComponent (which will submit all interactive components in the canvas)

    When a submit action takes place, the results are given in a hash with the `id` from the single-select component used as the key and the `id` from the chosen option as the value.
    """

    id: str = pydantic.Field()
    """
    A unique identifier for the component.
    """

    options: typing.List[SingleSelectOption] = pydantic.Field()
    """
    The list of options. Can provide 2 to 10.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text shown above the options.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The option that is selected by default.
    """

    save_state: typing.Optional[SingleSelectComponentSaveState] = pydantic.Field(default=None)
    """
    Styles the input. Default is `unsaved`. Prevent action with `saved`.
    """

    disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Styles all options and prevents the action. Default is false. Will be overridden if save_state is saved.
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
