# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .orders import (
    OrdersResource,
    AsyncOrdersResource,
    OrdersResourceWithRawResponse,
    AsyncOrdersResourceWithRawResponse,
    OrdersResourceWithStreamingResponse,
    AsyncOrdersResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.petst000re_list_inventory_response import Petst000reListInventoryResponse

__all__ = ["Petst000reResource", "AsyncPetst000reResource"]


class Petst000reResource(SyncAPIResource):
    @cached_property
    def orders(self) -> OrdersResource:
        return OrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> Petst000reResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jd-st/jd-project-python#accessing-raw-response-data-eg-headers
        """
        return Petst000reResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Petst000reResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jd-st/jd-project-python#with_streaming_response
        """
        return Petst000reResourceWithStreamingResponse(self)

    def list_inventory(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Petst000reListInventoryResponse:
        """Returns a map of status codes to quantities"""
        return self._get(
            "/petst000re/inventory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Petst000reListInventoryResponse,
        )


class AsyncPetst000reResource(AsyncAPIResource):
    @cached_property
    def orders(self) -> AsyncOrdersResource:
        return AsyncOrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPetst000reResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jd-st/jd-project-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPetst000reResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPetst000reResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jd-st/jd-project-python#with_streaming_response
        """
        return AsyncPetst000reResourceWithStreamingResponse(self)

    async def list_inventory(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Petst000reListInventoryResponse:
        """Returns a map of status codes to quantities"""
        return await self._get(
            "/petst000re/inventory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Petst000reListInventoryResponse,
        )


class Petst000reResourceWithRawResponse:
    def __init__(self, petst000re: Petst000reResource) -> None:
        self._petst000re = petst000re

        self.list_inventory = to_raw_response_wrapper(
            petst000re.list_inventory,
        )

    @cached_property
    def orders(self) -> OrdersResourceWithRawResponse:
        return OrdersResourceWithRawResponse(self._petst000re.orders)


class AsyncPetst000reResourceWithRawResponse:
    def __init__(self, petst000re: AsyncPetst000reResource) -> None:
        self._petst000re = petst000re

        self.list_inventory = async_to_raw_response_wrapper(
            petst000re.list_inventory,
        )

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithRawResponse:
        return AsyncOrdersResourceWithRawResponse(self._petst000re.orders)


class Petst000reResourceWithStreamingResponse:
    def __init__(self, petst000re: Petst000reResource) -> None:
        self._petst000re = petst000re

        self.list_inventory = to_streamed_response_wrapper(
            petst000re.list_inventory,
        )

    @cached_property
    def orders(self) -> OrdersResourceWithStreamingResponse:
        return OrdersResourceWithStreamingResponse(self._petst000re.orders)


class AsyncPetst000reResourceWithStreamingResponse:
    def __init__(self, petst000re: AsyncPetst000reResource) -> None:
        self._petst000re = petst000re

        self.list_inventory = async_to_streamed_response_wrapper(
            petst000re.list_inventory,
        )

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithStreamingResponse:
        return AsyncOrdersResourceWithStreamingResponse(self._petst000re.orders)
