# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from albot_api_sdk import AlbotAPISDK, AsyncAlbotAPISDK
from albot_api_sdk.types import PlainAPIResponse
from albot_api_sdk.types.guilds import ConnectionCommandRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectionCommand:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: AlbotAPISDK) -> None:
        connection_command = client.guilds.connection_command.retrieve(
            0,
        )
        assert_matches_type(ConnectionCommandRetrieveResponse, connection_command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: AlbotAPISDK) -> None:
        response = client.guilds.connection_command.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_command = response.parse()
        assert_matches_type(ConnectionCommandRetrieveResponse, connection_command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: AlbotAPISDK) -> None:
        with client.guilds.connection_command.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_command = response.parse()
            assert_matches_type(ConnectionCommandRetrieveResponse, connection_command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: AlbotAPISDK) -> None:
        connection_command = client.guilds.connection_command.update(
            guild_id=0,
            command="command",
        )
        assert_matches_type(PlainAPIResponse, connection_command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: AlbotAPISDK) -> None:
        response = client.guilds.connection_command.with_raw_response.update(
            guild_id=0,
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_command = response.parse()
        assert_matches_type(PlainAPIResponse, connection_command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: AlbotAPISDK) -> None:
        with client.guilds.connection_command.with_streaming_response.update(
            guild_id=0,
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_command = response.parse()
            assert_matches_type(PlainAPIResponse, connection_command, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConnectionCommand:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAlbotAPISDK) -> None:
        connection_command = await async_client.guilds.connection_command.retrieve(
            0,
        )
        assert_matches_type(ConnectionCommandRetrieveResponse, connection_command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.connection_command.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_command = await response.parse()
        assert_matches_type(ConnectionCommandRetrieveResponse, connection_command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.connection_command.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_command = await response.parse()
            assert_matches_type(ConnectionCommandRetrieveResponse, connection_command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncAlbotAPISDK) -> None:
        connection_command = await async_client.guilds.connection_command.update(
            guild_id=0,
            command="command",
        )
        assert_matches_type(PlainAPIResponse, connection_command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.connection_command.with_raw_response.update(
            guild_id=0,
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection_command = await response.parse()
        assert_matches_type(PlainAPIResponse, connection_command, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.connection_command.with_streaming_response.update(
            guild_id=0,
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection_command = await response.parse()
            assert_matches_type(PlainAPIResponse, connection_command, path=["response"])

        assert cast(Any, response.is_closed) is True
