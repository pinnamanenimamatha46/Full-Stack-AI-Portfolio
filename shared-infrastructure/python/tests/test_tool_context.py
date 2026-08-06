"""Tests for the shared AI-tool execution context."""

import pytest

from full_stack_ai_shared.tools import ToolContext


def test_tool_context_defaults() -> None:
    """ToolContext should provide generated defaults."""
    context = ToolContext()

    assert context.execution_id
    assert context.agent_name is None
    assert context.user_id is None
    assert context.metadata == {}


def test_tool_context_generates_unique_execution_ids() -> None:
    """ToolContext instances should receive unique execution IDs."""
    first_context = ToolContext()
    second_context = ToolContext()

    assert first_context.execution_id != second_context.execution_id


def test_tool_context_accepts_identity_values() -> None:
    """ToolContext should preserve supplied identity values."""
    context = ToolContext(
        agent_name="diagnostic-agent",
        user_id="user-101",
    )

    assert context.agent_name == "diagnostic-agent"
    assert context.user_id == "user-101"


def test_tool_context_normalizes_identity_values() -> None:
    """ToolContext should remove surrounding whitespace."""
    context = ToolContext(
        execution_id="  execution-101  ",
        agent_name="  diagnostic-agent  ",
        user_id="  user-101  ",
    )

    assert context.execution_id == "execution-101"
    assert context.agent_name == "diagnostic-agent"
    assert context.user_id == "user-101"


def test_tool_context_accepts_initial_metadata() -> None:
    """ToolContext should preserve supplied metadata."""
    context = ToolContext(
        metadata={
            "asset_id": "pump-101",
            "priority": "high",
        }
    )

    assert context.metadata == {
        "asset_id": "pump-101",
        "priority": "high",
    }


def test_tool_context_sets_metadata() -> None:
    """ToolContext should store metadata values."""
    context = ToolContext()

    context.set_metadata("asset_id", "compressor-202")

    assert context.metadata["asset_id"] == "compressor-202"


def test_tool_context_normalizes_metadata_keys() -> None:
    """Metadata operations should normalize key whitespace."""
    context = ToolContext()

    context.set_metadata("  asset_id  ", "pump-101")

    assert context.metadata == {
        "asset_id": "pump-101",
    }
    assert context.get_metadata("  asset_id  ") == "pump-101"


def test_tool_context_gets_existing_metadata() -> None:
    """ToolContext should return existing metadata values."""
    context = ToolContext(
        metadata={
            "asset_id": "pump-101",
        }
    )

    assert context.get_metadata("asset_id") == "pump-101"


def test_tool_context_gets_default_for_missing_metadata() -> None:
    """ToolContext should return a default for missing metadata."""
    context = ToolContext()

    result = context.get_metadata(
        "priority",
        "normal",
    )

    assert result == "normal"


@pytest.mark.parametrize(
    ("field_name", "field_value", "message"),
    [
        (
            "execution_id",
            "",
            "Tool execution ID must not be empty.",
        ),
        (
            "execution_id",
            "   ",
            "Tool execution ID must not be empty.",
        ),
        (
            "agent_name",
            "",
            "Agent name must not be empty.",
        ),
        (
            "agent_name",
            "   ",
            "Agent name must not be empty.",
        ),
        (
            "user_id",
            "",
            "User ID must not be empty.",
        ),
        (
            "user_id",
            "   ",
            "User ID must not be empty.",
        ),
    ],
)
def test_tool_context_rejects_empty_identity_values(
    field_name: str,
    field_value: str,
    message: str,
) -> None:
    """ToolContext should reject empty identity fields."""
    values = {
        field_name: field_value,
    }

    with pytest.raises(
        ValueError,
        match=message,
    ):
        ToolContext(**values)


@pytest.mark.parametrize(
    "metadata_key",
    [
        "",
        "   ",
    ],
)
def test_tool_context_set_metadata_rejects_empty_key(
    metadata_key: str,
) -> None:
    """set_metadata should reject empty keys."""
    context = ToolContext()

    with pytest.raises(
        ValueError,
        match="Metadata key must not be empty.",
    ):
        context.set_metadata(
            metadata_key,
            "value",
        )


@pytest.mark.parametrize(
    "metadata_key",
    [
        "",
        "   ",
    ],
)
def test_tool_context_get_metadata_rejects_empty_key(
    metadata_key: str,
) -> None:
    """get_metadata should reject empty keys."""
    context = ToolContext()

    with pytest.raises(
        ValueError,
        match="Metadata key must not be empty.",
    ):
        context.get_metadata(metadata_key)
