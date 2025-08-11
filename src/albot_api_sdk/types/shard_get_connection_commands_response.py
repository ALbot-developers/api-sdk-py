# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ShardGetConnectionCommandsResponse", "Data"]


class Data(BaseModel):
    commands: object


class ShardGetConnectionCommandsResponse(BaseModel):
    data: Data

    message: str
