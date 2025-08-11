# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubscriptionRenewParams"]


class SubscriptionRenewParams(TypedDict, total=False):
    new_plan: Required[str]
