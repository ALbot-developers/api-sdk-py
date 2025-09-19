# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.users.me import guild_list_params
from ....types.users.me.guild_list_response import GuildListResponse
from ....types.users.me.guild_retrieve_info_response import GuildRetrieveInfoResponse

__all__ = ["GuildsResource", "AsyncGuildsResource"]


class GuildsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GuildsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return GuildsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GuildsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#with_streaming_response
        """
        return GuildsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        mutual: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GuildListResponse:
        """
        List User Guilds

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/users/me/guilds",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"mutual": mutual}, guild_list_params.GuildListParams),
            ),
            cast_to=GuildListResponse,
        )

    def retrieve_info(
        self,
        guild_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GuildRetrieveInfoResponse:
        """
        Get Guild Info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/users/me/guilds/{guild_id}/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GuildRetrieveInfoResponse,
        )


class AsyncGuildsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGuildsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncGuildsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGuildsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#with_streaming_response
        """
        return AsyncGuildsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        mutual: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GuildListResponse:
        """
        List User Guilds

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/users/me/guilds",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"mutual": mutual}, guild_list_params.GuildListParams),
            ),
            cast_to=GuildListResponse,
        )

    async def retrieve_info(
        self,
        guild_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GuildRetrieveInfoResponse:
        """
        Get Guild Info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/users/me/guilds/{guild_id}/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GuildRetrieveInfoResponse,
        )


class GuildsResourceWithRawResponse:
    def __init__(self, guilds: GuildsResource) -> None:
        self._guilds = guilds

        self.list = to_raw_response_wrapper(
            guilds.list,
        )
        self.retrieve_info = to_raw_response_wrapper(
            guilds.retrieve_info,
        )


class AsyncGuildsResourceWithRawResponse:
    def __init__(self, guilds: AsyncGuildsResource) -> None:
        self._guilds = guilds

        self.list = async_to_raw_response_wrapper(
            guilds.list,
        )
        self.retrieve_info = async_to_raw_response_wrapper(
            guilds.retrieve_info,
        )


class GuildsResourceWithStreamingResponse:
    def __init__(self, guilds: GuildsResource) -> None:
        self._guilds = guilds

        self.list = to_streamed_response_wrapper(
            guilds.list,
        )
        self.retrieve_info = to_streamed_response_wrapper(
            guilds.retrieve_info,
        )


class AsyncGuildsResourceWithStreamingResponse:
    def __init__(self, guilds: AsyncGuildsResource) -> None:
        self._guilds = guilds

        self.list = async_to_streamed_response_wrapper(
            guilds.list,
        )
        self.retrieve_info = async_to_streamed_response_wrapper(
            guilds.retrieve_info,
        )
