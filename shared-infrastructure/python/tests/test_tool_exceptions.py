"""Tests for shared AI tool exceptions."""

from full_stack_ai_shared.tools.exceptions import (
    ToolAlreadyRegisteredError,
    ToolError,
    ToolExecutionError,
    ToolNotFoundError,
)


def test_tool_not_found_error() -> None:
    """ToolNotFoundError should include the missing tool name."""
    error = ToolNotFoundError("asset_lookup")

    assert isinstance(error, ToolError)
    assert error.tool_name == "asset_lookup"
    assert str(error) == "Tool 'asset_lookup' is not registered."


def test_tool_already_registered_error() -> None:
    """ToolAlreadyRegisteredError should include the duplicate tool name."""
    error = ToolAlreadyRegisteredError("asset_lookup")

    assert isinstance(error, ToolError)
    assert error.tool_name == "asset_lookup"
    assert str(error) == "Tool 'asset_lookup' is already registered."


def test_tool_execution_error() -> None:
    """ToolExecutionError should preserve execution failure details."""
    error = ToolExecutionError(
        tool_name="asset_lookup",
        message="Database connection failed.",
    )

    assert isinstance(error, ToolError)
    assert error.tool_name == "asset_lookup"
    assert error.message == "Database connection failed."
    assert (
        str(error)
        == "Tool 'asset_lookup' execution failed: Database connection failed."
    )
