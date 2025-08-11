# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ShardAssignResponse", "Data"]


class Data(BaseModel):
    discord_token: str

    heartbeat_token: str

    sentry_dsn: str

    shard_count: int

    shard_id: int

    tts_key: str


class ShardAssignResponse(BaseModel):
    data: Data

    message: str
