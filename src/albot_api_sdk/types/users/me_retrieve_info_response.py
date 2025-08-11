# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MeRetrieveInfoResponse", "Data", "DataInfo", "DataInfoAvatarDecorationData"]


class DataInfoAvatarDecorationData(BaseModel):
    asset: str

    sku_id: Optional[str] = None


class DataInfo(BaseModel):
    id: str

    accent_color: Optional[int] = None

    avatar: Optional[str] = None

    avatar_decoration_data: Optional[DataInfoAvatarDecorationData] = None

    banner: Optional[str] = None

    bot: Optional[bool] = None

    discriminator: str

    email: Optional[str] = None

    flags: int

    global_name: Optional[str] = None

    locale: str

    mfa_enabled: bool

    premium_type: Optional[int] = None

    public_flags: int

    system: Optional[bool] = None

    username: str

    verified: Optional[bool] = None


class Data(BaseModel):
    info: DataInfo


class MeRetrieveInfoResponse(BaseModel):
    data: Data

    message: str
