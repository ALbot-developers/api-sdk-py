# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from albot_api_sdk import AlbotAPISDK, AsyncAlbotAPISDK
from albot_api_sdk.types.users.me import GuildListResponse, GuildRetrieveInfoResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGuilds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: AlbotAPISDK) -> None:
        guild = client.users.me.guilds.list()
        assert_matches_type(GuildListResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: AlbotAPISDK) -> None:
        guild = client.users.me.guilds.list(
            mutual=True,
        )
        assert_matches_type(GuildListResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: AlbotAPISDK) -> None:
        response = client.users.me.guilds.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guild = response.parse()
        assert_matches_type(GuildListResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: AlbotAPISDK) -> None:
        with client.users.me.guilds.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guild = response.parse()
            assert_matches_type(GuildListResponse, guild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_info(self, client: AlbotAPISDK) -> None:
        guild = client.users.me.guilds.retrieve_info(
            0,
        )
        assert_matches_type(GuildRetrieveInfoResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_info(self, client: AlbotAPISDK) -> None:
        response = client.users.me.guilds.with_raw_response.retrieve_info(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guild = response.parse()
        assert_matches_type(GuildRetrieveInfoResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_info(self, client: AlbotAPISDK) -> None:
        with client.users.me.guilds.with_streaming_response.retrieve_info(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guild = response.parse()
            assert_matches_type(GuildRetrieveInfoResponse, guild, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGuilds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAlbotAPISDK) -> None:
        guild = await async_client.users.me.guilds.list()
        assert_matches_type(GuildListResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAlbotAPISDK) -> None:
        guild = await async_client.users.me.guilds.list(
            mutual=True,
        )
        assert_matches_type(GuildListResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.users.me.guilds.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guild = await response.parse()
        assert_matches_type(GuildListResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.users.me.guilds.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guild = await response.parse()
            assert_matches_type(GuildListResponse, guild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_info(self, async_client: AsyncAlbotAPISDK) -> None:
        guild = await async_client.users.me.guilds.retrieve_info(
            0,
        )
        assert_matches_type(GuildRetrieveInfoResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_info(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.users.me.guilds.with_raw_response.retrieve_info(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guild = await response.parse()
        assert_matches_type(GuildRetrieveInfoResponse, guild, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_info(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.users.me.guilds.with_streaming_response.retrieve_info(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guild = await response.parse()
            assert_matches_type(GuildRetrieveInfoResponse, guild, path=["response"])

        assert cast(Any, response.is_closed) is True
