# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import oauth2_callback_params, oauth2_redirect_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.url_api_response import URLAPIResponse
from ..types.plain_api_response import PlainAPIResponse

__all__ = ["Oauth2Resource", "AsyncOauth2Resource"]


class Oauth2Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> Oauth2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/albot-api-sdk-python#accessing-raw-response-data-eg-headers
        """
        return Oauth2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Oauth2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/albot-api-sdk-python#with_streaming_response
        """
        return Oauth2ResourceWithStreamingResponse(self)

    def callback(
        self,
        *,
        code: str,
        state: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlainAPIResponse:
        """
        Oauth2 Callback

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/oauth2/callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code": code,
                        "state": state,
                    },
                    oauth2_callback_params.Oauth2CallbackParams,
                ),
            ),
            cast_to=PlainAPIResponse,
        )

    def logout(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlainAPIResponse:
        """Logout"""
        return self._post(
            "/oauth2/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )

    def redirect(
        self,
        *,
        redirect: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLAPIResponse:
        """
        Oauth2 Redirect

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/oauth2/login",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"redirect": redirect}, oauth2_redirect_params.Oauth2RedirectParams),
            ),
            cast_to=URLAPIResponse,
        )


class AsyncOauth2Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOauth2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/albot-api-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOauth2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOauth2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/albot-api-sdk-python#with_streaming_response
        """
        return AsyncOauth2ResourceWithStreamingResponse(self)

    async def callback(
        self,
        *,
        code: str,
        state: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlainAPIResponse:
        """
        Oauth2 Callback

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/oauth2/callback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "code": code,
                        "state": state,
                    },
                    oauth2_callback_params.Oauth2CallbackParams,
                ),
            ),
            cast_to=PlainAPIResponse,
        )

    async def logout(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlainAPIResponse:
        """Logout"""
        return await self._post(
            "/oauth2/logout",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )

    async def redirect(
        self,
        *,
        redirect: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> URLAPIResponse:
        """
        Oauth2 Redirect

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/oauth2/login",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"redirect": redirect}, oauth2_redirect_params.Oauth2RedirectParams),
            ),
            cast_to=URLAPIResponse,
        )


class Oauth2ResourceWithRawResponse:
    def __init__(self, oauth2: Oauth2Resource) -> None:
        self._oauth2 = oauth2

        self.callback = to_raw_response_wrapper(
            oauth2.callback,
        )
        self.logout = to_raw_response_wrapper(
            oauth2.logout,
        )
        self.redirect = to_raw_response_wrapper(
            oauth2.redirect,
        )


class AsyncOauth2ResourceWithRawResponse:
    def __init__(self, oauth2: AsyncOauth2Resource) -> None:
        self._oauth2 = oauth2

        self.callback = async_to_raw_response_wrapper(
            oauth2.callback,
        )
        self.logout = async_to_raw_response_wrapper(
            oauth2.logout,
        )
        self.redirect = async_to_raw_response_wrapper(
            oauth2.redirect,
        )


class Oauth2ResourceWithStreamingResponse:
    def __init__(self, oauth2: Oauth2Resource) -> None:
        self._oauth2 = oauth2

        self.callback = to_streamed_response_wrapper(
            oauth2.callback,
        )
        self.logout = to_streamed_response_wrapper(
            oauth2.logout,
        )
        self.redirect = to_streamed_response_wrapper(
            oauth2.redirect,
        )


class AsyncOauth2ResourceWithStreamingResponse:
    def __init__(self, oauth2: AsyncOauth2Resource) -> None:
        self._oauth2 = oauth2

        self.callback = async_to_streamed_response_wrapper(
            oauth2.callback,
        )
        self.logout = async_to_streamed_response_wrapper(
            oauth2.logout,
        )
        self.redirect = async_to_streamed_response_wrapper(
            oauth2.redirect,
        )
