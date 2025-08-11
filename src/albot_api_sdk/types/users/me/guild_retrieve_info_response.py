# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .partial_guild import PartialGuild

__all__ = ["GuildRetrieveInfoResponse", "Data"]


class Data(BaseModel):
    info: PartialGuild


class GuildRetrieveInfoResponse(BaseModel):
    data: Data

    message: str
