"""HTTP request timing middleware."""

from __future__ import annotations

from time import perf_counter

from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from full_stack_ai_shared.logging import get_logger

logger = get_logger(__name__)


class RequestTimingMiddleware:
    """Measure and report HTTP request execution time."""

    def __init__(
        self,
        app: ASGIApp,
        *,
        process_time_header: str = "X-Process-Time",
    ) -> None:
        """Initialize the request timing middleware."""
        self.app = app
        self.process_time_header = process_time_header

    async def __call__(
        self,
        scope: Scope,
        receive: Receive,
        send: Send,
    ) -> None:
        """Measure the execution duration of an HTTP request."""
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        started_at = perf_counter()
        method = str(scope.get("method", "UNKNOWN"))
        path = str(scope.get("path", "/"))

        async def send_wrapper(message: Message) -> None:
            if message["type"] == "http.response.start":
                elapsed_seconds = perf_counter() - started_at
                headers = MutableHeaders(scope=message)
                headers[self.process_time_header] = f"{elapsed_seconds:.6f}"

            await send(message)

        try:
            await self.app(scope, receive, send_wrapper)
        finally:
            elapsed_seconds = perf_counter() - started_at

            logger.info(
                "HTTP request timing",
                extra={
                    "http_method": method,
                    "http_path": path,
                    "duration_seconds": elapsed_seconds,
                },
            )
