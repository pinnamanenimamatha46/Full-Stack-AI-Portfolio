"""HTTP request logging middleware."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Any

from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from full_stack_ai_shared.logging import (
    clear_request_id,
    create_request_id,
    get_logger,
    set_request_id,
)

logger = get_logger(__name__)


class RequestLoggingMiddleware:
    """Log incoming HTTP requests and outgoing responses."""

    def __init__(
        self,
        app: ASGIApp,
        *,
        request_id_header: str = "X-Request-ID",
    ) -> None:
        """Initialize the request logging middleware."""
        self.app = app
        self.request_id_header = request_id_header

    async def __call__(
        self,
        scope: Scope,
        receive: Receive,
        send: Send,
    ) -> None:
        """Process and log an HTTP request."""
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        request_id = self._get_request_id(scope)
        set_request_id(request_id)

        method = str(scope.get("method", "UNKNOWN"))
        path = str(scope.get("path", "/"))
        client_ip = self._get_client_ip(scope)

        status_code: int | None = None

        async def send_wrapper(message: Message) -> None:
            nonlocal status_code

            if message["type"] == "http.response.start":
                status_code = int(message["status"])

                headers = MutableHeaders(scope=message)
                headers[self.request_id_header] = request_id

            await send(message)

        logger.info(
            "HTTP request started",
            extra={
                "request_id": request_id,
                "http_method": method,
                "http_path": path,
                "client_ip": client_ip,
            },
        )

        try:
            await self.app(scope, receive, send_wrapper)
        except Exception:
            logger.exception(
                "HTTP request failed",
                extra={
                    "request_id": request_id,
                    "http_method": method,
                    "http_path": path,
                    "client_ip": client_ip,
                },
            )
            raise
        else:
            logger.info(
                "HTTP request completed",
                extra={
                    "request_id": request_id,
                    "http_method": method,
                    "http_path": path,
                    "client_ip": client_ip,
                    "status_code": status_code,
                },
            )
        finally:
            clear_request_id()

    def _get_request_id(self, scope: Scope) -> str:
        """Return an incoming request ID or create a new one."""
        header_name = self.request_id_header.lower().encode("latin-1")
        raw_headers = scope.get("headers", [])

        for raw_name, raw_value in raw_headers:
            name = bytes(raw_name)
            value = bytes(raw_value)

            if name.lower() == header_name:
                request_id = value.decode("latin-1").strip()

                if request_id:
                    return request_id

        return str(create_request_id())

    @staticmethod
    def _get_client_ip(scope: Scope) -> str | None:
        """Return the client IP address when available."""
        client: Any = scope.get("client")

        if not client:
            return None

        return str(client[0])


RequestHandler = Callable[[Scope, Receive, Send], Awaitable[None]]
