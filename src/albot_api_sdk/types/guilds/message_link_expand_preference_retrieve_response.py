# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .message_link_expand_preference import MessageLinkExpandPreference

__all__ = ["MessageLinkExpandPreferenceRetrieveResponse"]


class MessageLinkExpandPreferenceRetrieveResponse(BaseModel):
    data: MessageLinkExpandPreference

    message: str
