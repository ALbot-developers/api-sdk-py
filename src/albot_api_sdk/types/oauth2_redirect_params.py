# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["Oauth2RedirectParams"]


class Oauth2RedirectParams(TypedDict, total=False):
    redirect: Required[str]
