# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from albot_api_sdk import AlbotAPISDK, AsyncAlbotAPISDK
from albot_api_sdk.types import URLAPIResponse
from albot_api_sdk.types.users import MeRetrieveInfoResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_checkout_session(self, client: AlbotAPISDK) -> None:
        me = client.users.me.create_checkout_session(
            plan="plan",
        )
        assert_matches_type(URLAPIResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_checkout_session(self, client: AlbotAPISDK) -> None:
        response = client.users.me.with_raw_response.create_checkout_session(
            plan="plan",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = response.parse()
        assert_matches_type(URLAPIResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_checkout_session(self, client: AlbotAPISDK) -> None:
        with client.users.me.with_streaming_response.create_checkout_session(
            plan="plan",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = response.parse()
            assert_matches_type(URLAPIResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_info(self, client: AlbotAPISDK) -> None:
        me = client.users.me.retrieve_info()
        assert_matches_type(MeRetrieveInfoResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_info(self, client: AlbotAPISDK) -> None:
        response = client.users.me.with_raw_response.retrieve_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = response.parse()
        assert_matches_type(MeRetrieveInfoResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_info(self, client: AlbotAPISDK) -> None:
        with client.users.me.with_streaming_response.retrieve_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = response.parse()
            assert_matches_type(MeRetrieveInfoResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMe:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_checkout_session(self, async_client: AsyncAlbotAPISDK) -> None:
        me = await async_client.users.me.create_checkout_session(
            plan="plan",
        )
        assert_matches_type(URLAPIResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_checkout_session(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.users.me.with_raw_response.create_checkout_session(
            plan="plan",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = await response.parse()
        assert_matches_type(URLAPIResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_checkout_session(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.users.me.with_streaming_response.create_checkout_session(
            plan="plan",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = await response.parse()
            assert_matches_type(URLAPIResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_info(self, async_client: AsyncAlbotAPISDK) -> None:
        me = await async_client.users.me.retrieve_info()
        assert_matches_type(MeRetrieveInfoResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_info(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.users.me.with_raw_response.retrieve_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        me = await response.parse()
        assert_matches_type(MeRetrieveInfoResponse, me, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_info(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.users.me.with_streaming_response.retrieve_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            me = await response.parse()
            assert_matches_type(MeRetrieveInfoResponse, me, path=["response"])

        assert cast(Any, response.is_closed) is True
