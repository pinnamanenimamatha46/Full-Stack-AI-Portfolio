"""Reusable FastAPI authentication dependencies."""

from collections.abc import Callable
from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from full_stack_ai_shared.auth.tokens import (
    TokenError,
    TokenPayload,
    decode_access_token,
)
from full_stack_ai_shared.exceptions import ApplicationError
from full_stack_ai_shared.security import TokenSettings

bearer_scheme = HTTPBearer(auto_error=False)


def create_current_token_dependency(
    settings: TokenSettings,
) -> Callable[..., TokenPayload]:
    """Create a FastAPI dependency that validates bearer tokens."""

    def get_current_token(
        credentials: Annotated[
            HTTPAuthorizationCredentials | None,
            Depends(bearer_scheme),
        ],
    ) -> TokenPayload:
        if credentials is None:
            raise ApplicationError(
                "Authentication credentials were not provided.",
                code="not_authenticated",
                status_code=401,
            )

        if credentials.scheme.lower() != "bearer":
            raise ApplicationError(
                "Unsupported authentication scheme.",
                code="invalid_authentication_scheme",
                status_code=401,
            )

        try:
            return decode_access_token(
                credentials.credentials,
                settings,
            )
        except TokenError as exc:
            raise ApplicationError(
                str(exc),
                code="invalid_access_token",
                status_code=401,
            ) from exc

    return get_current_token
