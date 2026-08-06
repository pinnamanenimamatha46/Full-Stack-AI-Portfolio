"""Tests for shared AI tool execution context."""

import pytest

from full_stack_ai_shared.tools.context import ToolContext


def test_tool_context_defaults() -> None:
    """ToolContext should provide generated and empty default values."""
    context = ToolContext()

    assert context.execution_id
    assert context.agent_name is None
    assert context.user_id is None
    assert context.metadata == {}


def test_tool_context_accepts_execution_details() -> None:
    """ToolContext should store agent, user, and metadata values."""
    context = ToolContext(
        execution_id="execution-123",
        agent_name="maintenance-agent",
        user_id="user-456",
        metadata={"environment": "test"},
    )

    assert context.execution_id == "execution-123"
    assert context.agent_name == "maintenance-agent"
    assert context.user_id == "user-456"
    assert context.metadata == {"environment": "test"}


def test_tool_context_gets_metadata_value() -> None:
    """ToolContext should return stored metadata."""
    context = ToolContext(
        metadata={"asset_id": "PUMP-101"},
    )

    assert context.get_metadata("asset_id") == "PUMP-101"


def test_tool_context_returns_metadata_default() -> None:
    """ToolContext should return a default for missing metadata."""
    context = ToolContext()

    assert context.get_metadata("asset_id", "UNKNOWN") == "UNKNOWN"


def test_tool_context_sets_metadata_value() -> None:
    """ToolContext should add and update metadata."""
    context = ToolContext()

    context.set_metadata("region", "west")
    assert context.metadata == {"region": "west"}

    context.set_metadata("region", "central")
    assert context.metadata == {"region": "central"}


def test_tool_context_rejects_empty_execution_id() -> None:
    """ToolContext should reject an empty execution identifier."""
    with pytest.raises(
        ValueError,
        match="Execution ID must not be empty",
    ):
        ToolContext(execution_id=" ")


def test_tool_context_rejects_empty_agent_name() -> None:
    """ToolContext should reject an empty provided agent name."""
    with pytest.raises(
        ValueError,
        match="Agent name must not be empty",
    ):
        ToolContext(agent_name=" ")


def test_tool_context_rejects_empty_user_id() -> None:
    """ToolContext should reject an empty provided user identifier."""
    with pytest.raises(
        ValueError,
        match="User ID must not be empty",
    ):
        ToolContext(user_id=" ")


def test_tool_context_rejects_empty_metadata_key() -> None:
    """ToolContext should reject an empty metadata key."""
    context = ToolContext()

    with pytest.raises(
        ValueError,
        match="Metadata key must not be empty",
    ):
        context.set_metadata(" ", "value")
