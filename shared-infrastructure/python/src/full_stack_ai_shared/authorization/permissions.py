"""Permission definitions."""

from enum import StrEnum

from full_stack_ai_shared.authorization.roles import Role


class Permission(StrEnum):
    READ = "read"
    WRITE = "write"
    DELETE = "delete"
    ADMIN = "admin"
    EXECUTE = "execute"


ROLE_PERMISSIONS: dict[Role, set[Permission]] = {
    Role.ADMIN: {
        Permission.READ,
        Permission.WRITE,
        Permission.DELETE,
        Permission.ADMIN,
        Permission.EXECUTE,
    },
    Role.ENGINEER: {
        Permission.READ,
        Permission.WRITE,
        Permission.EXECUTE,
    },
    Role.ANALYST: {
        Permission.READ,
        Permission.EXECUTE,
    },
    Role.OPERATOR: {
        Permission.READ,
        Permission.WRITE,
    },
    Role.AUDITOR: {
        Permission.READ,
    },
    Role.VIEWER: {
        Permission.READ,
    },
}
