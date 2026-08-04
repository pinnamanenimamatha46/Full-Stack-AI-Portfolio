"""Request-scoped logging context."""

from contextvars import ContextVar
from uuid import uuid4

_request_id_context: ContextVar[str | None] = ContextVar(
    "request_id",
    default=None,
)


def create_request_id() -> str:
    """Create a new request identifier."""

    return str(uuid4())


def set_request_id(request_id: str) -> None:
    """Store the current request identifier."""

    _request_id_context.set(request_id)


def get_request_id() -> str | None:
    """Return the current request identifier."""

    return _request_id_context.get()


def clear_request_id() -> None:
    """Clear the current request identifier."""

    _request_id_context.set(None)
