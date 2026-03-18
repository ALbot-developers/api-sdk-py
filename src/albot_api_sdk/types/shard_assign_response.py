# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ShardAssignResponse", "Data"]


class Data(BaseModel):
    dashscope_tts_key: str

    discord_token: str

    heartbeat_token: str

    sakura_tts_key: str

    sentry_dsn: str

    shard_count: int

    shard_id: int

    tts_key: str


class ShardAssignResponse(BaseModel):
    data: Data

    message: str
