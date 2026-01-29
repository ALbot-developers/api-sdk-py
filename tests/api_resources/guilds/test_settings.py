# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from albot_api_sdk import AlbotAPISDK, AsyncAlbotAPISDK
from albot_api_sdk.types import PlainAPIResponse
from albot_api_sdk.types.guilds import SettingRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: AlbotAPISDK) -> None:
        setting = client.guilds.settings.retrieve(
            0,
        )
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: AlbotAPISDK) -> None:
        response = client.guilds.settings.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: AlbotAPISDK) -> None:
        with client.guilds.settings.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: AlbotAPISDK) -> None:
        setting = client.guilds.settings.update(
            guild_id=0,
        )
        assert_matches_type(PlainAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: AlbotAPISDK) -> None:
        setting = client.guilds.settings.update(
            guild_id=0,
            audio_api="gtts",
            character_limit=0,
            custom_voice="se-KLZ-Wavenet-v",
            lang="lang",
            read_guild=True,
            read_name=True,
            read_name_on_join=True,
            read_name_on_leave=True,
            read_not_joined_users=True,
            speech_speed=0,
            translate=True,
        )
        assert_matches_type(PlainAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: AlbotAPISDK) -> None:
        response = client.guilds.settings.with_raw_response.update(
            guild_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(PlainAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: AlbotAPISDK) -> None:
        with client.guilds.settings.with_streaming_response.update(
            guild_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(PlainAPIResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: AlbotAPISDK) -> None:
        setting = client.guilds.settings.delete(
            0,
        )
        assert_matches_type(PlainAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: AlbotAPISDK) -> None:
        response = client.guilds.settings.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(PlainAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: AlbotAPISDK) -> None:
        with client.guilds.settings.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(PlainAPIResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAlbotAPISDK) -> None:
        setting = await async_client.guilds.settings.retrieve(
            0,
        )
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.settings.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.settings.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAlbotAPISDK) -> None:
        setting = await async_client.guilds.settings.update(
            guild_id=0,
        )
        assert_matches_type(PlainAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAlbotAPISDK) -> None:
        setting = await async_client.guilds.settings.update(
            guild_id=0,
            audio_api="gtts",
            character_limit=0,
            custom_voice="se-KLZ-Wavenet-v",
            lang="lang",
            read_guild=True,
            read_name=True,
            read_name_on_join=True,
            read_name_on_leave=True,
            read_not_joined_users=True,
            speech_speed=0,
            translate=True,
        )
        assert_matches_type(PlainAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.settings.with_raw_response.update(
            guild_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(PlainAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.settings.with_streaming_response.update(
            guild_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(PlainAPIResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAlbotAPISDK) -> None:
        setting = await async_client.guilds.settings.delete(
            0,
        )
        assert_matches_type(PlainAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.settings.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(PlainAPIResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.settings.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(PlainAPIResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True
