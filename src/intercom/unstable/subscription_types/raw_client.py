# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.jsonable_encoder import jsonable_encoder
from ...core.request_options import RequestOptions
from ...core.unchecked_base_model import construct_type
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from ..types.subscription_type_list import SubscriptionTypeList
from .types.subscription_type import SubscriptionType

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawSubscriptionTypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def attach_subscription_type_to_contact(
        self, contact_id: str, *, id: str, consent_type: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SubscriptionType]:
        """
        You can add a specific subscription to a contact. In Intercom, we have two different subscription types based on user consent - opt-out and opt-in:

          1.Attaching a contact to an opt-out subscription type will opt that user out from receiving messages related to that subscription type.

          2.Attaching a contact to an opt-in subscription type will opt that user in to receiving messages related to that subscription type.

        This will return a subscription type model for the subscription type that was added to the contact.

        Parameters
        ----------
        contact_id : str
            The unique identifier for the contact which is given by Intercom

        id : str
            The unique identifier for the subscription which is given by Intercom

        consent_type : str
            The consent_type of a subscription, opt_out or opt_in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscriptionType]
            Successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"contacts/{jsonable_encoder(contact_id)}/subscriptions",
            method="POST",
            json={
                "id": id,
                "consent_type": consent_type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionType,
                    construct_type(
                        type_=SubscriptionType,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        construct_type(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def detach_subscription_type_to_contact(
        self, contact_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SubscriptionType]:
        """
        You can remove a specific subscription from a contact. This will return a subscription type model for the subscription type that was removed from the contact.

        Parameters
        ----------
        contact_id : str
            The unique identifier for the contact which is given by Intercom

        id : str
            The unique identifier for the subscription type which is given by Intercom

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscriptionType]
            Successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"contacts/{jsonable_encoder(contact_id)}/subscriptions/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionType,
                    construct_type(
                        type_=SubscriptionType,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        construct_type(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_subscription_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SubscriptionTypeList]:
        """
        You can list all subscription types. A list of subscription type objects will be returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscriptionTypeList]
            Successful
        """
        _response = self._client_wrapper.httpx_client.request(
            "subscription_types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionTypeList,
                    construct_type(
                        type_=SubscriptionTypeList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        construct_type(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSubscriptionTypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def attach_subscription_type_to_contact(
        self, contact_id: str, *, id: str, consent_type: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SubscriptionType]:
        """
        You can add a specific subscription to a contact. In Intercom, we have two different subscription types based on user consent - opt-out and opt-in:

          1.Attaching a contact to an opt-out subscription type will opt that user out from receiving messages related to that subscription type.

          2.Attaching a contact to an opt-in subscription type will opt that user in to receiving messages related to that subscription type.

        This will return a subscription type model for the subscription type that was added to the contact.

        Parameters
        ----------
        contact_id : str
            The unique identifier for the contact which is given by Intercom

        id : str
            The unique identifier for the subscription which is given by Intercom

        consent_type : str
            The consent_type of a subscription, opt_out or opt_in.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscriptionType]
            Successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"contacts/{jsonable_encoder(contact_id)}/subscriptions",
            method="POST",
            json={
                "id": id,
                "consent_type": consent_type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionType,
                    construct_type(
                        type_=SubscriptionType,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        construct_type(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def detach_subscription_type_to_contact(
        self, contact_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SubscriptionType]:
        """
        You can remove a specific subscription from a contact. This will return a subscription type model for the subscription type that was removed from the contact.

        Parameters
        ----------
        contact_id : str
            The unique identifier for the contact which is given by Intercom

        id : str
            The unique identifier for the subscription type which is given by Intercom

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscriptionType]
            Successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"contacts/{jsonable_encoder(contact_id)}/subscriptions/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionType,
                    construct_type(
                        type_=SubscriptionType,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        construct_type(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_subscription_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SubscriptionTypeList]:
        """
        You can list all subscription types. A list of subscription type objects will be returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscriptionTypeList]
            Successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            "subscription_types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionTypeList,
                    construct_type(
                        type_=SubscriptionTypeList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        construct_type(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
