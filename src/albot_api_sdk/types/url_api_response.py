# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["URLAPIResponse", "Data"]


class Data(BaseModel):
    url: str


class URLAPIResponse(BaseModel):
    data: Data

    message: str
