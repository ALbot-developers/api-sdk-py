# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TrustedRoleListResponse", "Data"]


class Data(BaseModel):
    enabled: Optional[bool] = None

    role_ids: Optional[List[int]] = None


class TrustedRoleListResponse(BaseModel):
    data: Data

    message: str
