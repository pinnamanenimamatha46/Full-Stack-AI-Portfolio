"""Custom application exceptions."""

from __future__ import annotations


class ApplicationError(Exception):
    """Base exception for application-level errors."""

    def __init__(
        self,
        message: str,
        *,
        code: str = "application_error",
        status_code: int = 400,
        field: str | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.status_code = status_code
        self.field = field


class NotFoundError(ApplicationError):
    """Raised when a requested resource cannot be found."""

    def __init__(
        self,
        message: str = "Resource not found.",
        *,
        code: str = "not_found",
    ) -> None:
        super().__init__(
            message,
            code=code,
            status_code=404,
        )


class ConflictError(ApplicationError):
    """Raised when a request conflicts with existing state."""

    def __init__(
        self,
        message: str = "Resource conflict.",
        *,
        code: str = "conflict",
        field: str | None = None,
    ) -> None:
        super().__init__(
            message,
            code=code,
            status_code=409,
            field=field,
        )


class ValidationError(ApplicationError):
    """Raised when application-level validation fails."""

    def __init__(
        self,
        message: str = "Validation failed.",
        *,
        code: str = "validation_error",
        field: str | None = None,
    ) -> None:
        super().__init__(
            message,
            code=code,
            status_code=422,
            field=field,
        )
