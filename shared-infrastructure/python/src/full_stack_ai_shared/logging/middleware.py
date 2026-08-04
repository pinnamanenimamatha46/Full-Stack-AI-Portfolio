"""FastAPI request logging middleware."""

from __future__ import annotations

from time import perf_counter
from typing import Final

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from full_stack_ai_shared.logging.logger import get_logger
from full_stack_ai_shared.logging.request_context import (
    clear_request_id,
    create_request_id,
    set_request_id,
)

REQUEST_ID_HEADER: Final[str] = "X-Request-ID"

logger = get_logger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Log HTTP requests and attach a request ID to each response."""

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        request_id = request.headers.get(REQUEST_ID_HEADER) or create_request_id()
        set_request_id(request_id)

        started_at = perf_counter()

        try:
            response = await call_next(request)

            duration_ms = (perf_counter() - started_at) * 1000

            logger.info(
                "%s %s completed with status %s in %.2f ms",
                request.method,
                request.url.path,
                response.status_code,
                duration_ms,
            )

            response.headers[REQUEST_ID_HEADER] = request_id
            return response
        except Exception:
            duration_ms = (perf_counter() - started_at) * 1000

            logger.exception(
                "%s %s failed after %.2f ms",
                request.method,
                request.url.path,
                duration_ms,
            )

            raise
        finally:
            clear_request_id()
