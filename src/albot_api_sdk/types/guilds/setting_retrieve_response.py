# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SettingRetrieveResponse", "Data", "DataSettings"]


class DataSettings(BaseModel):
    audio_api: Literal["gtts", "openai"]

    character_limit: int

    guild_id: int

    lang: str

    read_guild: bool

    read_name: bool

    read_name_on_join: bool

    read_name_on_leave: bool

    read_not_joined_users: bool

    speech_speed: float

    translate: bool

    custom_voice: Optional[str] = None


class Data(BaseModel):
    settings: DataSettings


class SettingRetrieveResponse(BaseModel):
    data: Data

    message: str
