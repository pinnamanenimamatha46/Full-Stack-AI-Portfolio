"""Tests for shared exceptions and FastAPI handlers."""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

from full_stack_ai_shared.exceptions import (
    ApplicationError,
    ConflictError,
    NotFoundError,
    ValidationError,
    register_exception_handlers,
)
from full_stack_ai_shared.logging import RequestLoggingMiddleware


class ItemRequest(BaseModel):
    """Test request model."""

    quantity: int


def create_test_app() -> FastAPI:
    """Create a FastAPI application with shared handlers."""

    app = FastAPI()
    app.add_middleware(RequestLoggingMiddleware)
    register_exception_handlers(app)

    @app.get("/missing")
    async def missing() -> None:
        raise NotFoundError("Asset not found.")

    @app.get("/conflict")
    async def conflict() -> None:
        raise ConflictError(
            "Asset already exists.",
            field="asset_id",
        )

    @app.post("/items")
    async def create_item(payload: ItemRequest) -> dict[str, int]:
        return {"quantity": payload.quantity}

    @app.get("/unexpected")
    async def unexpected() -> None:
        raise RuntimeError("Sensitive internal failure.")

    return app


def test_application_error() -> None:
    error = ApplicationError(
        "Operation failed.",
        code="operation_failed",
        status_code=400,
        field="name",
    )

    assert str(error) == "Operation failed."
    assert error.message == "Operation failed."
    assert error.code == "operation_failed"
    assert error.status_code == 400
    assert error.field == "name"


def test_not_found_error() -> None:
    error = NotFoundError("Asset not found.")

    assert error.status_code == 404
    assert error.code == "not_found"
    assert error.message == "Asset not found."


def test_conflict_error() -> None:
    error = ConflictError(
        "Asset already exists.",
        field="asset_id",
    )

    assert error.status_code == 409
    assert error.code == "conflict"
    assert error.field == "asset_id"


def test_validation_error() -> None:
    error = ValidationError(
        "Amount must be positive.",
        field="amount",
    )

    assert error.status_code == 422
    assert error.code == "validation_error"
    assert error.field == "amount"


def test_application_exception_handler() -> None:
    client = TestClient(create_test_app())

    response = client.get("/missing")
    payload = response.json()

    assert response.status_code == 404
    assert payload["success"] is False
    assert payload["message"] == "Asset not found."
    assert payload["errors"][0]["code"] == "not_found"
    assert payload["request_id"]


def test_conflict_exception_handler() -> None:
    client = TestClient(create_test_app())

    response = client.get("/conflict")
    payload = response.json()

    assert response.status_code == 409
    assert payload["errors"][0]["code"] == "conflict"
    assert payload["errors"][0]["field"] == "asset_id"


def test_request_validation_exception_handler() -> None:
    client = TestClient(create_test_app())

    response = client.post(
        "/items",
        json={"quantity": "invalid"},
    )
    payload = response.json()

    assert response.status_code == 422
    assert payload["success"] is False
    assert payload["message"] == "Request validation failed."
    assert payload["errors"]
    assert payload["errors"][0]["field"] == "body.quantity"


def test_unhandled_exception_handler() -> None:
    client = TestClient(
        create_test_app(),
        raise_server_exceptions=False,
    )

    response = client.get("/unexpected")
    payload = response.json()

    assert response.status_code == 500
    assert payload["success"] is False
    assert payload["message"] == "An unexpected error occurred."
    assert payload["errors"][0]["code"] == "internal_server_error"
    assert "Sensitive internal failure" not in response.text
