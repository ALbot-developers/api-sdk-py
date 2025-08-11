# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubscriptionActivateParams"]


class SubscriptionActivateParams(TypedDict, total=False):
    guild_id: Required[int]
