# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from .._models import BaseModel

__all__ = ["ListSubscriptions", "Data", "DataSubscription"]


class DataSubscription(BaseModel):
    last_updated: date

    plan: str

    sub_id: str

    sub_start: date

    user_id: int

    guild_id: Optional[int] = None


class Data(BaseModel):
    subscriptions: List[DataSubscription]


class ListSubscriptions(BaseModel):
    data: Data

    message: str
