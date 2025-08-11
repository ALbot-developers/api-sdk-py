# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

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
from ...types.guilds import trusted_role_update_params
from ...types.plain_api_response import PlainAPIResponse
from ...types.guilds.trusted_role_list_response import TrustedRoleListResponse

__all__ = ["TrustedRolesResource", "AsyncTrustedRolesResource"]


class TrustedRolesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrustedRolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/albot-api-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TrustedRolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrustedRolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/albot-api-sdk-python#with_streaming_response
        """
        return TrustedRolesResourceWithStreamingResponse(self)

    def update(
        self,
        guild_id: int,
        *,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        role_ids: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlainAPIResponse:
        """
        Update Guild Trusted Roles

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/guilds/{guild_id}/trusted_roles",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "role_ids": role_ids,
                },
                trusted_role_update_params.TrustedRoleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )

    def list(
        self,
        guild_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrustedRoleListResponse:
        """
        Get Guild Trusted Roles

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/guilds/{guild_id}/trusted_roles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrustedRoleListResponse,
        )


class AsyncTrustedRolesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrustedRolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/albot-api-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrustedRolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrustedRolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/albot-api-sdk-python#with_streaming_response
        """
        return AsyncTrustedRolesResourceWithStreamingResponse(self)

    async def update(
        self,
        guild_id: int,
        *,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        role_ids: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PlainAPIResponse:
        """
        Update Guild Trusted Roles

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/guilds/{guild_id}/trusted_roles",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "role_ids": role_ids,
                },
                trusted_role_update_params.TrustedRoleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )

    async def list(
        self,
        guild_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrustedRoleListResponse:
        """
        Get Guild Trusted Roles

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/guilds/{guild_id}/trusted_roles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrustedRoleListResponse,
        )


class TrustedRolesResourceWithRawResponse:
    def __init__(self, trusted_roles: TrustedRolesResource) -> None:
        self._trusted_roles = trusted_roles

        self.update = to_raw_response_wrapper(
            trusted_roles.update,
        )
        self.list = to_raw_response_wrapper(
            trusted_roles.list,
        )


class AsyncTrustedRolesResourceWithRawResponse:
    def __init__(self, trusted_roles: AsyncTrustedRolesResource) -> None:
        self._trusted_roles = trusted_roles

        self.update = async_to_raw_response_wrapper(
            trusted_roles.update,
        )
        self.list = async_to_raw_response_wrapper(
            trusted_roles.list,
        )


class TrustedRolesResourceWithStreamingResponse:
    def __init__(self, trusted_roles: TrustedRolesResource) -> None:
        self._trusted_roles = trusted_roles

        self.update = to_streamed_response_wrapper(
            trusted_roles.update,
        )
        self.list = to_streamed_response_wrapper(
            trusted_roles.list,
        )


class AsyncTrustedRolesResourceWithStreamingResponse:
    def __init__(self, trusted_roles: AsyncTrustedRolesResource) -> None:
        self._trusted_roles = trusted_roles

        self.update = async_to_streamed_response_wrapper(
            trusted_roles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            trusted_roles.list,
        )
