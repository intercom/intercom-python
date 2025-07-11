# This file was auto-generated by Fern from our API Definition.

import typing

from .create_data_event_request_with_email import CreateDataEventRequestWithEmail
from .create_data_event_request_with_id import CreateDataEventRequestWithId
from .create_data_event_request_with_user_id import CreateDataEventRequestWithUserId

CreateDataEventRequest = typing.Union[
    CreateDataEventRequestWithId, CreateDataEventRequestWithUserId, CreateDataEventRequestWithEmail
]
