"""Data models for shared AI tool execution."""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class ToolDefinition:
    """Describe a tool exposed to an AI agent."""

    name: str
    description: str
    input_schema: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate the tool definition."""
        if not self.name.strip():
            raise ValueError("Tool name must not be empty.")

        if not self.description.strip():
            raise ValueError("Tool description must not be empty.")


@dataclass(slots=True)
class ToolRequest:
    """Represent a request to execute a registered tool."""

    tool_name: str
    arguments: dict[str, Any] = field(default_factory=dict)
    request_id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        """Validate the tool request."""
        if not self.tool_name.strip():
            raise ValueError("Tool name must not be empty.")

        if not self.request_id.strip():
            raise ValueError("Request ID must not be empty.")


@dataclass(slots=True)
class ToolResult:
    """Represent the result of a tool execution."""

    tool_name: str
    success: bool
    output: Any = None
    error: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    request_id: str | None = None

    def __post_init__(self) -> None:
        """Validate the tool result."""
        if not self.tool_name.strip():
            raise ValueError("Tool name must not be empty.")

        if self.success and self.error is not None:
            raise ValueError("Successful tool results must not contain an error.")

        if not self.success and not self.error:
            raise ValueError("Failed tool results must contain an error message.")
