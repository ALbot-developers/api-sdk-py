# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SettingUpdateParams"]


class SettingUpdateParams(TypedDict, total=False):
    audio_api: Optional[Literal["gtts", "openai"]]

    character_limit: Optional[int]
    """Maximum character limit for messages"""

    custom_voice: Optional[str]

    lang: Optional[str]

    read_guild: Optional[bool]

    read_name: Optional[bool]

    read_name_on_join: Optional[bool]

    read_name_on_leave: Optional[bool]

    read_not_joined_users: Optional[bool]

    speech_speed: Optional[float]
    """Speech speed multiplier"""

    translate: Optional[bool]
