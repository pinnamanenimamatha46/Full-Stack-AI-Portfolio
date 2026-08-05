"""Shared authentication utilities."""

from full_stack_ai_shared.auth.dependencies import (
    bearer_scheme,
    create_current_token_dependency,
)
from full_stack_ai_shared.auth.passwords import (
    hash_password,
    verify_password,
)
from full_stack_ai_shared.auth.tokens import (
    TokenError,
    TokenPayload,
    create_access_token,
    decode_access_token,
)

__all__ = [
    "TokenError",
    "TokenPayload",
    "bearer_scheme",
    "create_access_token",
    "create_current_token_dependency",
    "decode_access_token",
    "hash_password",
    "verify_password",
]
