"""Tests for authorization roles and permissions."""

from datetime import UTC, datetime, timedelta

import pytest

from full_stack_ai_shared.auth import TokenPayload
from full_stack_ai_shared.authorization import (
    ROLE_PERMISSIONS,
    Permission,
    Role,
    extract_roles,
    require_permission,
)
from full_stack_ai_shared.exceptions import ApplicationError


def create_token_with_roles(*roles: Role) -> TokenPayload:
    """Create a token payload with assigned roles."""

    now = datetime.now(UTC)

    return TokenPayload(
        subject="user-123",
        issued_at=now,
        expires_at=now + timedelta(minutes=30),
        issuer="full-stack-ai-portfolio",
        audience="full-stack-ai-applications",
        roles=[role.value for role in roles],
    )


def test_admin_permissions() -> None:
    permissions = ROLE_PERMISSIONS[Role.ADMIN]

    assert Permission.ADMIN in permissions
    assert Permission.DELETE in permissions
    assert Permission.WRITE in permissions
    assert Permission.READ in permissions


def test_engineer_permissions() -> None:
    permissions = ROLE_PERMISSIONS[Role.ENGINEER]

    assert Permission.WRITE in permissions
    assert Permission.EXECUTE in permissions
    assert Permission.DELETE not in permissions


def test_viewer_permissions() -> None:
    permissions = ROLE_PERMISSIONS[Role.VIEWER]

    assert permissions == {Permission.READ}


def test_extract_roles() -> None:
    token = create_token_with_roles(
        Role.ADMIN,
        Role.ANALYST,
    )

    assert extract_roles(token) == {
        Role.ADMIN,
        Role.ANALYST,
    }


def test_extract_roles_ignores_unknown_roles() -> None:
    now = datetime.now(UTC)

    token = TokenPayload(
        subject="user-123",
        issued_at=now,
        expires_at=now + timedelta(minutes=30),
        issuer="full-stack-ai-portfolio",
        audience="full-stack-ai-applications",
        roles=["admin", "unknown-role"],
    )

    assert extract_roles(token) == {Role.ADMIN}


def test_require_permission_allows_authorized_role() -> None:
    token = create_token_with_roles(Role.ENGINEER)
    dependency = require_permission(Permission.WRITE)

    result = dependency(token)

    assert result is token


def test_require_permission_allows_admin() -> None:
    token = create_token_with_roles(Role.ADMIN)
    dependency = require_permission(Permission.DELETE)

    result = dependency(token)

    assert result is token


def test_require_permission_denies_unauthorized_role() -> None:
    token = create_token_with_roles(Role.VIEWER)
    dependency = require_permission(Permission.WRITE)

    with pytest.raises(ApplicationError) as exc_info:
        dependency(token)

    assert exc_info.value.status_code == 403
    assert exc_info.value.code == "permission_denied"


def test_require_permission_denies_token_without_roles() -> None:
    token = create_token_with_roles()
    dependency = require_permission(Permission.READ)

    with pytest.raises(ApplicationError) as exc_info:
        dependency(token)

    assert exc_info.value.status_code == 403
    assert exc_info.value.code == "permission_denied"
