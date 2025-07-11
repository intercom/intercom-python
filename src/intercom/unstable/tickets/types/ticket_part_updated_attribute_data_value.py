# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel
from .ticket_part_updated_attribute_data_value_id import TicketPartUpdatedAttributeDataValueId
from .ticket_part_updated_attribute_data_value_label import TicketPartUpdatedAttributeDataValueLabel


class TicketPartUpdatedAttributeDataValue(UncheckedBaseModel):
    """
    The new value of the attribute.
    """

    type: typing.Literal["value"] = pydantic.Field(default="value")
    """
    The type of the object. Always 'value'.
    """

    id: TicketPartUpdatedAttributeDataValueId
    label: TicketPartUpdatedAttributeDataValueLabel

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
