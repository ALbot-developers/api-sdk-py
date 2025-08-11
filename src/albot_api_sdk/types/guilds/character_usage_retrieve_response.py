# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .character_usages import CharacterUsages

__all__ = ["CharacterUsageRetrieveResponse"]


class CharacterUsageRetrieveResponse(BaseModel):
    data: CharacterUsages

    message: str
