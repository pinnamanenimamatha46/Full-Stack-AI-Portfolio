"""JWT access-token creation and validation."""

from datetime import UTC, datetime, timedelta
from typing import Any

import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from pydantic import BaseModel

from full_stack_ai_shared.security import TokenSettings


class TokenPayload(BaseModel):
    """Validated JWT payload."""

    subject: str
    issued_at: datetime
    expires_at: datetime
    issuer: str
    audience: str


class TokenError(ValueError):
    """Raised when an access token cannot be validated."""


def create_access_token(
    subject: str,
    settings: TokenSettings,
    *,
    expires_delta: timedelta | None = None,
    additional_claims: dict[str, Any] | None = None,
) -> str:
    """Create a signed JWT access token."""

    if not subject.strip():
        raise ValueError("Token subject cannot be empty.")

    issued_at = datetime.now(UTC)
    expires_at = issued_at + (
        expires_delta or timedelta(minutes=settings.access_token_expire_minutes)
    )

    payload: dict[str, Any] = {
        "sub": subject,
        "iat": issued_at,
        "exp": expires_at,
        "iss": settings.issuer,
        "aud": settings.audience,
    }

    if additional_claims:
        protected_claims = {"sub", "iat", "exp", "iss", "aud"}
        conflicting_claims = protected_claims.intersection(additional_claims)

        if conflicting_claims:
            names = ", ".join(sorted(conflicting_claims))
            raise ValueError(
                f"Additional claims cannot override protected claims: {names}"
            )

        payload.update(additional_claims)

    return jwt.encode(
        payload,
        settings.secret_key,
        algorithm=settings.algorithm,
    )


def decode_access_token(
    token: str,
    settings: TokenSettings,
) -> TokenPayload:
    """Decode and validate a JWT access token."""

    if not token:
        raise TokenError("Access token cannot be empty.")

    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm],
            audience=settings.audience,
            issuer=settings.issuer,
        )
    except ExpiredSignatureError as exc:
        raise TokenError("Access token has expired.") from exc
    except InvalidTokenError as exc:
        raise TokenError("Access token is invalid.") from exc

    subject = payload.get("sub")

    if not isinstance(subject, str) or not subject:
        raise TokenError("Access token subject is invalid.")

    return TokenPayload(
        subject=subject,
        issued_at=datetime.fromtimestamp(payload["iat"], tz=UTC),
        expires_at=datetime.fromtimestamp(payload["exp"], tz=UTC),
        issuer=payload["iss"],
        audience=payload["aud"],
    )
