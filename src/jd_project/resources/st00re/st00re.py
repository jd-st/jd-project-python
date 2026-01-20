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
from ...types.st00re_list_inventory_response import St00reListInventoryResponse

__all__ = ["St00reResource", "AsyncSt00reResource"]


class St00reResource(SyncAPIResource):
    @cached_property
    def orders(self) -> OrdersResource:
        return OrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> St00reResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jd-st/jd-project-python#accessing-raw-response-data-eg-headers
        """
        return St00reResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> St00reResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jd-st/jd-project-python#with_streaming_response
        """
        return St00reResourceWithStreamingResponse(self)

    def list_inventory(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> St00reListInventoryResponse:
        """Returns a map of status codes to quantities"""
        return self._get(
            "/st00re/inventory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=St00reListInventoryResponse,
        )


class AsyncSt00reResource(AsyncAPIResource):
    @cached_property
    def orders(self) -> AsyncOrdersResource:
        return AsyncOrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSt00reResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jd-st/jd-project-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSt00reResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSt00reResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jd-st/jd-project-python#with_streaming_response
        """
        return AsyncSt00reResourceWithStreamingResponse(self)

    async def list_inventory(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> St00reListInventoryResponse:
        """Returns a map of status codes to quantities"""
        return await self._get(
            "/st00re/inventory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=St00reListInventoryResponse,
        )


class St00reResourceWithRawResponse:
    def __init__(self, st00re: St00reResource) -> None:
        self._st00re = st00re

        self.list_inventory = to_raw_response_wrapper(
            st00re.list_inventory,
        )

    @cached_property
    def orders(self) -> OrdersResourceWithRawResponse:
        return OrdersResourceWithRawResponse(self._st00re.orders)


class AsyncSt00reResourceWithRawResponse:
    def __init__(self, st00re: AsyncSt00reResource) -> None:
        self._st00re = st00re

        self.list_inventory = async_to_raw_response_wrapper(
            st00re.list_inventory,
        )

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithRawResponse:
        return AsyncOrdersResourceWithRawResponse(self._st00re.orders)


class St00reResourceWithStreamingResponse:
    def __init__(self, st00re: St00reResource) -> None:
        self._st00re = st00re

        self.list_inventory = to_streamed_response_wrapper(
            st00re.list_inventory,
        )

    @cached_property
    def orders(self) -> OrdersResourceWithStreamingResponse:
        return OrdersResourceWithStreamingResponse(self._st00re.orders)


class AsyncSt00reResourceWithStreamingResponse:
    def __init__(self, st00re: AsyncSt00reResource) -> None:
        self._st00re = st00re

        self.list_inventory = async_to_streamed_response_wrapper(
            st00re.list_inventory,
        )

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithStreamingResponse:
        return AsyncOrdersResourceWithStreamingResponse(self._st00re.orders)
