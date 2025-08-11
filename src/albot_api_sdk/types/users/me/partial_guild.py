# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["PartialGuild"]


class PartialGuild(BaseModel):
    id: str

    banner: Optional[str] = None

    features: List[str]

    icon: Optional[str] = None

    name: str

    owner: bool

    permissions: str

    approximate_member_count: Optional[int] = None

    approximate_presence_count: Optional[int] = None
