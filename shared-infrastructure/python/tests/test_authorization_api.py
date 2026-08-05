"""Tests for FastAPI authentication and authorization integration."""

from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from full_stack_ai_shared.auth import (
    TokenPayload,
    create_access_token,
    create_current_token_dependency,
)
from full_stack_ai_shared.authorization import (
    Permission,
    require_permission,
)
from full_stack_ai_shared.exceptions import register_exception_handlers
from full_stack_ai_shared.logging import RequestLoggingMiddleware
from full_stack_ai_shared.security import TokenSettings


def create_token_settings() -> TokenSettings:
    """Return token settings for API authorization tests."""

    return TokenSettings(
        secret_key="test-secret-key-that-is-at-least-32-characters",
        access_token_expire_minutes=30,
    )


def create_authorization_test_app(settings: TokenSettings) -> FastAPI:
    """Create a test application with authentication and RBAC."""

    app = FastAPI()
    app.add_middleware(RequestLoggingMiddleware)
    register_exception_handlers(app)

    current_token = create_current_token_dependency(settings)
    require_write = require_permission(Permission.WRITE)

    @app.get("/protected")
    async def protected_route(
        token: Annotated[TokenPayload, Depends(current_token)],
    ) -> dict[str, str]:
        return {"subject": token.subject}

    @app.post("/write")
    async def write_route(
        token: Annotated[TokenPayload, Depends(current_token)],
    ) -> dict[str, str]:
        authorized_token = require_write(token)

        return {
            "subject": authorized_token.subject,
            "status": "write-authorized",
        }

    return app


def test_engineer_can_access_write_endpoint() -> None:
    settings = create_token_settings()
    client = TestClient(create_authorization_test_app(settings))

    token = create_access_token(
        "engineer-123",
        settings,
        additional_claims={"roles": ["engineer"]},
    )

    response = client.post(
        "/write",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "subject": "engineer-123",
        "status": "write-authorized",
    }


def test_viewer_cannot_access_write_endpoint() -> None:
    settings = create_token_settings()
    client = TestClient(create_authorization_test_app(settings))

    token = create_access_token(
        "viewer-123",
        settings,
        additional_claims={"roles": ["viewer"]},
    )

    response = client.post(
        "/write",
        headers={"Authorization": f"Bearer {token}"},
    )
    payload = response.json()

    assert response.status_code == 403
    assert payload["success"] is False
    assert payload["errors"][0]["code"] == "permission_denied"


def test_missing_token_cannot_access_protected_endpoint() -> None:
    settings = create_token_settings()
    client = TestClient(create_authorization_test_app(settings))

    response = client.get("/protected")
    payload = response.json()

    assert response.status_code == 401
    assert payload["errors"][0]["code"] == "not_authenticated"


def test_admin_can_access_write_endpoint() -> None:
    settings = create_token_settings()
    client = TestClient(create_authorization_test_app(settings))

    token = create_access_token(
        "admin-123",
        settings,
        additional_claims={"roles": ["admin"]},
    )

    response = client.post(
        "/write",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "write-authorized"
