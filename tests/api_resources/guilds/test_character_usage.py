# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from albot_api_sdk import AlbotAPISDK, AsyncAlbotAPISDK
from albot_api_sdk.types import PlainAPIResponse
from albot_api_sdk.types.guilds import CharacterUsageRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCharacterUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: AlbotAPISDK) -> None:
        character_usage = client.guilds.character_usage.retrieve(
            0,
        )
        assert_matches_type(CharacterUsageRetrieveResponse, character_usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: AlbotAPISDK) -> None:
        response = client.guilds.character_usage.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character_usage = response.parse()
        assert_matches_type(CharacterUsageRetrieveResponse, character_usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: AlbotAPISDK) -> None:
        with client.guilds.character_usage.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character_usage = response.parse()
            assert_matches_type(CharacterUsageRetrieveResponse, character_usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: AlbotAPISDK) -> None:
        character_usage = client.guilds.character_usage.update(
            guild_id=0,
        )
        assert_matches_type(PlainAPIResponse, character_usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: AlbotAPISDK) -> None:
        character_usage = client.guilds.character_usage.update(
            guild_id=0,
            standard={
                "used_characters": 0,
                "monthly_quota": 0,
            },
            wavenet={
                "used_characters": 0,
                "monthly_quota": 0,
            },
        )
        assert_matches_type(PlainAPIResponse, character_usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: AlbotAPISDK) -> None:
        response = client.guilds.character_usage.with_raw_response.update(
            guild_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character_usage = response.parse()
        assert_matches_type(PlainAPIResponse, character_usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: AlbotAPISDK) -> None:
        with client.guilds.character_usage.with_streaming_response.update(
            guild_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character_usage = response.parse()
            assert_matches_type(PlainAPIResponse, character_usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCharacterUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAlbotAPISDK) -> None:
        character_usage = await async_client.guilds.character_usage.retrieve(
            0,
        )
        assert_matches_type(CharacterUsageRetrieveResponse, character_usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.character_usage.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character_usage = await response.parse()
        assert_matches_type(CharacterUsageRetrieveResponse, character_usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.character_usage.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character_usage = await response.parse()
            assert_matches_type(CharacterUsageRetrieveResponse, character_usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncAlbotAPISDK) -> None:
        character_usage = await async_client.guilds.character_usage.update(
            guild_id=0,
        )
        assert_matches_type(PlainAPIResponse, character_usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAlbotAPISDK) -> None:
        character_usage = await async_client.guilds.character_usage.update(
            guild_id=0,
            standard={
                "used_characters": 0,
                "monthly_quota": 0,
            },
            wavenet={
                "used_characters": 0,
                "monthly_quota": 0,
            },
        )
        assert_matches_type(PlainAPIResponse, character_usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.character_usage.with_raw_response.update(
            guild_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        character_usage = await response.parse()
        assert_matches_type(PlainAPIResponse, character_usage, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.character_usage.with_streaming_response.update(
            guild_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            character_usage = await response.parse()
            assert_matches_type(PlainAPIResponse, character_usage, path=["response"])

        assert cast(Any, response.is_closed) is True
