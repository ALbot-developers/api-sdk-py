# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .dict import (
    DictResource,
    AsyncDictResource,
    DictResourceWithRawResponse,
    AsyncDictResourceWithRawResponse,
    DictResourceWithStreamingResponse,
    AsyncDictResourceWithStreamingResponse,
)
from ...types import guild_create_quick_report_params, guild_create_connection_states_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .trusted_roles import (
    TrustedRolesResource,
    AsyncTrustedRolesResource,
    TrustedRolesResourceWithRawResponse,
    AsyncTrustedRolesResourceWithRawResponse,
    TrustedRolesResourceWithStreamingResponse,
    AsyncTrustedRolesResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .character_usage import (
    CharacterUsageResource,
    AsyncCharacterUsageResource,
    CharacterUsageResourceWithRawResponse,
    AsyncCharacterUsageResourceWithRawResponse,
    CharacterUsageResourceWithStreamingResponse,
    AsyncCharacterUsageResourceWithStreamingResponse,
)
from .connection_command import (
    ConnectionCommandResource,
    AsyncConnectionCommandResource,
    ConnectionCommandResourceWithRawResponse,
    AsyncConnectionCommandResourceWithRawResponse,
    ConnectionCommandResourceWithStreamingResponse,
    AsyncConnectionCommandResourceWithStreamingResponse,
)
from ...types.list_subscriptions import ListSubscriptions
from ...types.plain_api_response import PlainAPIResponse
from .message_link_expand_preference import (
    MessageLinkExpandPreferenceResource,
    AsyncMessageLinkExpandPreferenceResource,
    MessageLinkExpandPreferenceResourceWithRawResponse,
    AsyncMessageLinkExpandPreferenceResourceWithRawResponse,
    MessageLinkExpandPreferenceResourceWithStreamingResponse,
    AsyncMessageLinkExpandPreferenceResourceWithStreamingResponse,
)
from ...types.guild_create_connection_states_response import GuildCreateConnectionStatesResponse

__all__ = ["GuildsResource", "AsyncGuildsResource"]


class GuildsResource(SyncAPIResource):
    @cached_property
    def dict(self) -> DictResource:
        return DictResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def character_usage(self) -> CharacterUsageResource:
        return CharacterUsageResource(self._client)

    @cached_property
    def trusted_roles(self) -> TrustedRolesResource:
        return TrustedRolesResource(self._client)

    @cached_property
    def connection_command(self) -> ConnectionCommandResource:
        return ConnectionCommandResource(self._client)

    @cached_property
    def message_link_expand_preference(self) -> MessageLinkExpandPreferenceResource:
        return MessageLinkExpandPreferenceResource(self._client)

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

    def create(
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
        Create Guild Resources

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/guilds/{guild_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
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
        Delete Guild Resources

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/guilds/{guild_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )

    def create_connection_states(
        self,
        guild_id: int,
        *,
        tc_id: int,
        vc_id: int,
        character_limit: Optional[int] | Omit = omit,
        lang: Optional[str] | Omit = omit,
        read_guild: Optional[bool] | Omit = omit,
        read_name: Optional[bool] | Omit = omit,
        speech_speed: Optional[float] | Omit = omit,
        translate: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GuildCreateConnectionStatesResponse:
        """
        Create Connection States Api

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/guilds/{guild_id}/connection_states",
            body=maybe_transform(
                {
                    "tc_id": tc_id,
                    "vc_id": vc_id,
                    "character_limit": character_limit,
                    "lang": lang,
                    "read_guild": read_guild,
                    "read_name": read_name,
                    "speech_speed": speech_speed,
                    "translate": translate,
                },
                guild_create_connection_states_params.GuildCreateConnectionStatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GuildCreateConnectionStatesResponse,
        )

    def create_quick_report(
        self,
        guild_id: int,
        *,
        category: str,
        description: str,
        turnstile_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Post Quick Report

        Args:
          turnstile_token: Cloudflare Turnstile token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"turnstile-token": turnstile_token, **(extra_headers or {})}
        return self._post(
            f"/guilds/{guild_id}/quick_reports",
            body=maybe_transform(
                {
                    "category": category,
                    "description": description,
                },
                guild_create_quick_report_params.GuildCreateQuickReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )

    def list_subscriptions(
        self,
        guild_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListSubscriptions:
        """
        List Guild Subscriptions Api

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/guilds/{guild_id}/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListSubscriptions,
        )


class AsyncGuildsResource(AsyncAPIResource):
    @cached_property
    def dict(self) -> AsyncDictResource:
        return AsyncDictResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def character_usage(self) -> AsyncCharacterUsageResource:
        return AsyncCharacterUsageResource(self._client)

    @cached_property
    def trusted_roles(self) -> AsyncTrustedRolesResource:
        return AsyncTrustedRolesResource(self._client)

    @cached_property
    def connection_command(self) -> AsyncConnectionCommandResource:
        return AsyncConnectionCommandResource(self._client)

    @cached_property
    def message_link_expand_preference(self) -> AsyncMessageLinkExpandPreferenceResource:
        return AsyncMessageLinkExpandPreferenceResource(self._client)

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

    async def create(
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
        Create Guild Resources

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/guilds/{guild_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
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
        Delete Guild Resources

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/guilds/{guild_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )

    async def create_connection_states(
        self,
        guild_id: int,
        *,
        tc_id: int,
        vc_id: int,
        character_limit: Optional[int] | Omit = omit,
        lang: Optional[str] | Omit = omit,
        read_guild: Optional[bool] | Omit = omit,
        read_name: Optional[bool] | Omit = omit,
        speech_speed: Optional[float] | Omit = omit,
        translate: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GuildCreateConnectionStatesResponse:
        """
        Create Connection States Api

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/guilds/{guild_id}/connection_states",
            body=await async_maybe_transform(
                {
                    "tc_id": tc_id,
                    "vc_id": vc_id,
                    "character_limit": character_limit,
                    "lang": lang,
                    "read_guild": read_guild,
                    "read_name": read_name,
                    "speech_speed": speech_speed,
                    "translate": translate,
                },
                guild_create_connection_states_params.GuildCreateConnectionStatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GuildCreateConnectionStatesResponse,
        )

    async def create_quick_report(
        self,
        guild_id: int,
        *,
        category: str,
        description: str,
        turnstile_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Post Quick Report

        Args:
          turnstile_token: Cloudflare Turnstile token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"turnstile-token": turnstile_token, **(extra_headers or {})}
        return await self._post(
            f"/guilds/{guild_id}/quick_reports",
            body=await async_maybe_transform(
                {
                    "category": category,
                    "description": description,
                },
                guild_create_quick_report_params.GuildCreateQuickReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )

    async def list_subscriptions(
        self,
        guild_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListSubscriptions:
        """
        List Guild Subscriptions Api

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/guilds/{guild_id}/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListSubscriptions,
        )


class GuildsResourceWithRawResponse:
    def __init__(self, guilds: GuildsResource) -> None:
        self._guilds = guilds

        self.create = to_raw_response_wrapper(
            guilds.create,
        )
        self.delete = to_raw_response_wrapper(
            guilds.delete,
        )
        self.create_connection_states = to_raw_response_wrapper(
            guilds.create_connection_states,
        )
        self.create_quick_report = to_raw_response_wrapper(
            guilds.create_quick_report,
        )
        self.list_subscriptions = to_raw_response_wrapper(
            guilds.list_subscriptions,
        )

    @cached_property
    def dict(self) -> DictResourceWithRawResponse:
        return DictResourceWithRawResponse(self._guilds.dict)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._guilds.settings)

    @cached_property
    def character_usage(self) -> CharacterUsageResourceWithRawResponse:
        return CharacterUsageResourceWithRawResponse(self._guilds.character_usage)

    @cached_property
    def trusted_roles(self) -> TrustedRolesResourceWithRawResponse:
        return TrustedRolesResourceWithRawResponse(self._guilds.trusted_roles)

    @cached_property
    def connection_command(self) -> ConnectionCommandResourceWithRawResponse:
        return ConnectionCommandResourceWithRawResponse(self._guilds.connection_command)

    @cached_property
    def message_link_expand_preference(self) -> MessageLinkExpandPreferenceResourceWithRawResponse:
        return MessageLinkExpandPreferenceResourceWithRawResponse(self._guilds.message_link_expand_preference)


class AsyncGuildsResourceWithRawResponse:
    def __init__(self, guilds: AsyncGuildsResource) -> None:
        self._guilds = guilds

        self.create = async_to_raw_response_wrapper(
            guilds.create,
        )
        self.delete = async_to_raw_response_wrapper(
            guilds.delete,
        )
        self.create_connection_states = async_to_raw_response_wrapper(
            guilds.create_connection_states,
        )
        self.create_quick_report = async_to_raw_response_wrapper(
            guilds.create_quick_report,
        )
        self.list_subscriptions = async_to_raw_response_wrapper(
            guilds.list_subscriptions,
        )

    @cached_property
    def dict(self) -> AsyncDictResourceWithRawResponse:
        return AsyncDictResourceWithRawResponse(self._guilds.dict)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._guilds.settings)

    @cached_property
    def character_usage(self) -> AsyncCharacterUsageResourceWithRawResponse:
        return AsyncCharacterUsageResourceWithRawResponse(self._guilds.character_usage)

    @cached_property
    def trusted_roles(self) -> AsyncTrustedRolesResourceWithRawResponse:
        return AsyncTrustedRolesResourceWithRawResponse(self._guilds.trusted_roles)

    @cached_property
    def connection_command(self) -> AsyncConnectionCommandResourceWithRawResponse:
        return AsyncConnectionCommandResourceWithRawResponse(self._guilds.connection_command)

    @cached_property
    def message_link_expand_preference(self) -> AsyncMessageLinkExpandPreferenceResourceWithRawResponse:
        return AsyncMessageLinkExpandPreferenceResourceWithRawResponse(self._guilds.message_link_expand_preference)


class GuildsResourceWithStreamingResponse:
    def __init__(self, guilds: GuildsResource) -> None:
        self._guilds = guilds

        self.create = to_streamed_response_wrapper(
            guilds.create,
        )
        self.delete = to_streamed_response_wrapper(
            guilds.delete,
        )
        self.create_connection_states = to_streamed_response_wrapper(
            guilds.create_connection_states,
        )
        self.create_quick_report = to_streamed_response_wrapper(
            guilds.create_quick_report,
        )
        self.list_subscriptions = to_streamed_response_wrapper(
            guilds.list_subscriptions,
        )

    @cached_property
    def dict(self) -> DictResourceWithStreamingResponse:
        return DictResourceWithStreamingResponse(self._guilds.dict)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._guilds.settings)

    @cached_property
    def character_usage(self) -> CharacterUsageResourceWithStreamingResponse:
        return CharacterUsageResourceWithStreamingResponse(self._guilds.character_usage)

    @cached_property
    def trusted_roles(self) -> TrustedRolesResourceWithStreamingResponse:
        return TrustedRolesResourceWithStreamingResponse(self._guilds.trusted_roles)

    @cached_property
    def connection_command(self) -> ConnectionCommandResourceWithStreamingResponse:
        return ConnectionCommandResourceWithStreamingResponse(self._guilds.connection_command)

    @cached_property
    def message_link_expand_preference(self) -> MessageLinkExpandPreferenceResourceWithStreamingResponse:
        return MessageLinkExpandPreferenceResourceWithStreamingResponse(self._guilds.message_link_expand_preference)


class AsyncGuildsResourceWithStreamingResponse:
    def __init__(self, guilds: AsyncGuildsResource) -> None:
        self._guilds = guilds

        self.create = async_to_streamed_response_wrapper(
            guilds.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            guilds.delete,
        )
        self.create_connection_states = async_to_streamed_response_wrapper(
            guilds.create_connection_states,
        )
        self.create_quick_report = async_to_streamed_response_wrapper(
            guilds.create_quick_report,
        )
        self.list_subscriptions = async_to_streamed_response_wrapper(
            guilds.list_subscriptions,
        )

    @cached_property
    def dict(self) -> AsyncDictResourceWithStreamingResponse:
        return AsyncDictResourceWithStreamingResponse(self._guilds.dict)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._guilds.settings)

    @cached_property
    def character_usage(self) -> AsyncCharacterUsageResourceWithStreamingResponse:
        return AsyncCharacterUsageResourceWithStreamingResponse(self._guilds.character_usage)

    @cached_property
    def trusted_roles(self) -> AsyncTrustedRolesResourceWithStreamingResponse:
        return AsyncTrustedRolesResourceWithStreamingResponse(self._guilds.trusted_roles)

    @cached_property
    def connection_command(self) -> AsyncConnectionCommandResourceWithStreamingResponse:
        return AsyncConnectionCommandResourceWithStreamingResponse(self._guilds.connection_command)

    @cached_property
    def message_link_expand_preference(self) -> AsyncMessageLinkExpandPreferenceResourceWithStreamingResponse:
        return AsyncMessageLinkExpandPreferenceResourceWithStreamingResponse(
            self._guilds.message_link_expand_preference
        )
