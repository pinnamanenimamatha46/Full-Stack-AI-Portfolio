"""Tests for shared AI-tool exceptions."""

import pytest

from full_stack_ai_shared.tools.exceptions import (
    ToolAlreadyRegisteredError,
    ToolError,
    ToolExecutionError,
    ToolNotFoundError,
    ToolRegistrationError,
    ToolValidationError,
)


@pytest.mark.parametrize(
    "exception_type",
    [
        ToolRegistrationError,
        ToolAlreadyRegisteredError,
        ToolNotFoundError,
        ToolValidationError,
        ToolExecutionError,
    ],
)
def test_tool_exceptions_inherit_from_tool_error(
    exception_type: type[ToolError],
) -> None:
    """Specialized tool exceptions should inherit from ToolError."""
    error = exception_type("Tool operation failed.")

    assert isinstance(error, ToolError)
    assert isinstance(error, Exception)


@pytest.mark.parametrize(
    ("exception_type", "message"),
    [
        (
            ToolError,
            "Generic tool failure.",
        ),
        (
            ToolRegistrationError,
            "Tool registration failed.",
        ),
        (
            ToolAlreadyRegisteredError,
            "Tool is already registered.",
        ),
        (
            ToolNotFoundError,
            "Requested tool was not found.",
        ),
        (
            ToolValidationError,
            "Tool input validation failed.",
        ),
        (
            ToolExecutionError,
            "Tool execution failed.",
        ),
    ],
)
def test_tool_exceptions_preserve_messages(
    exception_type: type[ToolError],
    message: str,
) -> None:
    """Tool exceptions should preserve supplied messages."""
    error = exception_type(message)

    assert str(error) == message


def test_tool_error_can_be_raised_and_caught() -> None:
    """ToolError should behave like a normal exception."""
    with pytest.raises(
        ToolError,
        match="Shared tool failure.",
    ):
        raise ToolError("Shared tool failure.")


def test_specialized_exception_can_be_caught_as_tool_error() -> None:
    """Specialized exceptions should be catchable as ToolError."""
    with pytest.raises(
        ToolError,
        match="Tool could not be executed.",
    ):
        raise ToolExecutionError("Tool could not be executed.")
