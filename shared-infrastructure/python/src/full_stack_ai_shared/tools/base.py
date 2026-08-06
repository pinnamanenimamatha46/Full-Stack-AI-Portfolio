"""Abstract base classes for shared AI tools."""

from abc import ABC, abstractmethod
from typing import Any

from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.models import ToolDefinition, ToolResult


class BaseTool(ABC):
    """Define the common interface implemented by all AI tools."""

    def __init__(
        self,
        name: str,
        description: str,
        input_schema: dict[str, Any] | None = None,
    ) -> None:
        """Initialize the tool definition."""
        self._definition = ToolDefinition(
            name=name,
            description=description,
            input_schema=input_schema or {},
        )

    @property
    def name(self) -> str:
        """Return the tool name."""
        return self._definition.name

    @property
    def description(self) -> str:
        """Return the tool description."""
        return self._definition.description

    @property
    def input_schema(self) -> dict[str, Any]:
        """Return a copy of the tool input schema."""
        return dict(self._definition.input_schema)

    @property
    def definition(self) -> ToolDefinition:
        """Return the tool definition."""
        return ToolDefinition(
            name=self._definition.name,
            description=self._definition.description,
            input_schema=dict(self._definition.input_schema),
        )

    @abstractmethod
    async def execute(
        self,
        arguments: dict[str, Any],
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Execute the tool with validated arguments."""
