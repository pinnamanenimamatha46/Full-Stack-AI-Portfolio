"""Tests for shared AI-agent execution context."""

import pytest

from full_stack_ai_shared.agents.context import AgentExecutionContext
from full_stack_ai_shared.agents.memory import AgentMemory
from full_stack_ai_shared.tools import ToolRegistry


def test_agent_execution_context_defaults() -> None:
    """Context should provide shared service defaults."""
    context = AgentExecutionContext()

    assert context.execution_id
    assert isinstance(context.tool_registry, ToolRegistry)
    assert isinstance(context.memory, AgentMemory)
    assert context.rag_service is None
    assert context.metadata == {}


def test_agent_execution_context_accepts_services() -> None:
    """Context should store supplied shared services."""
    registry = ToolRegistry()
    memory = AgentMemory()
    rag_service = object()

    context = AgentExecutionContext(
        execution_id="execution-123",
        tool_registry=registry,
        memory=memory,
        rag_service=rag_service,
        metadata={"environment": "test"},
    )

    assert context.execution_id == "execution-123"
    assert context.tool_registry is registry
    assert context.memory is memory
    assert context.rag_service is rag_service
    assert context.metadata == {"environment": "test"}


def test_agent_execution_context_gets_metadata() -> None:
    """Context should return stored metadata."""
    context = AgentExecutionContext(
        metadata={"asset_id": "PUMP-101"},
    )

    assert context.get_metadata("asset_id") == "PUMP-101"


def test_agent_execution_context_returns_metadata_default() -> None:
    """Context should return the supplied default for missing metadata."""
    context = AgentExecutionContext()

    assert context.get_metadata("region", "unknown") == "unknown"


def test_agent_execution_context_sets_metadata() -> None:
    """Context should add and update metadata."""
    context = AgentExecutionContext()

    context.set_metadata("region", "west")
    assert context.metadata == {"region": "west"}

    context.set_metadata("region", "central")
    assert context.metadata == {"region": "central"}


def test_agent_execution_context_rejects_empty_execution_id() -> None:
    """Context should reject an empty execution identifier."""
    with pytest.raises(
        ValueError,
        match="Execution ID must not be empty",
    ):
        AgentExecutionContext(execution_id=" ")


def test_agent_execution_context_rejects_empty_metadata_key() -> None:
    """Context should reject an empty metadata key."""
    context = AgentExecutionContext()

    with pytest.raises(
        ValueError,
        match="Metadata key must not be empty",
    ):
        context.set_metadata(" ", "value")
