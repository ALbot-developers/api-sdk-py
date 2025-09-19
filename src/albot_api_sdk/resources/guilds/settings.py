# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.guilds import setting_update_params
from ...types.plain_api_response import PlainAPIResponse
from ...types.guilds.setting_retrieve_response import SettingRetrieveResponse

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)

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
    ) -> SettingRetrieveResponse:
        """
        Get Guild Settings Api

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/guilds/{guild_id}/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingRetrieveResponse,
        )

    def update(
        self,
        guild_id: int,
        *,
        audio_api: Optional[Literal["gtts", "openai"]] | Omit = omit,
        character_limit: Optional[int] | Omit = omit,
        custom_voice: Optional[str] | Omit = omit,
        lang: Optional[str] | Omit = omit,
        read_guild: Optional[bool] | Omit = omit,
        read_name: Optional[bool] | Omit = omit,
        read_name_on_join: Optional[bool] | Omit = omit,
        read_name_on_leave: Optional[bool] | Omit = omit,
        read_not_joined_users: Optional[bool] | Omit = omit,
        speech_speed: Optional[float] | Omit = omit,
        translate: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Update Guild Settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/guilds/{guild_id}/settings",
            body=maybe_transform(
                {
                    "audio_api": audio_api,
                    "character_limit": character_limit,
                    "custom_voice": custom_voice,
                    "lang": lang,
                    "read_guild": read_guild,
                    "read_name": read_name,
                    "read_name_on_join": read_name_on_join,
                    "read_name_on_leave": read_name_on_leave,
                    "read_not_joined_users": read_not_joined_users,
                    "speech_speed": speech_speed,
                    "translate": translate,
                },
                setting_update_params.SettingUpdateParams,
            ),
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
        Delete Guild Settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/guilds/{guild_id}/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ALbot-developers/api-sdk-py#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)

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
    ) -> SettingRetrieveResponse:
        """
        Get Guild Settings Api

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/guilds/{guild_id}/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingRetrieveResponse,
        )

    async def update(
        self,
        guild_id: int,
        *,
        audio_api: Optional[Literal["gtts", "openai"]] | Omit = omit,
        character_limit: Optional[int] | Omit = omit,
        custom_voice: Optional[str] | Omit = omit,
        lang: Optional[str] | Omit = omit,
        read_guild: Optional[bool] | Omit = omit,
        read_name: Optional[bool] | Omit = omit,
        read_name_on_join: Optional[bool] | Omit = omit,
        read_name_on_leave: Optional[bool] | Omit = omit,
        read_not_joined_users: Optional[bool] | Omit = omit,
        speech_speed: Optional[float] | Omit = omit,
        translate: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlainAPIResponse:
        """
        Update Guild Settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/guilds/{guild_id}/settings",
            body=await async_maybe_transform(
                {
                    "audio_api": audio_api,
                    "character_limit": character_limit,
                    "custom_voice": custom_voice,
                    "lang": lang,
                    "read_guild": read_guild,
                    "read_name": read_name,
                    "read_name_on_join": read_name_on_join,
                    "read_name_on_leave": read_name_on_leave,
                    "read_not_joined_users": read_not_joined_users,
                    "speech_speed": speech_speed,
                    "translate": translate,
                },
                setting_update_params.SettingUpdateParams,
            ),
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
        Delete Guild Settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/guilds/{guild_id}/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlainAPIResponse,
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.retrieve = to_raw_response_wrapper(
            settings.retrieve,
        )
        self.update = to_raw_response_wrapper(
            settings.update,
        )
        self.delete = to_raw_response_wrapper(
            settings.delete,
        )


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.retrieve = async_to_raw_response_wrapper(
            settings.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            settings.update,
        )
        self.delete = async_to_raw_response_wrapper(
            settings.delete,
        )


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.retrieve = to_streamed_response_wrapper(
            settings.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            settings.update,
        )
        self.delete = to_streamed_response_wrapper(
            settings.delete,
        )


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.retrieve = async_to_streamed_response_wrapper(
            settings.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            settings.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            settings.delete,
        )
