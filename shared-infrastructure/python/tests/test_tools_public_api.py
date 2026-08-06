"""Tests for the shared AI tool framework public API."""

from full_stack_ai_shared.tools import (
    BaseTool,
    FunctionTool,
    ToolAlreadyRegisteredError,
    ToolContext,
    ToolDefinition,
    ToolError,
    ToolExecutionError,
    ToolNotFoundError,
    ToolRegistry,
    ToolRequest,
    ToolResult,
)


def test_tools_public_api_exports_expected_types() -> None:
    """The tools package should expose the complete public API."""
    assert BaseTool.__name__ == "BaseTool"
    assert FunctionTool.__name__ == "FunctionTool"
    assert ToolAlreadyRegisteredError.__name__ == ("ToolAlreadyRegisteredError")
    assert ToolContext.__name__ == "ToolContext"
    assert ToolDefinition.__name__ == "ToolDefinition"
    assert ToolError.__name__ == "ToolError"
    assert ToolExecutionError.__name__ == "ToolExecutionError"
    assert ToolNotFoundError.__name__ == "ToolNotFoundError"
    assert ToolRegistry.__name__ == "ToolRegistry"
    assert ToolRequest.__name__ == "ToolRequest"
    assert ToolResult.__name__ == "ToolResult"
