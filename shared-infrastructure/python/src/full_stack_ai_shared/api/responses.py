"""Reusable API response models."""

from typing import Generic, TypeVar

from pydantic import BaseModel, Field

DataT = TypeVar("DataT")


class SuccessResponse(BaseModel, Generic[DataT]):
    """Standard successful API response."""

    success: bool = True
    message: str
    data: DataT | None = None


class ErrorDetail(BaseModel):
    """Structured API error information."""

    code: str
    message: str
    field: str | None = None


class ErrorResponse(BaseModel):
    """Standard API error response."""

    success: bool = False
    message: str
    errors: list[ErrorDetail] = Field(default_factory=list)
    request_id: str | None = None
