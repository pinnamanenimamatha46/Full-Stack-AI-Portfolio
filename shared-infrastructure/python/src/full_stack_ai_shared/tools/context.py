"""Execution context for shared AI tools."""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class ToolContext:
    """Provide shared execution data to an AI tool."""

    execution_id: str = field(default_factory=lambda: str(uuid4()))
    agent_name: str | None = None
    user_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate the tool execution context."""
        if not self.execution_id.strip():
            raise ValueError("Execution ID must not be empty.")

        if self.agent_name is not None and not self.agent_name.strip():
            raise ValueError("Agent name must not be empty.")

        if self.user_id is not None and not self.user_id.strip():
            raise ValueError("User ID must not be empty.")

    def get_metadata(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """Return a metadata value or the provided default."""
        return self.metadata.get(key, default)

    def set_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """Add or update a metadata value."""
        if not key.strip():
            raise ValueError("Metadata key must not be empty.")

        self.metadata[key] = value
