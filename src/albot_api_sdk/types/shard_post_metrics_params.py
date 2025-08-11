# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ShardPostMetricsParams"]


class ShardPostMetricsParams(TypedDict, total=False):
    connected: Optional[int]

    guilds: Optional[int]
