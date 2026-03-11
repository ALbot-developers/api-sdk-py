# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from albot_api_sdk import AlbotAPISDK, AsyncAlbotAPISDK
from albot_api_sdk.types import PlainAPIResponse, ListSubscriptions

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: AlbotAPISDK) -> None:
        subscription = client.users.subscriptions.list(
            0,
        )
        assert_matches_type(ListSubscriptions, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: AlbotAPISDK) -> None:
        response = client.users.subscriptions.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(ListSubscriptions, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: AlbotAPISDK) -> None:
        with client.users.subscriptions.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(ListSubscriptions, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_activate(self, client: AlbotAPISDK) -> None:
        subscription = client.users.subscriptions.activate(
            sub_id="sub_id",
            user_id=0,
            guild_id=0,
        )
        assert_matches_type(PlainAPIResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_activate(self, client: AlbotAPISDK) -> None:
        response = client.users.subscriptions.with_raw_response.activate(
            sub_id="sub_id",
            user_id=0,
            guild_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(PlainAPIResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_activate(self, client: AlbotAPISDK) -> None:
        with client.users.subscriptions.with_streaming_response.activate(
            sub_id="sub_id",
            user_id=0,
            guild_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(PlainAPIResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_activate(self, client: AlbotAPISDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_id` but received ''"):
            client.users.subscriptions.with_raw_response.activate(
                sub_id="",
                user_id=0,
                guild_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: AlbotAPISDK) -> None:
        subscription = client.users.subscriptions.cancel(
            sub_id="sub_id",
            user_id=0,
        )
        assert_matches_type(PlainAPIResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: AlbotAPISDK) -> None:
        response = client.users.subscriptions.with_raw_response.cancel(
            sub_id="sub_id",
            user_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(PlainAPIResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: AlbotAPISDK) -> None:
        with client.users.subscriptions.with_streaming_response.cancel(
            sub_id="sub_id",
            user_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(PlainAPIResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: AlbotAPISDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_id` but received ''"):
            client.users.subscriptions.with_raw_response.cancel(
                sub_id="",
                user_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_renew(self, client: AlbotAPISDK) -> None:
        subscription = client.users.subscriptions.renew(
            sub_id="sub_id",
            user_id=0,
            new_plan="new_plan",
        )
        assert_matches_type(PlainAPIResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_renew(self, client: AlbotAPISDK) -> None:
        response = client.users.subscriptions.with_raw_response.renew(
            sub_id="sub_id",
            user_id=0,
            new_plan="new_plan",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(PlainAPIResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_renew(self, client: AlbotAPISDK) -> None:
        with client.users.subscriptions.with_streaming_response.renew(
            sub_id="sub_id",
            user_id=0,
            new_plan="new_plan",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(PlainAPIResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_renew(self, client: AlbotAPISDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_id` but received ''"):
            client.users.subscriptions.with_raw_response.renew(
                sub_id="",
                user_id=0,
                new_plan="new_plan",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAlbotAPISDK) -> None:
        subscription = await async_client.users.subscriptions.list(
            0,
        )
        assert_matches_type(ListSubscriptions, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.users.subscriptions.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(ListSubscriptions, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.users.subscriptions.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(ListSubscriptions, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_activate(self, async_client: AsyncAlbotAPISDK) -> None:
        subscription = await async_client.users.subscriptions.activate(
            sub_id="sub_id",
            user_id=0,
            guild_id=0,
        )
        assert_matches_type(PlainAPIResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_activate(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.users.subscriptions.with_raw_response.activate(
            sub_id="sub_id",
            user_id=0,
            guild_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(PlainAPIResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_activate(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.users.subscriptions.with_streaming_response.activate(
            sub_id="sub_id",
            user_id=0,
            guild_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(PlainAPIResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_activate(self, async_client: AsyncAlbotAPISDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_id` but received ''"):
            await async_client.users.subscriptions.with_raw_response.activate(
                sub_id="",
                user_id=0,
                guild_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncAlbotAPISDK) -> None:
        subscription = await async_client.users.subscriptions.cancel(
            sub_id="sub_id",
            user_id=0,
        )
        assert_matches_type(PlainAPIResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.users.subscriptions.with_raw_response.cancel(
            sub_id="sub_id",
            user_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(PlainAPIResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.users.subscriptions.with_streaming_response.cancel(
            sub_id="sub_id",
            user_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(PlainAPIResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncAlbotAPISDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_id` but received ''"):
            await async_client.users.subscriptions.with_raw_response.cancel(
                sub_id="",
                user_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_renew(self, async_client: AsyncAlbotAPISDK) -> None:
        subscription = await async_client.users.subscriptions.renew(
            sub_id="sub_id",
            user_id=0,
            new_plan="new_plan",
        )
        assert_matches_type(PlainAPIResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_renew(self, async_client: AsyncAlbotAPISDK) -> None:
        response = await async_client.users.subscriptions.with_raw_response.renew(
            sub_id="sub_id",
            user_id=0,
            new_plan="new_plan",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(PlainAPIResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_renew(self, async_client: AsyncAlbotAPISDK) -> None:
        async with async_client.users.subscriptions.with_streaming_response.renew(
            sub_id="sub_id",
            user_id=0,
            new_plan="new_plan",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(PlainAPIResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_renew(self, async_client: AsyncAlbotAPISDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sub_id` but received ''"):
            await async_client.users.subscriptions.with_raw_response.renew(
                sub_id="",
                user_id=0,
                new_plan="new_plan",
            )
