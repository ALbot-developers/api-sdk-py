# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

__all__ = ["TrustedRoleUpdateParams"]


class TrustedRoleUpdateParams(TypedDict, total=False):
    enabled: Optional[bool]

    role_ids: Optional[Iterable[int]]
