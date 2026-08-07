"""Tests for HTTP request timing middleware."""

import logging

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from full_stack_ai_shared.middleware.timing import RequestTimingMiddleware


def create_test_app() -> FastAPI:
    """Create an application configured with timing middleware."""
    app = FastAPI()
    app.add_middleware(RequestTimingMiddleware)

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "healthy"}

    return app


def test_timing_middleware_adds_process_time_header() -> None:
    """Middleware should add the request processing duration header."""
    client = TestClient(create_test_app())

    response = client.get("/health")

    assert response.status_code == 200
    assert "X-Process-Time" in response.headers
    assert float(response.headers["X-Process-Time"]) >= 0


def test_timing_middleware_preserves_response_body() -> None:
    """Middleware should not modify the application response body."""
    client = TestClient(create_test_app())

    response = client.get("/health")

    assert response.json() == {"status": "healthy"}


def test_timing_middleware_logs_request_duration(
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Middleware should log request execution timing information."""
    client = TestClient(create_test_app())

    with caplog.at_level(logging.INFO):
        response = client.get("/health")

    assert response.status_code == 200
    assert "HTTP request timing" in caplog.text
