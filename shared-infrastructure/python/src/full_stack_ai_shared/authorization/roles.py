"""Application roles."""

from enum import StrEnum


class Role(StrEnum):
    ADMIN = "admin"
    ENGINEER = "engineer"
    ANALYST = "analyst"
    OPERATOR = "operator"
    AUDITOR = "auditor"
    VIEWER = "viewer"
