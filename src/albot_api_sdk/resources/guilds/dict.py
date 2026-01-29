# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.guilds import dict_replace_params
from ...types.plain_api_response import PlainAPIResponse
from ...types.guilds.dict_retrieve_response import DictRetrieveResponse

__all__ = ["DictResource", "AsyncDictResource"]


class DictResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DictResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return DictResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DictResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#with_streaming_response
        """
        return DictResourceWithStreamingResponse(self)

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
    ) -> DictRetrieveResponse:
        """
        Get Guild Dict Api

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/guilds/{guild_id}/dict",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DictRetrieveResponse,
        )

    def delete(
        self,
        guild_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Delete Guild Dict

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/guilds/{guild_id}/dict",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )

    def replace(
        self,
        guild_id: int,
        *,
        dict: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Replace Guild Dict

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/guilds/{guild_id}/dict",
            body=maybe_transform({"dict": dict}, dict_replace_params.DictReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )


class AsyncDictResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDictResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncDictResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDictResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#with_streaming_response
        """
        return AsyncDictResourceWithStreamingResponse(self)

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
    ) -> DictRetrieveResponse:
        """
        Get Guild Dict Api

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/guilds/{guild_id}/dict",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DictRetrieveResponse,
        )

    async def delete(
        self,
        guild_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Delete Guild Dict

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/guilds/{guild_id}/dict",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )

    async def replace(
        self,
        guild_id: int,
        *,
        dict: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Replace Guild Dict

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/guilds/{guild_id}/dict",
            body=await async_maybe_transform({"dict": dict}, dict_replace_params.DictReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )


class DictResourceWithRawResponse:
    def __init__(self, dict: DictResource) -> None:
        self._dict = dict

        self.retrieve = to_raw_response_wrapper(
            dict.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            dict.delete,
        )
        self.replace = to_raw_response_wrapper(
            dict.replace,
        )


class AsyncDictResourceWithRawResponse:
    def __init__(self, dict: AsyncDictResource) -> None:
        self._dict = dict

        self.retrieve = async_to_raw_response_wrapper(
            dict.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            dict.delete,
        )
        self.replace = async_to_raw_response_wrapper(
            dict.replace,
        )


class DictResourceWithStreamingResponse:
    def __init__(self, dict: DictResource) -> None:
        self._dict = dict

        self.retrieve = to_streamed_response_wrapper(
            dict.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            dict.delete,
        )
        self.replace = to_streamed_response_wrapper(
            dict.replace,
        )


class AsyncDictResourceWithStreamingResponse:
    def __init__(self, dict: AsyncDictResource) -> None:
        self._dict = dict

        self.retrieve = async_to_streamed_response_wrapper(
            dict.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            dict.delete,
        )
        self.replace = async_to_streamed_response_wrapper(
            dict.replace,
        )
