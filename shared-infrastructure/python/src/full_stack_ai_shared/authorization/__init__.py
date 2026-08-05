"""Authorization utilities."""

from full_stack_ai_shared.authorization.dependencies import (
    extract_roles,
    require_permission,
)
from full_stack_ai_shared.authorization.permissions import (
    ROLE_PERMISSIONS,
    Permission,
)
from full_stack_ai_shared.authorization.roles import Role

__all__ = [
    "ROLE_PERMISSIONS",
    "Permission",
    "Role",
    "extract_roles",
    "require_permission",
]
