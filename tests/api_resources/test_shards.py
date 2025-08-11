# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from albot_api_sdk import AlbotAPISDK, AsyncAlbotAPISDK
from albot_api_sdk.types import (
    PlainAPIResponse,
    ShardListResponse,
    ShardAssignResponse,
    ShardGetConnectionCommandsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: AlbotAPISDK) -> None:
        shard = client.shards.list()
        assert_matches_type(ShardListResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: AlbotAPISDK) -> None:
        shard = client.shards.list(
            status="online",
        )
        assert_matches_type(ShardListResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: AlbotAPISDK) -> None:
        response = client.shards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shard = response.parse()
        assert_matches_type(ShardListResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: AlbotAPISDK) -> None:
        with client.shards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shard = response.parse()
            assert_matches_type(ShardListResponse, shard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_assign(self, client: AlbotAPISDK) -> None:
        shard = client.shards.assign()
        assert_matches_type(ShardAssignResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_assign(self, client: AlbotAPISDK) -> None:
        response = client.shards.with_raw_response.assign()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shard = response.parse()
        assert_matches_type(ShardAssignResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_assign(self, client: AlbotAPISDK) -> None:
        with client.shards.with_streaming_response.assign() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shard = response.parse()
            assert_matches_type(ShardAssignResponse, shard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_connection_commands(self, client: AlbotAPISDK) -> None:
        shard = client.shards.get_connection_commands(
            shard_id=0,
        )
        assert_matches_type(ShardGetConnectionCommandsResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_connection_commands_with_all_params(self, client: AlbotAPISDK) -> None:
        shard = client.shards.get_connection_commands(
            shard_id=0,
            changes_only=True,
        )
        assert_matches_type(ShardGetConnectionCommandsResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_connection_commands(self, client: AlbotAPISDK) -> None:
        response = client.shards.with_raw_response.get_connection_commands(
            shard_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shard = response.parse()
        assert_matches_type(ShardGetConnectionCommandsResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_connection_commands(self, client: AlbotAPISDK) -> None:
        with client.shards.with_streaming_response.get_connection_commands(
            shard_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shard = response.parse()
            assert_matches_type(ShardGetConnectionCommandsResponse, shard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_post_metrics(self, client: AlbotAPISDK) -> None:
        shard = client.shards.post_metrics(
            shard_id=0,
        )
        assert_matches_type(PlainAPIResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_post_metrics_with_all_params(self, client: AlbotAPISDK) -> None:
        shard = client.shards.post_metrics(
            shard_id=0,
            connected=0,
            guilds=0,
        )
        assert_matches_type(PlainAPIResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_post_metrics(self, client: AlbotAPISDK) -> None:
        response = client.shards.with_raw_response.post_metrics(
            shard_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shard = response.parse()
        assert_matches_type(PlainAPIResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_post_metrics(self, client: AlbotAPISDK) -> None:
        with client.shards.with_streaming_response.post_metrics(
            shard_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shard = response.parse()
            assert_matches_type(PlainAPIResponse, shard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_release(self, client: AlbotAPISDK) -> None:
        shard = client.shards.release(
            0,
        )
        assert_matches_type(PlainAPIResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_release(self, client: AlbotAPISDK) -> None:
        response = client.shards.with_raw_response.release(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shard = response.parse()
        assert_matches_type(PlainAPIResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_release(self, client: AlbotAPISDK) -> None:
        with client.shards.with_streaming_response.release(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shard = response.parse()
            assert_matches_type(PlainAPIResponse, shard, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncShards:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncAlbotAPISDK) -> None:
        shard = await async_client.shards.list()
        assert_matches_type(ShardListResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAlbotAPISDK) -> None:
        shard = await async_client.shards.list(
            status="online",
        )
        assert_matches_type(ShardListResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.shards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shard = await response.parse()
        assert_matches_type(ShardListResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.shards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shard = await response.parse()
            assert_matches_type(ShardListResponse, shard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_assign(self, async_client: AsyncAlbotAPISDK) -> None:
        shard = await async_client.shards.assign()
        assert_matches_type(ShardAssignResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_assign(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.shards.with_raw_response.assign()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shard = await response.parse()
        assert_matches_type(ShardAssignResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_assign(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.shards.with_streaming_response.assign() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shard = await response.parse()
            assert_matches_type(ShardAssignResponse, shard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_connection_commands(self, async_client: AsyncAlbotAPISDK) -> None:
        shard = await async_client.shards.get_connection_commands(
            shard_id=0,
        )
        assert_matches_type(ShardGetConnectionCommandsResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_connection_commands_with_all_params(self, async_client: AsyncAlbotAPISDK) -> None:
        shard = await async_client.shards.get_connection_commands(
            shard_id=0,
            changes_only=True,
        )
        assert_matches_type(ShardGetConnectionCommandsResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_connection_commands(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.shards.with_raw_response.get_connection_commands(
            shard_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shard = await response.parse()
        assert_matches_type(ShardGetConnectionCommandsResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_connection_commands(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.shards.with_streaming_response.get_connection_commands(
            shard_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shard = await response.parse()
            assert_matches_type(ShardGetConnectionCommandsResponse, shard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_post_metrics(self, async_client: AsyncAlbotAPISDK) -> None:
        shard = await async_client.shards.post_metrics(
            shard_id=0,
        )
        assert_matches_type(PlainAPIResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_post_metrics_with_all_params(self, async_client: AsyncAlbotAPISDK) -> None:
        shard = await async_client.shards.post_metrics(
            shard_id=0,
            connected=0,
            guilds=0,
        )
        assert_matches_type(PlainAPIResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_post_metrics(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.shards.with_raw_response.post_metrics(
            shard_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shard = await response.parse()
        assert_matches_type(PlainAPIResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_post_metrics(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.shards.with_streaming_response.post_metrics(
            shard_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shard = await response.parse()
            assert_matches_type(PlainAPIResponse, shard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_release(self, async_client: AsyncAlbotAPISDK) -> None:
        shard = await async_client.shards.release(
            0,
        )
        assert_matches_type(PlainAPIResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_release(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.shards.with_raw_response.release(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shard = await response.parse()
        assert_matches_type(PlainAPIResponse, shard, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_release(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.shards.with_streaming_response.release(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shard = await response.parse()
            assert_matches_type(PlainAPIResponse, shard, path=["response"])

        assert cast(Any, response.is_closed) is True
