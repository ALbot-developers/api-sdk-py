# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from albot_api_sdk import AlbotAPISDK, AsyncAlbotAPISDK
from albot_api_sdk.types import (
    PlainAPIResponse,
    ListSubscriptions,
    GuildCreateConnectionStatesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGuilds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: AlbotAPISDK) -> None:
        guild = client.guilds.create(
            0,
        )
        assert_matches_type(PlainAPIResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: AlbotAPISDK) -> None:
        response = client.guilds.with_raw_response.create(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guild = response.parse()
        assert_matches_type(PlainAPIResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: AlbotAPISDK) -> None:
        with client.guilds.with_streaming_response.create(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guild = response.parse()
            assert_matches_type(PlainAPIResponse, guild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: AlbotAPISDK) -> None:
        guild = client.guilds.delete(
            0,
        )
        assert_matches_type(PlainAPIResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: AlbotAPISDK) -> None:
        response = client.guilds.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guild = response.parse()
        assert_matches_type(PlainAPIResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: AlbotAPISDK) -> None:
        with client.guilds.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guild = response.parse()
            assert_matches_type(PlainAPIResponse, guild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_connection_states(self, client: AlbotAPISDK) -> None:
        guild = client.guilds.create_connection_states(
            guild_id=0,
            tc_id=0,
            vc_id=0,
        )
        assert_matches_type(GuildCreateConnectionStatesResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_connection_states_with_all_params(self, client: AlbotAPISDK) -> None:
        guild = client.guilds.create_connection_states(
            guild_id=0,
            tc_id=0,
            vc_id=0,
            character_limit=0,
            custom_voice="custom_voice",
            lang="lang",
            read_guild=True,
            read_name=True,
            speech_speed=0,
            translate=True,
        )
        assert_matches_type(GuildCreateConnectionStatesResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_connection_states(self, client: AlbotAPISDK) -> None:
        response = client.guilds.with_raw_response.create_connection_states(
            guild_id=0,
            tc_id=0,
            vc_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guild = response.parse()
        assert_matches_type(GuildCreateConnectionStatesResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_connection_states(self, client: AlbotAPISDK) -> None:
        with client.guilds.with_streaming_response.create_connection_states(
            guild_id=0,
            tc_id=0,
            vc_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guild = response.parse()
            assert_matches_type(GuildCreateConnectionStatesResponse, guild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_quick_report(self, client: AlbotAPISDK) -> None:
        guild = client.guilds.create_quick_report(
            guild_id=0,
            category="category",
            description="description",
            turnstile_token="turnstile-token",
        )
        assert_matches_type(PlainAPIResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_quick_report(self, client: AlbotAPISDK) -> None:
        response = client.guilds.with_raw_response.create_quick_report(
            guild_id=0,
            category="category",
            description="description",
            turnstile_token="turnstile-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guild = response.parse()
        assert_matches_type(PlainAPIResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_quick_report(self, client: AlbotAPISDK) -> None:
        with client.guilds.with_streaming_response.create_quick_report(
            guild_id=0,
            category="category",
            description="description",
            turnstile_token="turnstile-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guild = response.parse()
            assert_matches_type(PlainAPIResponse, guild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_subscriptions(self, client: AlbotAPISDK) -> None:
        guild = client.guilds.list_subscriptions(
            0,
        )
        assert_matches_type(ListSubscriptions, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_subscriptions(self, client: AlbotAPISDK) -> None:
        response = client.guilds.with_raw_response.list_subscriptions(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guild = response.parse()
        assert_matches_type(ListSubscriptions, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_subscriptions(self, client: AlbotAPISDK) -> None:
        with client.guilds.with_streaming_response.list_subscriptions(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guild = response.parse()
            assert_matches_type(ListSubscriptions, guild, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGuilds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAlbotAPISDK) -> None:
        guild = await async_client.guilds.create(
            0,
        )
        assert_matches_type(PlainAPIResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.with_raw_response.create(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guild = await response.parse()
        assert_matches_type(PlainAPIResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.with_streaming_response.create(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guild = await response.parse()
            assert_matches_type(PlainAPIResponse, guild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAlbotAPISDK) -> None:
        guild = await async_client.guilds.delete(
            0,
        )
        assert_matches_type(PlainAPIResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guild = await response.parse()
        assert_matches_type(PlainAPIResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guild = await response.parse()
            assert_matches_type(PlainAPIResponse, guild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_connection_states(self, async_client: AsyncAlbotAPISDK) -> None:
        guild = await async_client.guilds.create_connection_states(
            guild_id=0,
            tc_id=0,
            vc_id=0,
        )
        assert_matches_type(GuildCreateConnectionStatesResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_connection_states_with_all_params(self, async_client: AsyncAlbotAPISDK) -> None:
        guild = await async_client.guilds.create_connection_states(
            guild_id=0,
            tc_id=0,
            vc_id=0,
            character_limit=0,
            custom_voice="custom_voice",
            lang="lang",
            read_guild=True,
            read_name=True,
            speech_speed=0,
            translate=True,
        )
        assert_matches_type(GuildCreateConnectionStatesResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_connection_states(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.with_raw_response.create_connection_states(
            guild_id=0,
            tc_id=0,
            vc_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guild = await response.parse()
        assert_matches_type(GuildCreateConnectionStatesResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_connection_states(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.with_streaming_response.create_connection_states(
            guild_id=0,
            tc_id=0,
            vc_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guild = await response.parse()
            assert_matches_type(GuildCreateConnectionStatesResponse, guild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_quick_report(self, async_client: AsyncAlbotAPISDK) -> None:
        guild = await async_client.guilds.create_quick_report(
            guild_id=0,
            category="category",
            description="description",
            turnstile_token="turnstile-token",
        )
        assert_matches_type(PlainAPIResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_quick_report(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.with_raw_response.create_quick_report(
            guild_id=0,
            category="category",
            description="description",
            turnstile_token="turnstile-token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guild = await response.parse()
        assert_matches_type(PlainAPIResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_quick_report(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.with_streaming_response.create_quick_report(
            guild_id=0,
            category="category",
            description="description",
            turnstile_token="turnstile-token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guild = await response.parse()
            assert_matches_type(PlainAPIResponse, guild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_subscriptions(self, async_client: AsyncAlbotAPISDK) -> None:
        guild = await async_client.guilds.list_subscriptions(
            0,
        )
        assert_matches_type(ListSubscriptions, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_subscriptions(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.with_raw_response.list_subscriptions(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guild = await response.parse()
        assert_matches_type(ListSubscriptions, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_subscriptions(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.with_streaming_response.list_subscriptions(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guild = await response.parse()
            assert_matches_type(ListSubscriptions, guild, path=["response"])

        assert cast(Any, response.is_closed) is True
