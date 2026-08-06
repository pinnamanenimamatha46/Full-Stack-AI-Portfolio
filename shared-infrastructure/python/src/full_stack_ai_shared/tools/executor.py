"""Execution service for registered shared AI tools."""

from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.exceptions import ToolNotFoundError
from full_stack_ai_shared.tools.models import ToolRequest, ToolResult
from full_stack_ai_shared.tools.registry import ToolRegistry


class ToolExecutor:
    """Execute tool requests through a shared tool registry."""

    def __init__(self, registry: ToolRegistry) -> None:
        """Initialize the executor with a tool registry."""
        self._registry = registry

    @property
    def registry(self) -> ToolRegistry:
        """Return the tool registry used by the executor."""
        return self._registry

    async def execute(
        self,
        request: ToolRequest,
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Execute a tool request and return a normalized result."""
        execution_context = context or ToolContext(
            execution_id=request.request_id,
        )

        try:
            result = await self._registry.execute_request(
                request=request,
                context=execution_context,
            )
        except ToolNotFoundError as error:
            return ToolResult(
                tool_name=request.tool_name,
                success=False,
                error=str(error),
                request_id=request.request_id,
            )
        except Exception as error:
            return ToolResult(
                tool_name=request.tool_name,
                success=False,
                error=f"Tool execution failed: {error}",
                request_id=request.request_id,
            )

        result.request_id = request.request_id
        return result
