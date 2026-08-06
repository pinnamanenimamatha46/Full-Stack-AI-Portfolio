"""Tests for shared AI-agent abstractions, execution state, and memory."""

import pytest

from full_stack_ai_shared.agents import (
    AgentMemory,
    AgentRequest,
    AgentResult,
    AgentState,
    AgentStatus,
    BaseAgent,
)


class EchoAgent(BaseAgent):
    """Simple agent implementation used for testing."""

    async def run(self, request: AgentRequest) -> AgentResult:
        """Return the submitted task as a successful result."""
        return AgentResult(
            agent_name=self.name,
            success=True,
            output=f"Processed: {request.task}",
            metadata={"context_size": len(request.context)},
        )


def test_agent_request_defaults() -> None:
    """AgentRequest should provide an empty context by default."""
    request = AgentRequest(task="Analyze equipment health")

    assert request.task == "Analyze equipment health"
    assert request.context == {}


def test_agent_result_defaults() -> None:
    """AgentResult should provide empty metadata by default."""
    result = AgentResult(
        agent_name="diagnostic-agent",
        success=True,
        output="No critical anomaly detected.",
    )

    assert result.agent_name == "diagnostic-agent"
    assert result.success is True
    assert result.output == "No critical anomaly detected."
    assert result.metadata == {}


def test_agent_rejects_empty_name() -> None:
    """BaseAgent should reject an empty agent name."""
    with pytest.raises(
        ValueError,
        match="Agent name cannot be empty",
    ):
        EchoAgent("")


@pytest.mark.asyncio
async def test_agent_run() -> None:
    """An agent should process a request and return an AgentResult."""
    agent = EchoAgent("echo-agent")
    request = AgentRequest(
        task="Inspect compressor vibration",
        context={"asset_id": "CMP-1001"},
    )

    result = await agent.run(request)

    assert agent.name == "echo-agent"
    assert result.agent_name == "echo-agent"
    assert result.success is True
    assert result.output == "Processed: Inspect compressor vibration"
    assert result.metadata == {"context_size": 1}


def test_agent_state_defaults() -> None:
    """AgentState should initialize with pending execution defaults."""
    state = AgentState()

    assert state.execution_id
    assert state.status == AgentStatus.PENDING
    assert state.current_step is None
    assert state.inputs == {}
    assert state.outputs == {}
    assert state.errors == []


def test_agent_state_marks_running() -> None:
    """AgentState should transition to running."""
    state = AgentState()

    state.mark_running("planning")

    assert state.status == AgentStatus.RUNNING
    assert state.current_step == "planning"


def test_agent_state_marks_completed() -> None:
    """AgentState should store outputs when execution completes."""
    state = AgentState()
    state.mark_running("execution")

    state.mark_completed({"result": "success"})

    assert state.status == AgentStatus.COMPLETED
    assert state.current_step is None
    assert state.outputs == {"result": "success"}
    assert state.errors == []


def test_agent_state_marks_failed() -> None:
    """AgentState should store an error when execution fails."""
    state = AgentState()
    state.mark_running("tool-execution")

    state.mark_failed("Tool invocation failed.")

    assert state.status == AgentStatus.FAILED
    assert state.current_step is None
    assert state.errors == ["Tool invocation failed."]


def test_agent_memory_stores_and_reads_entry() -> None:
    """AgentMemory should store and retrieve an entry."""
    memory = AgentMemory()

    entry = memory.set(
        "asset_id",
        "CMP-1001",
        metadata={"source": "request"},
    )

    stored_entry = memory.get("asset_id")

    assert entry.key == "asset_id"
    assert stored_entry is not None
    assert stored_entry.value == "CMP-1001"
    assert stored_entry.metadata == {"source": "request"}
    assert memory.contains("asset_id") is True
    assert len(memory) == 1


def test_agent_memory_replaces_existing_entry() -> None:
    """AgentMemory should replace an entry with the same key."""
    memory = AgentMemory()

    memory.set("status", "pending")
    memory.set("status", "completed")

    entry = memory.get("status")

    assert entry is not None
    assert entry.value == "completed"
    assert len(memory) == 1


def test_agent_memory_removes_entry() -> None:
    """AgentMemory should remove and return an existing entry."""
    memory = AgentMemory()
    memory.set("temporary", 123)

    removed = memory.remove("temporary")

    assert removed is not None
    assert removed.value == 123
    assert memory.contains("temporary") is False
    assert len(memory) == 0


def test_agent_memory_lists_entries() -> None:
    """AgentMemory should list entries in insertion order."""
    memory = AgentMemory()
    memory.set("first", 1)
    memory.set("second", 2)

    entries = memory.list_entries()

    assert [entry.key for entry in entries] == ["first", "second"]


def test_agent_memory_clears_entries() -> None:
    """AgentMemory should clear all stored entries."""
    memory = AgentMemory()
    memory.set("first", 1)
    memory.set("second", 2)

    memory.clear()

    assert len(memory) == 0
    assert memory.list_entries() == []


def test_agent_memory_rejects_empty_key() -> None:
    """AgentMemory should reject an empty key."""
    memory = AgentMemory()

    with pytest.raises(
        ValueError,
        match="Memory key cannot be empty",
    ):
        memory.set("", "value")
