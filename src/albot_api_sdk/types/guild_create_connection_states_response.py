# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .guilds.character_usages import CharacterUsages

__all__ = ["GuildCreateConnectionStatesResponse", "Data", "DataConnectionStates"]


class DataConnectionStates(BaseModel):
    character_limit: int

    character_usage: CharacterUsages

    custom_voice: Optional[str] = None

    dict_: object = FieldInfo(alias="dict")

    dict_keys: List[object]

    guild_id: int

    language_code: Union[Literal["auto"], str]

    read_guild: bool

    read_name: bool

    read_name_on_join: bool

    read_name_on_leave: bool

    read_not_joined_users: bool

    service: Literal["gtts", "openai"]

    speech_speed: float

    standard_voice: str

    target_id: int

    translate: bool

    vc_id: int

    wavenet_voice: str

    sync_count: Optional[int] = None

    unix_time_connected: Optional[float] = None


class Data(BaseModel):
    connection_states: DataConnectionStates


class GuildCreateConnectionStatesResponse(BaseModel):
    data: Data

    message: str
