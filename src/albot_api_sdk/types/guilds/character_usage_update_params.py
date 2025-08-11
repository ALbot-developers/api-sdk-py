# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .character_usage_param import CharacterUsageParam

__all__ = ["CharacterUsageUpdateParams"]


class CharacterUsageUpdateParams(TypedDict, total=False):
    standard: Optional[CharacterUsageParam]

    wavenet: Optional[CharacterUsageParam]
