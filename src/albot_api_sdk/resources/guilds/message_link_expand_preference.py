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
from ...types.guilds import message_link_expand_preference_update_params
from ...types.plain_api_response import PlainAPIResponse
from ...types.guilds.message_link_expand_preference_retrieve_response import MessageLinkExpandPreferenceRetrieveResponse

__all__ = ["MessageLinkExpandPreferenceResource", "AsyncMessageLinkExpandPreferenceResource"]


class MessageLinkExpandPreferenceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessageLinkExpandPreferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return MessageLinkExpandPreferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessageLinkExpandPreferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#with_streaming_response
        """
        return MessageLinkExpandPreferenceResourceWithStreamingResponse(self)

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
    ) -> MessageLinkExpandPreferenceRetrieveResponse:
        """
        Get Guild Message Link Expand Pref

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/guilds/{guild_id}/message_link_expand_preference", guild_id=guild_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageLinkExpandPreferenceRetrieveResponse,
        )

    def update(
        self,
        guild_id: int,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Update Guild Message Link Expand Pref

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            path_template("/guilds/{guild_id}/message_link_expand_preference", guild_id=guild_id),
            body=maybe_transform(
                {"enabled": enabled},
                message_link_expand_preference_update_params.MessageLinkExpandPreferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )


class AsyncMessageLinkExpandPreferenceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessageLinkExpandPreferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncMessageLinkExpandPreferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessageLinkExpandPreferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#with_streaming_response
        """
        return AsyncMessageLinkExpandPreferenceResourceWithStreamingResponse(self)

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
    ) -> MessageLinkExpandPreferenceRetrieveResponse:
        """
        Get Guild Message Link Expand Pref

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/guilds/{guild_id}/message_link_expand_preference", guild_id=guild_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageLinkExpandPreferenceRetrieveResponse,
        )

    async def update(
        self,
        guild_id: int,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Update Guild Message Link Expand Pref

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            path_template("/guilds/{guild_id}/message_link_expand_preference", guild_id=guild_id),
            body=await async_maybe_transform(
                {"enabled": enabled},
                message_link_expand_preference_update_params.MessageLinkExpandPreferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )


class MessageLinkExpandPreferenceResourceWithRawResponse:
    def __init__(self, message_link_expand_preference: MessageLinkExpandPreferenceResource) -> None:
        self._message_link_expand_preference = message_link_expand_preference

        self.retrieve = to_raw_response_wrapper(
            message_link_expand_preference.retrieve,
        )
        self.update = to_raw_response_wrapper(
            message_link_expand_preference.update,
        )


class AsyncMessageLinkExpandPreferenceResourceWithRawResponse:
    def __init__(self, message_link_expand_preference: AsyncMessageLinkExpandPreferenceResource) -> None:
        self._message_link_expand_preference = message_link_expand_preference

        self.retrieve = async_to_raw_response_wrapper(
            message_link_expand_preference.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            message_link_expand_preference.update,
        )


class MessageLinkExpandPreferenceResourceWithStreamingResponse:
    def __init__(self, message_link_expand_preference: MessageLinkExpandPreferenceResource) -> None:
        self._message_link_expand_preference = message_link_expand_preference

        self.retrieve = to_streamed_response_wrapper(
            message_link_expand_preference.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            message_link_expand_preference.update,
        )


class AsyncMessageLinkExpandPreferenceResourceWithStreamingResponse:
    def __init__(self, message_link_expand_preference: AsyncMessageLinkExpandPreferenceResource) -> None:
        self._message_link_expand_preference = message_link_expand_preference

        self.retrieve = async_to_streamed_response_wrapper(
            message_link_expand_preference.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            message_link_expand_preference.update,
        )
