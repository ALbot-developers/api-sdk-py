# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DictRetrieveResponse", "Data"]


class Data(BaseModel):
    dict_: object = FieldInfo(alias="dict")


class DictRetrieveResponse(BaseModel):
    data: Data

    message: str
