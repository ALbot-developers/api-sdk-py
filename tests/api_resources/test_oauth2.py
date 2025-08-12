# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from albot_api_sdk import AlbotAPISDK, AsyncAlbotAPISDK
from albot_api_sdk.types import URLAPIResponse, PlainAPIResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOauth2:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_callback(self, client: AlbotAPISDK) -> None:
        oauth2 = client.oauth2.callback(
            code="code",
            state="state",
        )
        assert_matches_type(PlainAPIResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_callback(self, client: AlbotAPISDK) -> None:
        response = client.oauth2.with_raw_response.callback(
            code="code",
            state="state",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = response.parse()
        assert_matches_type(PlainAPIResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_callback(self, client: AlbotAPISDK) -> None:
        with client.oauth2.with_streaming_response.callback(
            code="code",
            state="state",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = response.parse()
            assert_matches_type(PlainAPIResponse, oauth2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_logout(self, client: AlbotAPISDK) -> None:
        oauth2 = client.oauth2.logout()
        assert_matches_type(PlainAPIResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_logout(self, client: AlbotAPISDK) -> None:
        response = client.oauth2.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = response.parse()
        assert_matches_type(PlainAPIResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_logout(self, client: AlbotAPISDK) -> None:
        with client.oauth2.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = response.parse()
            assert_matches_type(PlainAPIResponse, oauth2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_redirect(self, client: AlbotAPISDK) -> None:
        oauth2 = client.oauth2.redirect(
            redirect="redirect",
        )
        assert_matches_type(URLAPIResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_redirect(self, client: AlbotAPISDK) -> None:
        response = client.oauth2.with_raw_response.redirect(
            redirect="redirect",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = response.parse()
        assert_matches_type(URLAPIResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_redirect(self, client: AlbotAPISDK) -> None:
        with client.oauth2.with_streaming_response.redirect(
            redirect="redirect",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = response.parse()
            assert_matches_type(URLAPIResponse, oauth2, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOauth2:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_callback(self, async_client: AsyncAlbotAPISDK) -> None:
        oauth2 = await async_client.oauth2.callback(
            code="code",
            state="state",
        )
        assert_matches_type(PlainAPIResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_callback(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.oauth2.with_raw_response.callback(
            code="code",
            state="state",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = await response.parse()
        assert_matches_type(PlainAPIResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_callback(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.oauth2.with_streaming_response.callback(
            code="code",
            state="state",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = await response.parse()
            assert_matches_type(PlainAPIResponse, oauth2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_logout(self, async_client: AsyncAlbotAPISDK) -> None:
        oauth2 = await async_client.oauth2.logout()
        assert_matches_type(PlainAPIResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_logout(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.oauth2.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = await response.parse()
        assert_matches_type(PlainAPIResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_logout(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.oauth2.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = await response.parse()
            assert_matches_type(PlainAPIResponse, oauth2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_redirect(self, async_client: AsyncAlbotAPISDK) -> None:
        oauth2 = await async_client.oauth2.redirect(
            redirect="redirect",
        )
        assert_matches_type(URLAPIResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_redirect(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.oauth2.with_raw_response.redirect(
            redirect="redirect",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth2 = await response.parse()
        assert_matches_type(URLAPIResponse, oauth2, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_redirect(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.oauth2.with_streaming_response.redirect(
            redirect="redirect",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth2 = await response.parse()
            assert_matches_type(URLAPIResponse, oauth2, path=["response"])

        assert cast(Any, response.is_closed) is True
