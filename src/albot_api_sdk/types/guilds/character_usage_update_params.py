# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CharacterUsageUpdateParams", "ClonedVoice", "Standard", "Wavenet"]


class CharacterUsageUpdateParams(TypedDict, total=False):
    cloned_voice: Optional[ClonedVoice]

    standard: Optional[Standard]

    wavenet: Optional[Wavenet]


class ClonedVoice(TypedDict, total=False):
    used_characters: Required[int]


class Standard(TypedDict, total=False):
    used_characters: Required[int]


class Wavenet(TypedDict, total=False):
    used_characters: Required[int]
