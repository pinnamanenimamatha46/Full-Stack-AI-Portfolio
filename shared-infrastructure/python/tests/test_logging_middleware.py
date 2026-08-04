"""Tests for FastAPI request logging middleware."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from full_stack_ai_shared.logging import (
    REQUEST_ID_HEADER,
    RequestLoggingMiddleware,
)


def create_test_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(RequestLoggingMiddleware)

    @app.get("/health")
    async def health_check() -> dict[str, str]:
        return {"status": "healthy"}

    return app


def test_middleware_generates_request_id() -> None:
    client = TestClient(create_test_app())

    response = client.get("/health")

    assert response.status_code == 200
    assert response.headers[REQUEST_ID_HEADER]


def test_middleware_preserves_request_id() -> None:
    client = TestClient(create_test_app())
    request_id = "test-request-123"

    response = client.get(
        "/health",
        headers={REQUEST_ID_HEADER: request_id},
    )

    assert response.status_code == 200
    assert response.headers[REQUEST_ID_HEADER] == request_id
