"""Tests for shared authentication utilities."""

from datetime import timedelta
from typing import Annotated

import jwt
import pytest
from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from full_stack_ai_shared.auth import (
    TokenError,
    TokenPayload,
    create_access_token,
    create_current_token_dependency,
    decode_access_token,
    hash_password,
    verify_password,
)
from full_stack_ai_shared.exceptions import register_exception_handlers
from full_stack_ai_shared.logging import RequestLoggingMiddleware
from full_stack_ai_shared.security import TokenSettings


def create_token_settings() -> TokenSettings:
    """Return isolated token settings for tests."""

    return TokenSettings(
        secret_key="test-secret-key-that-is-at-least-32-characters",
        access_token_expire_minutes=30,
    )


def create_auth_test_app(settings: TokenSettings) -> FastAPI:
    """Create a FastAPI application with bearer authentication."""

    app = FastAPI()
    app.add_middleware(RequestLoggingMiddleware)
    register_exception_handlers(app)

    current_token = create_current_token_dependency(settings)

    @app.get("/protected")
    async def protected_route(
        token: Annotated[TokenPayload, Depends(current_token)],
    ) -> dict[str, str]:
        return {"subject": token.subject}

    return app


def test_hash_password() -> None:
    password = "StrongPassword123!"
    hashed_password = hash_password(password)

    assert hashed_password != password
    assert verify_password(password, hashed_password) is True


def test_verify_password_rejects_invalid_password() -> None:
    hashed_password = hash_password("CorrectPassword123!")

    assert (
        verify_password(
            "WrongPassword123!",
            hashed_password,
        )
        is False
    )


def test_hash_password_uses_unique_salt() -> None:
    password = "StrongPassword123!"

    first_hash = hash_password(password)
    second_hash = hash_password(password)

    assert first_hash != second_hash
    assert verify_password(password, first_hash) is True
    assert verify_password(password, second_hash) is True


def test_hash_password_rejects_empty_password() -> None:
    with pytest.raises(
        ValueError,
        match="Password cannot be empty",
    ):
        hash_password("")


def test_verify_password_rejects_empty_values() -> None:
    assert verify_password("", "stored-hash") is False
    assert verify_password("password", "") is False


def test_create_and_decode_access_token() -> None:
    settings = create_token_settings()

    token = create_access_token("user-123", settings)
    payload = decode_access_token(token, settings)

    assert payload.subject == "user-123"
    assert payload.issuer == settings.issuer
    assert payload.audience == settings.audience
    assert payload.expires_at > payload.issued_at


def test_create_access_token_rejects_empty_subject() -> None:
    settings = create_token_settings()

    with pytest.raises(
        ValueError,
        match="Token subject cannot be empty",
    ):
        create_access_token("", settings)


def test_access_token_rejects_protected_claim_override() -> None:
    settings = create_token_settings()

    with pytest.raises(
        ValueError,
        match="cannot override protected claims",
    ):
        create_access_token(
            "user-123",
            settings,
            additional_claims={"sub": "other-user"},
        )


def test_decode_access_token_rejects_expired_token() -> None:
    settings = create_token_settings()

    token = create_access_token(
        "user-123",
        settings,
        expires_delta=timedelta(seconds=-1),
    )

    with pytest.raises(
        TokenError,
        match="Access token has expired",
    ):
        decode_access_token(token, settings)


def test_decode_access_token_rejects_invalid_signature() -> None:
    settings = create_token_settings()
    different_settings = TokenSettings(
        secret_key="different-secret-key-that-is-also-long-enough",
    )

    token = create_access_token("user-123", settings)

    with pytest.raises(
        TokenError,
        match="Access token is invalid",
    ):
        decode_access_token(token, different_settings)


def test_decode_access_token_rejects_missing_subject() -> None:
    settings = create_token_settings()

    token = jwt.encode(
        {
            "iat": 1_700_000_000,
            "exp": 4_000_000_000,
            "iss": settings.issuer,
            "aud": settings.audience,
        },
        settings.secret_key,
        algorithm=settings.algorithm,
    )

    with pytest.raises(
        TokenError,
        match="Access token subject is invalid",
    ):
        decode_access_token(token, settings)


def test_protected_route_accepts_valid_token() -> None:
    settings = create_token_settings()
    client = TestClient(create_auth_test_app(settings))
    token = create_access_token("user-123", settings)

    response = client.get(
        "/protected",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json() == {"subject": "user-123"}


def test_protected_route_rejects_missing_token() -> None:
    settings = create_token_settings()
    client = TestClient(create_auth_test_app(settings))

    response = client.get("/protected")
    payload = response.json()

    assert response.status_code == 401
    assert payload["errors"][0]["code"] == "not_authenticated"


def test_protected_route_rejects_invalid_token() -> None:
    settings = create_token_settings()
    client = TestClient(create_auth_test_app(settings))

    response = client.get(
        "/protected",
        headers={"Authorization": "Bearer invalid-token"},
    )
    payload = response.json()

    assert response.status_code == 401
    assert payload["errors"][0]["code"] == "invalid_access_token"
