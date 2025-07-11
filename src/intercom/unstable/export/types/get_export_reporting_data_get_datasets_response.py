# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel
from .get_export_reporting_data_get_datasets_response_data_item import GetExportReportingDataGetDatasetsResponseDataItem


class GetExportReportingDataGetDatasetsResponse(UncheckedBaseModel):
    type: typing.Optional[str] = None
    data: typing.Optional[typing.List[GetExportReportingDataGetDatasetsResponseDataItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
