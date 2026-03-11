# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from albot_api_sdk import AlbotAPISDK, AsyncAlbotAPISDK
from albot_api_sdk.types import PlainAPIResponse
from albot_api_sdk.types.guilds import (
    MessageLinkExpandPreferenceRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessageLinkExpandPreference:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: AlbotAPISDK) -> None:
        message_link_expand_preference = client.guilds.message_link_expand_preference.retrieve(
            0,
        )
        assert_matches_type(
            MessageLinkExpandPreferenceRetrieveResponse, message_link_expand_preference, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: AlbotAPISDK) -> None:
        response = client.guilds.message_link_expand_preference.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_link_expand_preference = response.parse()
        assert_matches_type(
            MessageLinkExpandPreferenceRetrieveResponse, message_link_expand_preference, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: AlbotAPISDK) -> None:
        with client.guilds.message_link_expand_preference.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_link_expand_preference = response.parse()
            assert_matches_type(
                MessageLinkExpandPreferenceRetrieveResponse, message_link_expand_preference, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: AlbotAPISDK) -> None:
        message_link_expand_preference = client.guilds.message_link_expand_preference.update(
            guild_id=0,
            enabled=True,
        )
        assert_matches_type(PlainAPIResponse, message_link_expand_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: AlbotAPISDK) -> None:
        response = client.guilds.message_link_expand_preference.with_raw_response.update(
            guild_id=0,
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_link_expand_preference = response.parse()
        assert_matches_type(PlainAPIResponse, message_link_expand_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: AlbotAPISDK) -> None:
        with client.guilds.message_link_expand_preference.with_streaming_response.update(
            guild_id=0,
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_link_expand_preference = response.parse()
            assert_matches_type(PlainAPIResponse, message_link_expand_preference, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMessageLinkExpandPreference:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAlbotAPISDK) -> None:
        message_link_expand_preference = await async_client.guilds.message_link_expand_preference.retrieve(
            0,
        )
        assert_matches_type(
            MessageLinkExpandPreferenceRetrieveResponse, message_link_expand_preference, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.message_link_expand_preference.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_link_expand_preference = await response.parse()
        assert_matches_type(
            MessageLinkExpandPreferenceRetrieveResponse, message_link_expand_preference, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.message_link_expand_preference.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_link_expand_preference = await response.parse()
            assert_matches_type(
                MessageLinkExpandPreferenceRetrieveResponse, message_link_expand_preference, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncAlbotAPISDK) -> None:
        message_link_expand_preference = await async_client.guilds.message_link_expand_preference.update(
            guild_id=0,
            enabled=True,
        )
        assert_matches_type(PlainAPIResponse, message_link_expand_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.message_link_expand_preference.with_raw_response.update(
            guild_id=0,
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_link_expand_preference = await response.parse()
        assert_matches_type(PlainAPIResponse, message_link_expand_preference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.message_link_expand_preference.with_streaming_response.update(
            guild_id=0,
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_link_expand_preference = await response.parse()
            assert_matches_type(PlainAPIResponse, message_link_expand_preference, path=["response"])

        assert cast(Any, response.is_closed) is True
