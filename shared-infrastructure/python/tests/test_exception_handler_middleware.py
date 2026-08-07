"""Tests for unhandled exception middleware."""

import logging

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from full_stack_ai_shared.middleware.exception_handler import (
    ExceptionHandlerMiddleware,
)


def create_test_app(
    *,
    include_exception_details: bool = False,
) -> FastAPI:
    """Create an application configured with exception middleware."""
    app = FastAPI()
    app.add_middleware(
        ExceptionHandlerMiddleware,
        include_exception_details=include_exception_details,
    )

    @app.get("/success")
    async def success() -> dict[str, str]:
        return {"status": "healthy"}

    @app.get("/failure")
    async def failure() -> None:
        raise RuntimeError("Database connection failed.")

    return app


def test_exception_middleware_preserves_successful_response() -> None:
    """Middleware should preserve successful application responses."""
    client = TestClient(create_test_app())

    response = client.get("/success")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_exception_middleware_returns_internal_server_error() -> None:
    """Middleware should convert exceptions into JSON responses."""
    client = TestClient(create_test_app(), raise_server_exceptions=False)

    response = client.get("/failure")

    assert response.status_code == 500
    assert response.json()["status_code"] == 500
    assert response.json()["error"] == "Internal Server Error"
    assert response.json()["message"] == "An unexpected error occurred."


def test_exception_middleware_hides_exception_details_by_default() -> None:
    """Middleware should not expose internal exception details by default."""
    client = TestClient(create_test_app(), raise_server_exceptions=False)

    response = client.get("/failure")

    assert "detail" not in response.json()
    assert "Database connection failed." not in response.text


def test_exception_middleware_can_include_exception_details() -> None:
    """Middleware should expose details only when explicitly configured."""
    client = TestClient(
        create_test_app(include_exception_details=True),
        raise_server_exceptions=False,
    )

    response = client.get("/failure")

    assert response.status_code == 500
    assert response.json()["detail"] == "Database connection failed."


def test_exception_middleware_logs_unhandled_exception(
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Middleware should log unhandled application exceptions."""
    client = TestClient(create_test_app(), raise_server_exceptions=False)

    with caplog.at_level(logging.ERROR):
        response = client.get("/failure")

    assert response.status_code == 500
    assert "Unhandled HTTP application exception" in caplog.text
    assert "Database connection failed." in caplog.text
