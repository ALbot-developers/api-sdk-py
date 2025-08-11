# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .partial_guild import PartialGuild

__all__ = ["GuildListResponse", "Data"]


class Data(BaseModel):
    guilds: List[PartialGuild]


class GuildListResponse(BaseModel):
    data: Data

    message: str
