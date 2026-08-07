"""JSON Web Token creation and validation utilities."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Any

import jwt


class JWTError(Exception):
    """Base exception for JWT-related failures."""


class JWTExpiredError(JWTError):
    """Raised when a JWT has expired."""


class JWTInvalidError(JWTError):
    """Raised when a JWT is invalid."""


def create_access_token(
    subject: str,
    secret_key: str,
    *,
    algorithm: str = "HS256",
    expires_delta: timedelta = timedelta(minutes=30),
    additional_claims: dict[str, Any] | None = None,
) -> str:
    """Create a signed access token for a subject."""
    if not subject.strip():
        raise ValueError("JWT subject must not be empty.")

    if not secret_key.strip():
        raise ValueError("JWT secret key must not be empty.")

    issued_at = datetime.now(UTC)
    expires_at = issued_at + expires_delta

    payload: dict[str, Any] = {
        "sub": subject,
        "iat": issued_at,
        "exp": expires_at,
    }

    if additional_claims:
        payload.update(additional_claims)

    token = jwt.encode(
        payload,
        secret_key,
        algorithm=algorithm,
    )

    return str(token)


def decode_access_token(
    token: str,
    secret_key: str,
    *,
    algorithm: str = "HS256",
) -> dict[str, Any]:
    """Decode and validate an access token."""
    if not token.strip():
        raise JWTInvalidError("JWT token must not be empty.")

    if not secret_key.strip():
        raise ValueError("JWT secret key must not be empty.")

    try:
        payload = jwt.decode(
            token,
            secret_key,
            algorithms=[algorithm],
        )
    except jwt.ExpiredSignatureError as exc:
        raise JWTExpiredError("JWT token has expired.") from exc
    except jwt.PyJWTError as exc:
        raise JWTInvalidError("JWT token is invalid.") from exc

    return dict(payload)
