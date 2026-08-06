"""Execution context for shared AI-agent orchestration."""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

from full_stack_ai_shared.agents.memory import AgentMemory
from full_stack_ai_shared.tools import ToolRegistry


@dataclass(slots=True)
class AgentExecutionContext:
    """Provide shared services and metadata during agent execution."""

    execution_id: str = field(default_factory=lambda: str(uuid4()))
    tool_registry: ToolRegistry = field(default_factory=ToolRegistry)
    memory: AgentMemory = field(default_factory=AgentMemory)
    rag_service: Any | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate the agent execution context."""
        if not self.execution_id.strip():
            raise ValueError("Execution ID must not be empty.")

    def get_metadata(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """Return a metadata value or the supplied default."""
        return self.metadata.get(key, default)

    def set_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """Add or update execution metadata."""
        if not key.strip():
            raise ValueError("Metadata key must not be empty.")

        self.metadata[key] = value
