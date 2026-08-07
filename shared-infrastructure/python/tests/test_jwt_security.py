"""Tests for JSON Web Token security utilities."""

from datetime import timedelta

import pytest

from full_stack_ai_shared.security import (
    JWTExpiredError,
    JWTInvalidError,
    create_access_token,
    decode_access_token,
)

SECRET_KEY = "enterprise-test-secret-key"


def test_create_and_decode_access_token() -> None:
    """A generated token should preserve its subject."""
    token = create_access_token(
        subject="user-123",
        secret_key=SECRET_KEY,
    )

    payload = decode_access_token(
        token,
        SECRET_KEY,
    )

    assert payload["sub"] == "user-123"
    assert "iat" in payload
    assert "exp" in payload


def test_access_token_supports_additional_claims() -> None:
    """Additional claims should be included in the token."""
    token = create_access_token(
        subject="user-123",
        secret_key=SECRET_KEY,
        additional_claims={
            "role": "administrator",
            "tenant_id": "tenant-456",
        },
    )

    payload = decode_access_token(token, SECRET_KEY)

    assert payload["role"] == "administrator"
    assert payload["tenant_id"] == "tenant-456"


def test_create_access_token_rejects_empty_subject() -> None:
    """Token creation should reject an empty subject."""
    with pytest.raises(
        ValueError,
        match="JWT subject must not be empty",
    ):
        create_access_token(
            subject=" ",
            secret_key=SECRET_KEY,
        )


def test_decode_access_token_rejects_invalid_token() -> None:
    """Token decoding should reject malformed tokens."""
    with pytest.raises(
        JWTInvalidError,
        match="JWT token is invalid",
    ):
        decode_access_token(
            "not-a-valid-token",
            SECRET_KEY,
        )


def test_decode_access_token_rejects_wrong_secret() -> None:
    """Token decoding should reject tokens signed with another key."""
    token = create_access_token(
        subject="user-123",
        secret_key=SECRET_KEY,
    )

    with pytest.raises(JWTInvalidError):
        decode_access_token(
            token,
            "different-secret-key",
        )


def test_decode_access_token_rejects_expired_token() -> None:
    """Token decoding should reject expired tokens."""
    token = create_access_token(
        subject="user-123",
        secret_key=SECRET_KEY,
        expires_delta=timedelta(seconds=-1),
    )

    with pytest.raises(
        JWTExpiredError,
        match="JWT token has expired",
    ):
        decode_access_token(
            token,
            SECRET_KEY,
        )
