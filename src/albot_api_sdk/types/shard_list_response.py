# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ShardListResponse", "Data"]


class Data(BaseModel):
    ids: List[int]


class ShardListResponse(BaseModel):
    data: Data

    message: str
