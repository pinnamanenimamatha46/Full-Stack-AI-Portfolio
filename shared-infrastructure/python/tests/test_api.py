"""Tests for shared API utilities."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from full_stack_ai_shared.api import (
    ErrorDetail,
    ErrorResponse,
    SuccessResponse,
    health_router,
)


def create_test_app() -> FastAPI:
    app = FastAPI()
    app.include_router(health_router, prefix="/api/v1")
    return app


def test_success_response() -> None:
    response = SuccessResponse[dict[str, str]](
        message="Operation completed.",
        data={"status": "ready"},
    )

    assert response.success is True
    assert response.message == "Operation completed."
    assert response.data == {"status": "ready"}


def test_error_response() -> None:
    response = ErrorResponse(
        message="Validation failed.",
        errors=[
            ErrorDetail(
                code="invalid_value",
                message="The supplied value is invalid.",
                field="name",
            )
        ],
        request_id="request-123",
    )

    assert response.success is False
    assert response.request_id == "request-123"
    assert response.errors[0].code == "invalid_value"
    assert response.errors[0].field == "name"


def test_error_response_defaults_to_empty_errors() -> None:
    response = ErrorResponse(message="Unexpected error.")

    assert response.errors == []


def test_health_endpoint() -> None:
    client = TestClient(create_test_app())

    response = client.get("/api/v1/health")
    payload = response.json()

    assert response.status_code == 200
    assert payload["success"] is True
    assert payload["message"] == "Service is healthy."
    assert payload["data"]["status"] == "healthy"
    assert payload["data"]["version"] == "0.1.0"
    assert payload["data"]["timestamp"]
