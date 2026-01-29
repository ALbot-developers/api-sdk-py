# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["ShardGetConnectionCommandsResponse", "Data"]


class Data(BaseModel):
    commands: Dict[str, object]


class ShardGetConnectionCommandsResponse(BaseModel):
    data: Data

    message: str
