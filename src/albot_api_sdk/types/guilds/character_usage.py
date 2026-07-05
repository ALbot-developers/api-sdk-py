# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CharacterUsage"]


class CharacterUsage(BaseModel):
    monthly_quota: int

    used_characters: int
