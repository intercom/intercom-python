# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.data_attribute_list import DataAttributeList
from .raw_client import AsyncRawDataAttributesClient, RawDataAttributesClient
from .types.create_data_attribute_request_data_type import CreateDataAttributeRequestDataType
from .types.create_data_attribute_request_model import CreateDataAttributeRequestModel
from .types.data_attribute import DataAttribute
from .types.data_attributes_list_request_model import DataAttributesListRequestModel
from .types.update_data_attribute_request_options_item import UpdateDataAttributeRequestOptionsItem

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DataAttributesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDataAttributesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDataAttributesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDataAttributesClient
        """
        return self._raw_client

    def list(
        self,
        *,
        model: typing.Optional[DataAttributesListRequestModel] = None,
        include_archived: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataAttributeList:
        """
        You can fetch a list of all data attributes belonging to a workspace for contacts, companies or conversations.

        Parameters
        ----------
        model : typing.Optional[DataAttributesListRequestModel]
            Specify the data attribute model to return.

        include_archived : typing.Optional[bool]
            Include archived attributes in the list. By default we return only non archived data attributes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataAttributeList
            Successful response

        Examples
        --------
        from intercom import Intercom

        client = Intercom(
            token="YOUR_TOKEN",
        )
        client.data_attributes.list()
        """
        _response = self._raw_client.list(
            model=model, include_archived=include_archived, request_options=request_options
        )
        return _response.data

    def create(
        self,
        *,
        name: str,
        model: CreateDataAttributeRequestModel,
        data_type: CreateDataAttributeRequestDataType,
        description: typing.Optional[str] = OMIT,
        options: typing.Optional[typing.Sequence[str]] = OMIT,
        messenger_writable: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataAttribute:
        """
        You can create a data attributes for a `contact` or a `company`.

        Parameters
        ----------
        name : str
            The name of the data attribute.

        model : CreateDataAttributeRequestModel
            The model that the data attribute belongs to.

        data_type : CreateDataAttributeRequestDataType
            The type of data stored for this attribute.

        description : typing.Optional[str]
            The readable description you see in the UI for the attribute.

        options : typing.Optional[typing.Sequence[str]]
            To create list attributes. Provide a set of hashes with `value` as the key of the options you want to make. `data_type` must be `string`.

        messenger_writable : typing.Optional[bool]
            Can this attribute be updated by the Messenger

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataAttribute
            Successful

        Examples
        --------
        from intercom import Intercom

        client = Intercom(
            token="YOUR_TOKEN",
        )
        client.data_attributes.create(
            name="Mithril Shirt",
            model="company",
            data_type="string",
        )
        """
        _response = self._raw_client.create(
            name=name,
            model=model,
            data_type=data_type,
            description=description,
            options=options,
            messenger_writable=messenger_writable,
            request_options=request_options,
        )
        return _response.data

    def update(
        self,
        data_attribute_id: str,
        *,
        archived: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        options: typing.Optional[typing.Sequence[UpdateDataAttributeRequestOptionsItem]] = OMIT,
        messenger_writable: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataAttribute:
        """

        You can update a data attribute.

        > 🚧 Updating the data type is not possible
        >
        > It is currently a dangerous action to execute changing a data attribute's type via the API. You will need to update the type via the UI instead.

        Parameters
        ----------
        data_attribute_id : str
            The data attribute id

        archived : typing.Optional[bool]
            Whether the attribute is to be archived or not.

        description : typing.Optional[str]
            The readable description you see in the UI for the attribute.

        options : typing.Optional[typing.Sequence[UpdateDataAttributeRequestOptionsItem]]
            To create list attributes. Provide a set of hashes with `value` as the key of the options you want to make. `data_type` must be `string`.

        messenger_writable : typing.Optional[bool]
            Can this attribute be updated by the Messenger

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataAttribute
            Successful

        Examples
        --------
        from intercom import Intercom
        from intercom.data_attributes import UpdateDataAttributeRequestOptionsItem

        client = Intercom(
            token="YOUR_TOKEN",
        )
        client.data_attributes.update(
            data_attribute_id="1",
            archived=False,
            description="Just a plain old ring",
            options=[
                UpdateDataAttributeRequestOptionsItem(
                    value="1-10",
                ),
                UpdateDataAttributeRequestOptionsItem(
                    value="11-20",
                ),
            ],
        )
        """
        _response = self._raw_client.update(
            data_attribute_id,
            archived=archived,
            description=description,
            options=options,
            messenger_writable=messenger_writable,
            request_options=request_options,
        )
        return _response.data


class AsyncDataAttributesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDataAttributesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDataAttributesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDataAttributesClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        model: typing.Optional[DataAttributesListRequestModel] = None,
        include_archived: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataAttributeList:
        """
        You can fetch a list of all data attributes belonging to a workspace for contacts, companies or conversations.

        Parameters
        ----------
        model : typing.Optional[DataAttributesListRequestModel]
            Specify the data attribute model to return.

        include_archived : typing.Optional[bool]
            Include archived attributes in the list. By default we return only non archived data attributes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataAttributeList
            Successful response

        Examples
        --------
        import asyncio

        from intercom import AsyncIntercom

        client = AsyncIntercom(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.data_attributes.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            model=model, include_archived=include_archived, request_options=request_options
        )
        return _response.data

    async def create(
        self,
        *,
        name: str,
        model: CreateDataAttributeRequestModel,
        data_type: CreateDataAttributeRequestDataType,
        description: typing.Optional[str] = OMIT,
        options: typing.Optional[typing.Sequence[str]] = OMIT,
        messenger_writable: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataAttribute:
        """
        You can create a data attributes for a `contact` or a `company`.

        Parameters
        ----------
        name : str
            The name of the data attribute.

        model : CreateDataAttributeRequestModel
            The model that the data attribute belongs to.

        data_type : CreateDataAttributeRequestDataType
            The type of data stored for this attribute.

        description : typing.Optional[str]
            The readable description you see in the UI for the attribute.

        options : typing.Optional[typing.Sequence[str]]
            To create list attributes. Provide a set of hashes with `value` as the key of the options you want to make. `data_type` must be `string`.

        messenger_writable : typing.Optional[bool]
            Can this attribute be updated by the Messenger

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataAttribute
            Successful

        Examples
        --------
        import asyncio

        from intercom import AsyncIntercom

        client = AsyncIntercom(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.data_attributes.create(
                name="Mithril Shirt",
                model="company",
                data_type="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            name=name,
            model=model,
            data_type=data_type,
            description=description,
            options=options,
            messenger_writable=messenger_writable,
            request_options=request_options,
        )
        return _response.data

    async def update(
        self,
        data_attribute_id: str,
        *,
        archived: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        options: typing.Optional[typing.Sequence[UpdateDataAttributeRequestOptionsItem]] = OMIT,
        messenger_writable: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DataAttribute:
        """

        You can update a data attribute.

        > 🚧 Updating the data type is not possible
        >
        > It is currently a dangerous action to execute changing a data attribute's type via the API. You will need to update the type via the UI instead.

        Parameters
        ----------
        data_attribute_id : str
            The data attribute id

        archived : typing.Optional[bool]
            Whether the attribute is to be archived or not.

        description : typing.Optional[str]
            The readable description you see in the UI for the attribute.

        options : typing.Optional[typing.Sequence[UpdateDataAttributeRequestOptionsItem]]
            To create list attributes. Provide a set of hashes with `value` as the key of the options you want to make. `data_type` must be `string`.

        messenger_writable : typing.Optional[bool]
            Can this attribute be updated by the Messenger

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DataAttribute
            Successful

        Examples
        --------
        import asyncio

        from intercom import AsyncIntercom
        from intercom.data_attributes import UpdateDataAttributeRequestOptionsItem

        client = AsyncIntercom(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.data_attributes.update(
                data_attribute_id="1",
                archived=False,
                description="Just a plain old ring",
                options=[
                    UpdateDataAttributeRequestOptionsItem(
                        value="1-10",
                    ),
                    UpdateDataAttributeRequestOptionsItem(
                        value="11-20",
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            data_attribute_id,
            archived=archived,
            description=description,
            options=options,
            messenger_writable=messenger_writable,
            request_options=request_options,
        )
        return _response.data
