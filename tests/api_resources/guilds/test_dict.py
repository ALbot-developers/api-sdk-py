# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from albot_api_sdk import AlbotAPISDK, AsyncAlbotAPISDK
from albot_api_sdk.types import PlainAPIResponse
from albot_api_sdk.types.guilds import DictRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDict:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: AlbotAPISDK) -> None:
        dict_ = client.guilds.dict.retrieve(
            0,
        )
        assert_matches_type(DictRetrieveResponse, dict_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: AlbotAPISDK) -> None:
        response = client.guilds.dict.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dict_ = response.parse()
        assert_matches_type(DictRetrieveResponse, dict_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: AlbotAPISDK) -> None:
        with client.guilds.dict.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dict_ = response.parse()
            assert_matches_type(DictRetrieveResponse, dict_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: AlbotAPISDK) -> None:
        dict_ = client.guilds.dict.delete(
            0,
        )
        assert_matches_type(PlainAPIResponse, dict_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: AlbotAPISDK) -> None:
        response = client.guilds.dict.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dict_ = response.parse()
        assert_matches_type(PlainAPIResponse, dict_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: AlbotAPISDK) -> None:
        with client.guilds.dict.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dict_ = response.parse()
            assert_matches_type(PlainAPIResponse, dict_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace(self, client: AlbotAPISDK) -> None:
        dict_ = client.guilds.dict.replace(
            guild_id=0,
            dict={"foo": "bar"},
        )
        assert_matches_type(PlainAPIResponse, dict_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: AlbotAPISDK) -> None:
        response = client.guilds.dict.with_raw_response.replace(
            guild_id=0,
            dict={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dict_ = response.parse()
        assert_matches_type(PlainAPIResponse, dict_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: AlbotAPISDK) -> None:
        with client.guilds.dict.with_streaming_response.replace(
            guild_id=0,
            dict={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dict_ = response.parse()
            assert_matches_type(PlainAPIResponse, dict_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDict:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAlbotAPISDK) -> None:
        dict_ = await async_client.guilds.dict.retrieve(
            0,
        )
        assert_matches_type(DictRetrieveResponse, dict_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.dict.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dict_ = await response.parse()
        assert_matches_type(DictRetrieveResponse, dict_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.dict.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dict_ = await response.parse()
            assert_matches_type(DictRetrieveResponse, dict_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAlbotAPISDK) -> None:
        dict_ = await async_client.guilds.dict.delete(
            0,
        )
        assert_matches_type(PlainAPIResponse, dict_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.dict.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dict_ = await response.parse()
        assert_matches_type(PlainAPIResponse, dict_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.dict.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dict_ = await response.parse()
            assert_matches_type(PlainAPIResponse, dict_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncAlbotAPISDK) -> None:
        dict_ = await async_client.guilds.dict.replace(
            guild_id=0,
            dict={"foo": "bar"},
        )
        assert_matches_type(PlainAPIResponse, dict_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.dict.with_raw_response.replace(
            guild_id=0,
            dict={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dict_ = await response.parse()
        assert_matches_type(PlainAPIResponse, dict_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.dict.with_streaming_response.replace(
            guild_id=0,
            dict={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dict_ = await response.parse()
            assert_matches_type(PlainAPIResponse, dict_, path=["response"])

        assert cast(Any, response.is_closed) is True
