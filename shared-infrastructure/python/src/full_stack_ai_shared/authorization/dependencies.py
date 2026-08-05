"""FastAPI authorization dependencies."""

from collections.abc import Callable

from full_stack_ai_shared.auth import TokenPayload
from full_stack_ai_shared.authorization.permissions import (
    ROLE_PERMISSIONS,
    Permission,
)
from full_stack_ai_shared.authorization.roles import Role
from full_stack_ai_shared.exceptions import ApplicationError


def extract_roles(token: TokenPayload) -> set[Role]:
    """Extract validated roles from a token payload."""

    raw_roles = getattr(token, "roles", None)

    if raw_roles is None:
        return set()

    roles: set[Role] = set()

    for raw_role in raw_roles:
        try:
            roles.add(Role(raw_role))
        except ValueError:
            continue

    return roles


def require_permission(
    permission: Permission,
) -> Callable[[TokenPayload], TokenPayload]:
    """Create a dependency requiring a specific permission."""

    def dependency(token: TokenPayload) -> TokenPayload:
        roles = extract_roles(token)

        has_permission = any(
            permission in ROLE_PERMISSIONS.get(role, set()) for role in roles
        )

        if not has_permission:
            raise ApplicationError(
                "You do not have permission to perform this action.",
                code="permission_denied",
                status_code=403,
            )

        return token

    return dependency
