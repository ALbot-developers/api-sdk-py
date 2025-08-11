# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .guilds import (
    GuildsResource,
    AsyncGuildsResource,
    GuildsResourceWithRawResponse,
    AsyncGuildsResourceWithRawResponse,
    GuildsResourceWithStreamingResponse,
    AsyncGuildsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)
from ....types.users import me_create_checkout_session_params
from ...._base_client import make_request_options
from ....types.url_api_response import URLAPIResponse
from ....types.users.me_retrieve_info_response import MeRetrieveInfoResponse

__all__ = ["MeResource", "AsyncMeResource"]


class MeResource(SyncAPIResource):
    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        return SubscriptionsResource(self._client)

    @cached_property
    def guilds(self) -> GuildsResource:
        return GuildsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return MeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#with_streaming_response
        """
        return MeResourceWithStreamingResponse(self)

    def create_checkout_session(
        self,
        *,
        plan: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLAPIResponse:
        """
        Checkout Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/users/me/checkout-session",
            body=maybe_transform({"plan": plan}, me_create_checkout_session_params.MeCreateCheckoutSessionParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLAPIResponse,
        )

    def retrieve_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeRetrieveInfoResponse:
        """Get User Info Api"""
        return self._get(
            "/users/me/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeRetrieveInfoResponse,
        )


class AsyncMeResource(AsyncAPIResource):
    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def guilds(self) -> AsyncGuildsResource:
        return AsyncGuildsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncMeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#with_streaming_response
        """
        return AsyncMeResourceWithStreamingResponse(self)

    async def create_checkout_session(
        self,
        *,
        plan: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLAPIResponse:
        """
        Checkout Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/users/me/checkout-session",
            body=await async_maybe_transform(
                {"plan": plan}, me_create_checkout_session_params.MeCreateCheckoutSessionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLAPIResponse,
        )

    async def retrieve_info(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeRetrieveInfoResponse:
        """Get User Info Api"""
        return await self._get(
            "/users/me/info",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeRetrieveInfoResponse,
        )


class MeResourceWithRawResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.create_checkout_session = to_raw_response_wrapper(
            me.create_checkout_session,
        )
        self.retrieve_info = to_raw_response_wrapper(
            me.retrieve_info,
        )

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        return SubscriptionsResourceWithRawResponse(self._me.subscriptions)

    @cached_property
    def guilds(self) -> GuildsResourceWithRawResponse:
        return GuildsResourceWithRawResponse(self._me.guilds)


class AsyncMeResourceWithRawResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.create_checkout_session = async_to_raw_response_wrapper(
            me.create_checkout_session,
        )
        self.retrieve_info = async_to_raw_response_wrapper(
            me.retrieve_info,
        )

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        return AsyncSubscriptionsResourceWithRawResponse(self._me.subscriptions)

    @cached_property
    def guilds(self) -> AsyncGuildsResourceWithRawResponse:
        return AsyncGuildsResourceWithRawResponse(self._me.guilds)


class MeResourceWithStreamingResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

        self.create_checkout_session = to_streamed_response_wrapper(
            me.create_checkout_session,
        )
        self.retrieve_info = to_streamed_response_wrapper(
            me.retrieve_info,
        )

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        return SubscriptionsResourceWithStreamingResponse(self._me.subscriptions)

    @cached_property
    def guilds(self) -> GuildsResourceWithStreamingResponse:
        return GuildsResourceWithStreamingResponse(self._me.guilds)


class AsyncMeResourceWithStreamingResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

        self.create_checkout_session = async_to_streamed_response_wrapper(
            me.create_checkout_session,
        )
        self.retrieve_info = async_to_streamed_response_wrapper(
            me.retrieve_info,
        )

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        return AsyncSubscriptionsResourceWithStreamingResponse(self._me.subscriptions)

    @cached_property
    def guilds(self) -> AsyncGuildsResourceWithStreamingResponse:
        return AsyncGuildsResourceWithStreamingResponse(self._me.guilds)
