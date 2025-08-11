# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .connection_command import ConnectionCommand

__all__ = ["ConnectionCommandRetrieveResponse"]


class ConnectionCommandRetrieveResponse(BaseModel):
    data: ConnectionCommand

    message: str
