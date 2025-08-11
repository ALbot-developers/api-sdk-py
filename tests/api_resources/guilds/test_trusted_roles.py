# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from albot_api_sdk import AlbotAPISDK, AsyncAlbotAPISDK
from albot_api_sdk.types import PlainAPIResponse
from albot_api_sdk.types.guilds import TrustedRoleListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrustedRoles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: AlbotAPISDK) -> None:
        trusted_role = client.guilds.trusted_roles.update(
            guild_id=0,
        )
        assert_matches_type(PlainAPIResponse, trusted_role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: AlbotAPISDK) -> None:
        trusted_role = client.guilds.trusted_roles.update(
            guild_id=0,
            enabled=True,
            role_ids=[0],
        )
        assert_matches_type(PlainAPIResponse, trusted_role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: AlbotAPISDK) -> None:
        response = client.guilds.trusted_roles.with_raw_response.update(
            guild_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_role = response.parse()
        assert_matches_type(PlainAPIResponse, trusted_role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: AlbotAPISDK) -> None:
        with client.guilds.trusted_roles.with_streaming_response.update(
            guild_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_role = response.parse()
            assert_matches_type(PlainAPIResponse, trusted_role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: AlbotAPISDK) -> None:
        trusted_role = client.guilds.trusted_roles.list(
            0,
        )
        assert_matches_type(TrustedRoleListResponse, trusted_role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: AlbotAPISDK) -> None:
        response = client.guilds.trusted_roles.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_role = response.parse()
        assert_matches_type(TrustedRoleListResponse, trusted_role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: AlbotAPISDK) -> None:
        with client.guilds.trusted_roles.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_role = response.parse()
            assert_matches_type(TrustedRoleListResponse, trusted_role, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTrustedRoles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncAlbotAPISDK) -> None:
        trusted_role = await async_client.guilds.trusted_roles.update(
            guild_id=0,
        )
        assert_matches_type(PlainAPIResponse, trusted_role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncAlbotAPISDK) -> None:
        trusted_role = await async_client.guilds.trusted_roles.update(
            guild_id=0,
            enabled=True,
            role_ids=[0],
        )
        assert_matches_type(PlainAPIResponse, trusted_role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.trusted_roles.with_raw_response.update(
            guild_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_role = await response.parse()
        assert_matches_type(PlainAPIResponse, trusted_role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.trusted_roles.with_streaming_response.update(
            guild_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_role = await response.parse()
            assert_matches_type(PlainAPIResponse, trusted_role, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncAlbotAPISDK) -> None:
        trusted_role = await async_client.guilds.trusted_roles.list(
            0,
        )
        assert_matches_type(TrustedRoleListResponse, trusted_role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.guilds.trusted_roles.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trusted_role = await response.parse()
        assert_matches_type(TrustedRoleListResponse, trusted_role, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.guilds.trusted_roles.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trusted_role = await response.parse()
            assert_matches_type(TrustedRoleListResponse, trusted_role, path=["response"])

        assert cast(Any, response.is_closed) is True
