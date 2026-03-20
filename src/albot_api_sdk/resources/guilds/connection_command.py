# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.guilds import connection_command_update_params
from ...types.plain_api_response import PlainAPIResponse
from ...types.guilds.connection_command_retrieve_response import ConnectionCommandRetrieveResponse

__all__ = ["ConnectionCommandResource", "AsyncConnectionCommandResource"]


class ConnectionCommandResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConnectionCommandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return ConnectionCommandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectionCommandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#with_streaming_response
        """
        return ConnectionCommandResourceWithStreamingResponse(self)

    def retrieve(
        self,
        guild_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionCommandRetrieveResponse:
        """
        Get Guild Connection Command

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/guilds/{guild_id}/connection_command", guild_id=guild_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionCommandRetrieveResponse,
        )

    def update(
        self,
        guild_id: int,
        *,
        command: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Update Guild Connection Command

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            path_template("/guilds/{guild_id}/connection_command", guild_id=guild_id),
            body=maybe_transform({"command": command}, connection_command_update_params.ConnectionCommandUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )


class AsyncConnectionCommandResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConnectionCommandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectionCommandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectionCommandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#with_streaming_response
        """
        return AsyncConnectionCommandResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        guild_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConnectionCommandRetrieveResponse:
        """
        Get Guild Connection Command

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/guilds/{guild_id}/connection_command", guild_id=guild_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConnectionCommandRetrieveResponse,
        )

    async def update(
        self,
        guild_id: int,
        *,
        command: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Update Guild Connection Command

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            path_template("/guilds/{guild_id}/connection_command", guild_id=guild_id),
            body=await async_maybe_transform(
                {"command": command}, connection_command_update_params.ConnectionCommandUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )


class ConnectionCommandResourceWithRawResponse:
    def __init__(self, connection_command: ConnectionCommandResource) -> None:
        self._connection_command = connection_command

        self.retrieve = to_raw_response_wrapper(
            connection_command.retrieve,
        )
        self.update = to_raw_response_wrapper(
            connection_command.update,
        )


class AsyncConnectionCommandResourceWithRawResponse:
    def __init__(self, connection_command: AsyncConnectionCommandResource) -> None:
        self._connection_command = connection_command

        self.retrieve = async_to_raw_response_wrapper(
            connection_command.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            connection_command.update,
        )


class ConnectionCommandResourceWithStreamingResponse:
    def __init__(self, connection_command: ConnectionCommandResource) -> None:
        self._connection_command = connection_command

        self.retrieve = to_streamed_response_wrapper(
            connection_command.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            connection_command.update,
        )


class AsyncConnectionCommandResourceWithStreamingResponse:
    def __init__(self, connection_command: AsyncConnectionCommandResource) -> None:
        self._connection_command = connection_command

        self.retrieve = async_to_streamed_response_wrapper(
            connection_command.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            connection_command.update,
        )
