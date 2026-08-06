"""Registry for discovering and retrieving shared AI agents."""

from collections.abc import Iterator

from full_stack_ai_shared.agents.base import BaseAgent


class AgentRegistry:
    """Store and manage named AI-agent instances."""

    def __init__(self) -> None:
        """Initialize an empty agent registry."""
        self._agents: dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        """Register an agent using its unique name."""
        agent_name = agent.name.strip()

        if not agent_name:
            raise ValueError("Agent name must not be empty.")

        if agent_name in self._agents:
            raise ValueError(f"Agent '{agent_name}' is already registered.")

        self._agents[agent_name] = agent

    def get(self, agent_name: str) -> BaseAgent:
        """Return an agent registered under the supplied name."""
        normalized_name = agent_name.strip()

        if not normalized_name:
            raise ValueError("Agent name must not be empty.")

        try:
            return self._agents[normalized_name]
        except KeyError as error:
            raise KeyError(f"Agent '{normalized_name}' is not registered.") from error

    def unregister(self, agent_name: str) -> BaseAgent:
        """Remove and return a registered agent."""
        normalized_name = agent_name.strip()

        if not normalized_name:
            raise ValueError("Agent name must not be empty.")

        try:
            return self._agents.pop(normalized_name)
        except KeyError as error:
            raise KeyError(f"Agent '{normalized_name}' is not registered.") from error

    def contains(self, agent_name: str) -> bool:
        """Return whether an agent name exists in the registry."""
        return agent_name.strip() in self._agents

    def list_names(self) -> list[str]:
        """Return all registered agent names in insertion order."""
        return list(self._agents)

    def clear(self) -> None:
        """Remove all registered agents."""
        self._agents.clear()

    def __len__(self) -> int:
        """Return the number of registered agents."""
        return len(self._agents)

    def __iter__(self) -> Iterator[BaseAgent]:
        """Iterate over registered agents."""
        return iter(self._agents.values())
