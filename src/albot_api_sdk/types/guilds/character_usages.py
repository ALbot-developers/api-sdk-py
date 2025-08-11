# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .character_usage import CharacterUsage

__all__ = ["CharacterUsages"]


class CharacterUsages(BaseModel):
    standard: CharacterUsage

    wavenet: CharacterUsage
