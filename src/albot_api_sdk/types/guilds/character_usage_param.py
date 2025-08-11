# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CharacterUsageParam"]


class CharacterUsageParam(TypedDict, total=False):
    used_characters: Required[int]

    monthly_quota: int
