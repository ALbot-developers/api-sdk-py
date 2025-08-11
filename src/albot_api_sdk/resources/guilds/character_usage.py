# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.guilds import character_usage_update_params
from ...types.plain_api_response import PlainAPIResponse
from ...types.guilds.character_usage_param import CharacterUsageParam
from ...types.guilds.character_usage_retrieve_response import CharacterUsageRetrieveResponse

__all__ = ["CharacterUsageResource", "AsyncCharacterUsageResource"]


class CharacterUsageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CharacterUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/albot-api-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CharacterUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CharacterUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/albot-api-sdk-python#with_streaming_response
        """
        return CharacterUsageResourceWithStreamingResponse(self)

    def retrieve(
        self,
        guild_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CharacterUsageRetrieveResponse:
        """
        Get Guild Character Usage Api

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/guilds/{guild_id}/character_usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CharacterUsageRetrieveResponse,
        )

    def update(
        self,
        guild_id: int,
        *,
        standard: Optional[CharacterUsageParam] | NotGiven = NOT_GIVEN,
        wavenet: Optional[CharacterUsageParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlainAPIResponse:
        """
        Update Guild Character Usage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/guilds/{guild_id}/character_usage",
            body=maybe_transform(
                {
                    "standard": standard,
                    "wavenet": wavenet,
                },
                character_usage_update_params.CharacterUsageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )


class AsyncCharacterUsageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCharacterUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/albot-api-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCharacterUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCharacterUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/albot-api-sdk-python#with_streaming_response
        """
        return AsyncCharacterUsageResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        guild_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CharacterUsageRetrieveResponse:
        """
        Get Guild Character Usage Api

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/guilds/{guild_id}/character_usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CharacterUsageRetrieveResponse,
        )

    async def update(
        self,
        guild_id: int,
        *,
        standard: Optional[CharacterUsageParam] | NotGiven = NOT_GIVEN,
        wavenet: Optional[CharacterUsageParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlainAPIResponse:
        """
        Update Guild Character Usage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/guilds/{guild_id}/character_usage",
            body=await async_maybe_transform(
                {
                    "standard": standard,
                    "wavenet": wavenet,
                },
                character_usage_update_params.CharacterUsageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )


class CharacterUsageResourceWithRawResponse:
    def __init__(self, character_usage: CharacterUsageResource) -> None:
        self._character_usage = character_usage

        self.retrieve = to_raw_response_wrapper(
            character_usage.retrieve,
        )
        self.update = to_raw_response_wrapper(
            character_usage.update,
        )


class AsyncCharacterUsageResourceWithRawResponse:
    def __init__(self, character_usage: AsyncCharacterUsageResource) -> None:
        self._character_usage = character_usage

        self.retrieve = async_to_raw_response_wrapper(
            character_usage.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            character_usage.update,
        )


class CharacterUsageResourceWithStreamingResponse:
    def __init__(self, character_usage: CharacterUsageResource) -> None:
        self._character_usage = character_usage

        self.retrieve = to_streamed_response_wrapper(
            character_usage.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            character_usage.update,
        )


class AsyncCharacterUsageResourceWithStreamingResponse:
    def __init__(self, character_usage: AsyncCharacterUsageResource) -> None:
        self._character_usage = character_usage

        self.retrieve = async_to_streamed_response_wrapper(
            character_usage.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            character_usage.update,
        )
