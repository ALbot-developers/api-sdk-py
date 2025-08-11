# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["GuildCreateQuickReportParams"]


class GuildCreateQuickReportParams(TypedDict, total=False):
    category: Required[str]

    description: Required[str]

    turnstile_token: Required[Annotated[str, PropertyInfo(alias="turnstile-token")]]
    """Cloudflare Turnstile token"""
