# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import shard_list_params, shard_post_metrics_params, shard_get_connection_commands_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.plain_api_response import PlainAPIResponse
from ..types.shard_list_response import ShardListResponse
from ..types.shard_assign_response import ShardAssignResponse
from ..types.shard_get_connection_commands_response import ShardGetConnectionCommandsResponse

__all__ = ["ShardsResource", "AsyncShardsResource"]


class ShardsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return ShardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#with_streaming_response
        """
        return ShardsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        status: Literal["online", "offline", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShardListResponse:
        """
        Index

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/shards",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, shard_list_params.ShardListParams),
            ),
            cast_to=ShardListResponse,
        )

    def assign(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShardAssignResponse:
        """Assign Shard"""
        return self._get(
            "/shards/assign",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShardAssignResponse,
        )

    def get_connection_commands(
        self,
        shard_id: int,
        *,
        changes_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShardGetConnectionCommandsResponse:
        """
        Get Connection Commands

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/shards/{shard_id}/connection_commands",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"changes_only": changes_only},
                    shard_get_connection_commands_params.ShardGetConnectionCommandsParams,
                ),
            ),
            cast_to=ShardGetConnectionCommandsResponse,
        )

    def post_metrics(
        self,
        shard_id: int,
        *,
        connected: Optional[int] | Omit = omit,
        guilds: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Post Metrics

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/shards/{shard_id}/metrics",
            body=maybe_transform(
                {
                    "connected": connected,
                    "guilds": guilds,
                },
                shard_post_metrics_params.ShardPostMetricsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )

    def release(
        self,
        shard_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Release Shard

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/shards/{shard_id}/release",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )


class AsyncShardsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncShardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#with_streaming_response
        """
        return AsyncShardsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        status: Literal["online", "offline", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShardListResponse:
        """
        Index

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/shards",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"status": status}, shard_list_params.ShardListParams),
            ),
            cast_to=ShardListResponse,
        )

    async def assign(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShardAssignResponse:
        """Assign Shard"""
        return await self._get(
            "/shards/assign",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShardAssignResponse,
        )

    async def get_connection_commands(
        self,
        shard_id: int,
        *,
        changes_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ShardGetConnectionCommandsResponse:
        """
        Get Connection Commands

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/shards/{shard_id}/connection_commands",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"changes_only": changes_only},
                    shard_get_connection_commands_params.ShardGetConnectionCommandsParams,
                ),
            ),
            cast_to=ShardGetConnectionCommandsResponse,
        )

    async def post_metrics(
        self,
        shard_id: int,
        *,
        connected: Optional[int] | Omit = omit,
        guilds: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Post Metrics

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/shards/{shard_id}/metrics",
            body=await async_maybe_transform(
                {
                    "connected": connected,
                    "guilds": guilds,
                },
                shard_post_metrics_params.ShardPostMetricsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )

    async def release(
        self,
        shard_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Release Shard

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/shards/{shard_id}/release",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )


class ShardsResourceWithRawResponse:
    def __init__(self, shards: ShardsResource) -> None:
        self._shards = shards

        self.list = to_raw_response_wrapper(
            shards.list,
        )
        self.assign = to_raw_response_wrapper(
            shards.assign,
        )
        self.get_connection_commands = to_raw_response_wrapper(
            shards.get_connection_commands,
        )
        self.post_metrics = to_raw_response_wrapper(
            shards.post_metrics,
        )
        self.release = to_raw_response_wrapper(
            shards.release,
        )


class AsyncShardsResourceWithRawResponse:
    def __init__(self, shards: AsyncShardsResource) -> None:
        self._shards = shards

        self.list = async_to_raw_response_wrapper(
            shards.list,
        )
        self.assign = async_to_raw_response_wrapper(
            shards.assign,
        )
        self.get_connection_commands = async_to_raw_response_wrapper(
            shards.get_connection_commands,
        )
        self.post_metrics = async_to_raw_response_wrapper(
            shards.post_metrics,
        )
        self.release = async_to_raw_response_wrapper(
            shards.release,
        )


class ShardsResourceWithStreamingResponse:
    def __init__(self, shards: ShardsResource) -> None:
        self._shards = shards

        self.list = to_streamed_response_wrapper(
            shards.list,
        )
        self.assign = to_streamed_response_wrapper(
            shards.assign,
        )
        self.get_connection_commands = to_streamed_response_wrapper(
            shards.get_connection_commands,
        )
        self.post_metrics = to_streamed_response_wrapper(
            shards.post_metrics,
        )
        self.release = to_streamed_response_wrapper(
            shards.release,
        )


class AsyncShardsResourceWithStreamingResponse:
    def __init__(self, shards: AsyncShardsResource) -> None:
        self._shards = shards

        self.list = async_to_streamed_response_wrapper(
            shards.list,
        )
        self.assign = async_to_streamed_response_wrapper(
            shards.assign,
        )
        self.get_connection_commands = async_to_streamed_response_wrapper(
            shards.get_connection_commands,
        )
        self.post_metrics = async_to_streamed_response_wrapper(
            shards.post_metrics,
        )
        self.release = async_to_streamed_response_wrapper(
            shards.release,
        )
