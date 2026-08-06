"""Tests for shared AI tool data models."""

import pytest

from full_stack_ai_shared.tools.models import (
    ToolDefinition,
    ToolRequest,
    ToolResult,
)


def test_tool_definition_defaults() -> None:
    """ToolDefinition should provide an empty input schema."""
    definition = ToolDefinition(
        name="asset_lookup",
        description="Look up an industrial asset.",
    )

    assert definition.name == "asset_lookup"
    assert definition.description == "Look up an industrial asset."
    assert definition.input_schema == {}


def test_tool_definition_rejects_empty_name() -> None:
    """ToolDefinition should reject an empty name."""
    with pytest.raises(ValueError, match="Tool name must not be empty"):
        ToolDefinition(
            name=" ",
            description="Valid description.",
        )


def test_tool_definition_rejects_empty_description() -> None:
    """ToolDefinition should reject an empty description."""
    with pytest.raises(
        ValueError,
        match="Tool description must not be empty",
    ):
        ToolDefinition(
            name="asset_lookup",
            description=" ",
        )


def test_tool_request_defaults() -> None:
    """ToolRequest should generate an identifier and empty arguments."""
    request = ToolRequest(tool_name="asset_lookup")

    assert request.tool_name == "asset_lookup"
    assert request.arguments == {}
    assert request.request_id


def test_tool_request_accepts_arguments() -> None:
    """ToolRequest should store tool arguments."""
    request = ToolRequest(
        tool_name="asset_lookup",
        arguments={"asset_id": "PUMP-101"},
    )

    assert request.arguments == {"asset_id": "PUMP-101"}


def test_tool_request_rejects_empty_tool_name() -> None:
    """ToolRequest should reject an empty tool name."""
    with pytest.raises(ValueError, match="Tool name must not be empty"):
        ToolRequest(tool_name=" ")


def test_successful_tool_result() -> None:
    """ToolResult should store successful tool output."""
    result = ToolResult(
        tool_name="asset_lookup",
        success=True,
        output={"asset_id": "PUMP-101"},
    )

    assert result.tool_name == "asset_lookup"
    assert result.success is True
    assert result.output == {"asset_id": "PUMP-101"}
    assert result.error is None
    assert result.metadata == {}


def test_failed_tool_result() -> None:
    """ToolResult should store failure details."""
    result = ToolResult(
        tool_name="asset_lookup",
        success=False,
        error="Asset was not found.",
    )

    assert result.success is False
    assert result.output is None
    assert result.error == "Asset was not found."


def test_successful_result_rejects_error() -> None:
    """Successful results should not contain errors."""
    with pytest.raises(
        ValueError,
        match="Successful tool results must not contain an error",
    ):
        ToolResult(
            tool_name="asset_lookup",
            success=True,
            error="Unexpected error.",
        )


def test_failed_result_requires_error() -> None:
    """Failed results should require an error message."""
    with pytest.raises(
        ValueError,
        match="Failed tool results must contain an error message",
    ):
        ToolResult(
            tool_name="asset_lookup",
            success=False,
        )
