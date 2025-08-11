# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CharacterUsage"]


class CharacterUsage(BaseModel):
    used_characters: int

    monthly_quota: Optional[int] = None
