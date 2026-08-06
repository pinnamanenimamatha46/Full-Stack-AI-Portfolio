"""Execution context for shared AI-tool invocations."""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class ToolContext:
    """Provide metadata and identity details during tool execution."""

    execution_id: str = field(default_factory=lambda: str(uuid4()))
    agent_name: str | None = None
    user_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate and normalize context values."""
        normalized_execution_id = self.execution_id.strip()

        if not normalized_execution_id:
            raise ValueError("Tool execution ID must not be empty.")

        self.execution_id = normalized_execution_id

        if self.agent_name is not None:
            normalized_agent_name = self.agent_name.strip()

            if not normalized_agent_name:
                raise ValueError("Agent name must not be empty.")

            self.agent_name = normalized_agent_name

        if self.user_id is not None:
            normalized_user_id = self.user_id.strip()

            if not normalized_user_id:
                raise ValueError("User ID must not be empty.")

            self.user_id = normalized_user_id

    def get_metadata(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """Return a metadata value or the supplied default."""
        normalized_key = key.strip()

        if not normalized_key:
            raise ValueError("Metadata key must not be empty.")

        return self.metadata.get(normalized_key, default)

    def set_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """Store a metadata value in the context."""
        normalized_key = key.strip()

        if not normalized_key:
            raise ValueError("Metadata key must not be empty.")

        self.metadata[normalized_key] = value
