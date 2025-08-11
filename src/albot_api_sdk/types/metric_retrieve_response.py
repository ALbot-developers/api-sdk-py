# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MetricRetrieveResponse", "Data", "DataMetrics"]


class DataMetrics(BaseModel):
    connected: int

    guilds: int


class Data(BaseModel):
    metrics: DataMetrics


class MetricRetrieveResponse(BaseModel):
    data: Data

    message: str
