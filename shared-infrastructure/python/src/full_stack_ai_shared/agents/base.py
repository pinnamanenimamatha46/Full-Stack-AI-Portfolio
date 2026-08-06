"""Base abstractions for reusable AI agents."""

from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    """Input passed to an AI agent."""

    task: str = Field(min_length=1)
    context: dict[str, Any] = Field(default_factory=dict)


class AgentResult(BaseModel):
    """Standard result returned by an AI agent."""

    agent_name: str
    success: bool
    output: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class BaseAgent(ABC):
    """Base interface implemented by all portfolio agents."""

    def __init__(self, name: str) -> None:
        normalized_name = name.strip()

        if not normalized_name:
            raise ValueError("Agent name cannot be empty.")

        self._name = normalized_name

    @property
    def name(self) -> str:
        """Return the agent name."""

        return self._name

    @abstractmethod
    async def run(self, request: AgentRequest) -> AgentResult:
        """Execute an agent task and return a standard result."""
