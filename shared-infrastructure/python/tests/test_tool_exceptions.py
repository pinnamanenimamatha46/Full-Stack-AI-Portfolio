"""Tests for shared AI tool exceptions."""

from full_stack_ai_shared.tools.exceptions import (
    ToolAlreadyRegisteredError,
    ToolError,
    ToolNotFoundError,
)


def test_tool_error_is_base_exception() -> None:
    """ToolError should inherit from Exception."""
    error = ToolError("Tool execution failed.")

    assert isinstance(error, Exception)
    assert str(error) == "Tool execution failed."


def test_tool_already_registered_error_message() -> None:
    """Duplicate registrations should identify the tool name."""
    error = ToolAlreadyRegisteredError("weather-tool")

    assert isinstance(error, ToolError)
    assert str(error) == "Tool 'weather-tool' is already registered."


def test_tool_not_found_error_message() -> None:
    """Missing-tool errors should identify the requested tool."""
    error = ToolNotFoundError("missing-tool")

    assert isinstance(error, ToolError)
    assert str(error) == "Tool 'missing-tool' is not registered"
