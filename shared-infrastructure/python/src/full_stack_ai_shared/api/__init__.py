"""Shared API utilities."""

from full_stack_ai_shared.api.health import health_router
from full_stack_ai_shared.api.responses import (
    ErrorDetail,
    ErrorResponse,
    SuccessResponse,
)

__all__ = [
    "ErrorDetail",
    "ErrorResponse",
    "SuccessResponse",
    "health_router",
]
