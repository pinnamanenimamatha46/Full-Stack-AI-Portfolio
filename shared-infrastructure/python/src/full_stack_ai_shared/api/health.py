"""Reusable health-check API router."""

from datetime import UTC, datetime

from fastapi import APIRouter

from full_stack_ai_shared import __version__
from full_stack_ai_shared.api.responses import SuccessResponse

health_router = APIRouter(tags=["Health"])


@health_router.get(
    "/health",
    response_model=SuccessResponse[dict[str, str]],
)
async def health_check() -> SuccessResponse[dict[str, str]]:
    """Return the shared service health status."""

    return SuccessResponse(
        message="Service is healthy.",
        data={
            "status": "healthy",
            "version": __version__,
            "timestamp": datetime.now(UTC).isoformat(),
        },
    )
