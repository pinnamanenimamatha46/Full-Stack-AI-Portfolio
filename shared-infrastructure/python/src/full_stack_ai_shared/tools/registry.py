"""Registry for discovering and executing shared AI tools."""

from typing import Any

from full_stack_ai_shared.tools.base import BaseTool
from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.exceptions import (
    ToolAlreadyRegisteredError,
    ToolNotFoundError,
)
from full_stack_ai_shared.tools.models import (
    ToolDefinition,
    ToolRequest,
    ToolResult,
)


class ToolRegistry:
    """Store, discover, and execute registered AI tools."""

    def __init__(self) -> None:
        """Initialize an empty tool registry."""
        self._tools: dict[str, BaseTool] = {}

    def register(
        self,
        tool: BaseTool,
        *,
        replace: bool = False,
    ) -> None:
        """Register a tool by its unique name."""
        if tool.name in self._tools and not replace:
            raise ToolAlreadyRegisteredError(tool.name)

        self._tools[tool.name] = tool

    def unregister(self, tool_name: str) -> BaseTool:
        """Remove and return a registered tool."""
        try:
            return self._tools.pop(tool_name)
        except KeyError as error:
            raise ToolNotFoundError(tool_name) from error

    def get(self, tool_name: str) -> BaseTool:
        """Return a registered tool by name."""
        try:
            return self._tools[tool_name]
        except KeyError as error:
            raise ToolNotFoundError(tool_name) from error

    def contains(self, tool_name: str) -> bool:
        """Return whether a tool is registered."""
        return tool_name in self._tools

    def list_tools(self) -> list[ToolDefinition]:
        """Return definitions for all registered tools."""
        return [self._tools[name].definition for name in sorted(self._tools)]

    async def execute(
        self,
        tool_name: str,
        arguments: dict[str, Any] | None = None,
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Execute a registered tool by name."""
        request = ToolRequest(
            tool_name=tool_name,
            arguments=arguments or {},
        )

        return await self.execute_request(
            request=request,
            context=context,
        )

    async def execute_request(
        self,
        request: ToolRequest,
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Execute a complete tool request."""
        tool = self.get(request.tool_name)

        result = await tool.execute(
            arguments=request.arguments,
            context=context,
        )

        result.request_id = request.request_id
        return result

    def clear(self) -> None:
        """Remove all registered tools."""
        self._tools.clear()

    def __len__(self) -> int:
        """Return the number of registered tools."""
        return len(self._tools)

    def __contains__(self, tool_name: object) -> bool:
        """Support membership checks using the `in` operator."""
        if not isinstance(tool_name, str):
            return False

        return self.contains(tool_name)
