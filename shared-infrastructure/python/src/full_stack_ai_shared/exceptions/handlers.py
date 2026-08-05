"""FastAPI exception handlers."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Any, cast

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.responses import Response

from full_stack_ai_shared.api import ErrorDetail, ErrorResponse
from full_stack_ai_shared.exceptions.errors import ApplicationError
from full_stack_ai_shared.logging import get_logger, get_request_id

logger = get_logger(__name__)

ExceptionHandler = Callable[
    [Request, Exception],
    Response | Awaitable[Response],
]


def build_error_response(
    *,
    message: str,
    errors: list[ErrorDetail],
) -> dict[str, Any]:
    """Build a serializable standard error response."""

    response = ErrorResponse(
        message=message,
        errors=errors,
        request_id=get_request_id(),
    )
    return response.model_dump()


async def application_error_handler(
    request: Request,
    exc: ApplicationError,
) -> JSONResponse:
    """Handle known application exceptions."""

    logger.warning(
        "%s %s failed: %s",
        request.method,
        request.url.path,
        exc.message,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=build_error_response(
            message=exc.message,
            errors=[
                ErrorDetail(
                    code=exc.code,
                    message=exc.message,
                    field=exc.field,
                )
            ],
        ),
    )


async def request_validation_error_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    """Handle FastAPI request-validation failures."""

    errors = [
        ErrorDetail(
            code=str(error["type"]),
            message=str(error["msg"]),
            field=".".join(str(part) for part in error["loc"]),
        )
        for error in exc.errors()
    ]

    logger.warning(
        "%s %s validation failed",
        request.method,
        request.url.path,
    )

    return JSONResponse(
        status_code=422,
        content=build_error_response(
            message="Request validation failed.",
            errors=errors,
        ),
    )


async def unhandled_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    """Handle unexpected exceptions without exposing internal details."""

    logger.exception(
        "%s %s raised an unexpected exception",
        request.method,
        request.url.path,
        exc_info=exc,
    )

    return JSONResponse(
        status_code=500,
        content=build_error_response(
            message="An unexpected error occurred.",
            errors=[
                ErrorDetail(
                    code="internal_server_error",
                    message="The server could not complete the request.",
                )
            ],
        ),
    )


def register_exception_handlers(app: FastAPI) -> None:
    """Register all shared exception handlers on a FastAPI application."""

    app.add_exception_handler(
        ApplicationError,
        cast(ExceptionHandler, application_error_handler),
    )
    app.add_exception_handler(
        RequestValidationError,
        cast(ExceptionHandler, request_validation_error_handler),
    )
    app.add_exception_handler(
        Exception,
        unhandled_exception_handler,
    )
