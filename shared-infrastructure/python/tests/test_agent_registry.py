"""Tests for the shared AI-agent registry."""

from collections.abc import Callable
from typing import Any

import pytest

from full_stack_ai_shared.agents import (
    AgentRegistry,
    AgentRequest,
    AgentResult,
    BaseAgent,
)


class StubAgent(BaseAgent):
    """Simple agent implementation used for registry tests."""

    async def run(self, request: AgentRequest) -> AgentResult:
        """Return the submitted task as a successful result."""
        return AgentResult(
            agent_name=self.name,
            success=True,
            output=request.task,
        )


def test_agent_registry_starts_empty() -> None:
    """Registry should contain no agents after initialization."""
    registry = AgentRegistry()

    assert len(registry) == 0
    assert registry.list_names() == []


def test_agent_registry_registers_agent() -> None:
    """Registry should store an agent by name."""
    registry = AgentRegistry()
    agent = StubAgent(name="diagnostic-agent")

    registry.register(agent)

    assert len(registry) == 1
    assert registry.contains("diagnostic-agent")
    assert registry.get("diagnostic-agent") is agent


def test_agent_registry_rejects_duplicate_agent_name() -> None:
    """Registry should reject agents with duplicate names."""
    registry = AgentRegistry()
    first_agent = StubAgent(name="diagnostic-agent")
    second_agent = StubAgent(name="diagnostic-agent")

    registry.register(first_agent)

    with pytest.raises(
        ValueError,
        match="Agent 'diagnostic-agent' is already registered.",
    ):
        registry.register(second_agent)


def test_agent_registry_get_rejects_unknown_agent() -> None:
    """Registry should reject requests for unknown agents."""
    registry = AgentRegistry()

    with pytest.raises(
        KeyError,
        match="Agent 'missing-agent' is not registered.",
    ):
        registry.get("missing-agent")


def test_agent_registry_unregisters_agent() -> None:
    """Registry should remove and return a registered agent."""
    registry = AgentRegistry()
    agent = StubAgent(name="diagnostic-agent")
    registry.register(agent)

    removed_agent = registry.unregister("diagnostic-agent")

    assert removed_agent is agent
    assert not registry.contains("diagnostic-agent")
    assert len(registry) == 0


def test_agent_registry_unregister_rejects_unknown_agent() -> None:
    """Registry should reject removal of an unknown agent."""
    registry = AgentRegistry()

    with pytest.raises(
        KeyError,
        match="Agent 'missing-agent' is not registered.",
    ):
        registry.unregister("missing-agent")


def test_agent_registry_lists_registered_names() -> None:
    """Registry should list names in registration order."""
    registry = AgentRegistry()
    registry.register(StubAgent(name="planning-agent"))
    registry.register(StubAgent(name="retrieval-agent"))

    assert registry.list_names() == [
        "planning-agent",
        "retrieval-agent",
    ]


def test_agent_registry_iterates_over_agents() -> None:
    """Registry should iterate over registered agent instances."""
    registry = AgentRegistry()
    planning_agent = StubAgent(name="planning-agent")
    retrieval_agent = StubAgent(name="retrieval-agent")

    registry.register(planning_agent)
    registry.register(retrieval_agent)

    assert list(registry) == [
        planning_agent,
        retrieval_agent,
    ]


def test_agent_registry_clears_agents() -> None:
    """Registry should remove every registered agent."""
    registry = AgentRegistry()
    registry.register(StubAgent(name="planning-agent"))
    registry.register(StubAgent(name="retrieval-agent"))

    registry.clear()

    assert len(registry) == 0
    assert registry.list_names() == []


@pytest.mark.parametrize(
    ("operation", "agent_name"),
    [
        ("get", ""),
        ("get", "   "),
        ("unregister", ""),
        ("unregister", "   "),
    ],
)
def test_agent_registry_rejects_empty_names(
    operation: str,
    agent_name: str,
) -> None:
    """Registry operations should reject empty agent names."""
    registry = AgentRegistry()

    method: Callable[[str], Any] = getattr(registry, operation)

    with pytest.raises(
        ValueError,
        match="Agent name must not be empty.",
    ):
        method(agent_name)
