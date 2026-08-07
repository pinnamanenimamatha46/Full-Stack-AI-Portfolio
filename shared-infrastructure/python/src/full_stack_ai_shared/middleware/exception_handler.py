"""Unhandled exception middleware."""

from __future__ import annotations

from http import HTTPStatus

from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

from full_stack_ai_shared.logging import get_logger, get_request_id

logger = get_logger(__name__)


class ExceptionHandlerMiddleware:
    """Convert unhandled application exceptions into JSON responses."""

    def __init__(
        self,
        app: ASGIApp,
        *,
        include_exception_details: bool = False,
    ) -> None:
        """Initialize the exception handler middleware."""
        self.app = app
        self.include_exception_details = include_exception_details

    async def __call__(
        self,
        scope: Scope,
        receive: Receive,
        send: Send,
    ) -> None:
        """Handle unhandled HTTP application exceptions."""
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        try:
            await self.app(scope, receive, send)
        except Exception as exc:
            request_id = get_request_id()

            logger.exception(
                "Unhandled HTTP application exception",
                extra={
                    "request_id": request_id,
                    "http_method": str(scope.get("method", "UNKNOWN")),
                    "http_path": str(scope.get("path", "/")),
                    "exception_type": type(exc).__name__,
                },
            )

            response_content: dict[str, str | int | None] = {
                "status_code": HTTPStatus.INTERNAL_SERVER_ERROR.value,
                "error": HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
                "message": "An unexpected error occurred.",
                "request_id": request_id,
            }

            if self.include_exception_details:
                response_content["detail"] = str(exc)

            response = JSONResponse(
                content=response_content,
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            )

            await response(scope, receive, send)
