"""Tests for request logging middleware."""

from __future__ import annotations

import logging
from collections.abc import Iterator

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from full_stack_ai_shared.logging import get_request_id
from full_stack_ai_shared.middleware import RequestLoggingMiddleware


@pytest.fixture
def app() -> FastAPI:
    """Create a FastAPI application with request logging enabled."""
    application = FastAPI()
    application.add_middleware(RequestLoggingMiddleware)

    @application.get("/health")
    async def health() -> dict[str, str | None]:
        return {
            "status": "healthy",
            "request_id": get_request_id(),
        }

    @application.get("/failure")
    async def failure() -> None:
        raise RuntimeError("Unexpected middleware test failure.")

    return application


@pytest.fixture
def anyio_backend() -> str:
    """Use asyncio for async tests."""
    return "asyncio"


@pytest.fixture
def log_records(
    caplog: pytest.LogCaptureFixture,
) -> Iterator[pytest.LogCaptureFixture]:
    """Capture middleware log records."""
    caplog.set_level(
        logging.INFO,
        logger="full_stack_ai_shared.middleware.request_logging",
    )

    yield caplog


@pytest.mark.anyio
async def test_middleware_adds_generated_request_id(
    app: FastAPI,
) -> None:
    """Middleware should generate and return a request ID."""
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:
        response = await client.get("/health")

    assert response.status_code == 200
    assert response.headers["X-Request-ID"]
    assert response.json()["request_id"] == response.headers["X-Request-ID"]


@pytest.mark.anyio
async def test_middleware_preserves_incoming_request_id(
    app: FastAPI,
) -> None:
    """Middleware should preserve a valid incoming request ID."""
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:
        response = await client.get(
            "/health",
            headers={"X-Request-ID": "request-123"},
        )

    assert response.status_code == 200
    assert response.headers["X-Request-ID"] == "request-123"
    assert response.json()["request_id"] == "request-123"


@pytest.mark.anyio
async def test_middleware_logs_request_start_and_completion(
    app: FastAPI,
    log_records: pytest.LogCaptureFixture,
) -> None:
    """Middleware should log request start and completion."""
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:
        response = await client.get(
            "/health",
            headers={"X-Request-ID": "logging-test-123"},
        )

    assert response.status_code == 200

    messages = [record.getMessage() for record in log_records.records]

    assert "HTTP request started" in messages
    assert "HTTP request completed" in messages

    completion_record = next(
        record
        for record in log_records.records
        if record.getMessage() == "HTTP request completed"
    )

    assert completion_record.request_id == "logging-test-123"
    assert completion_record.http_method == "GET"
    assert completion_record.http_path == "/health"
    assert completion_record.status_code == 200


@pytest.mark.anyio
async def test_middleware_logs_unhandled_exception(
    app: FastAPI,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Middleware should log exceptions before re-raising them."""
    caplog.set_level(
        logging.ERROR,
        logger="full_stack_ai_shared.middleware.request_logging",
    )

    transport = ASGITransport(
        app=app,
        raise_app_exceptions=True,
    )

    with pytest.raises(
        RuntimeError,
        match="Unexpected middleware test failure",
    ):
        async with AsyncClient(
            transport=transport,
            base_url="http://test",
        ) as client:
            await client.get(
                "/failure",
                headers={"X-Request-ID": "failure-test-123"},
            )

    failure_record = next(
        record
        for record in caplog.records
        if record.getMessage() == "HTTP request failed"
    )

    assert failure_record.request_id == "failure-test-123"
    assert failure_record.http_method == "GET"
    assert failure_record.http_path == "/failure"
