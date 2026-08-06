"""Function-based tool implementations and decorators."""

from collections.abc import Awaitable, Callable
from inspect import isawaitable
from typing import Any

from full_stack_ai_shared.tools.base import BaseTool
from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.models import ToolResult

ToolFunction = Callable[..., Any | Awaitable[Any]]


class FunctionTool(BaseTool):
    """Expose a Python function through the shared tool interface."""

    def __init__(
        self,
        name: str,
        description: str,
        function: ToolFunction,
        input_schema: dict[str, Any] | None = None,
    ) -> None:
        """Initialize the function-backed tool."""
        super().__init__(
            name=name,
            description=description,
            input_schema=input_schema,
        )
        self._function = function

    async def execute(
        self,
        arguments: dict[str, Any],
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Execute the wrapped function with the provided arguments."""
        del context

        try:
            output = self._function(**arguments)

            if isawaitable(output):
                output = await output

            return ToolResult(
                tool_name=self.name,
                success=True,
                output=output,
            )
        except Exception as error:
            return ToolResult(
                tool_name=self.name,
                success=False,
                error=str(error),
            )


def tool(
    name: str,
    description: str,
    input_schema: dict[str, Any] | None = None,
) -> Callable[[ToolFunction], FunctionTool]:
    """Convert a Python function into a shared AI tool."""

    def decorator(function: ToolFunction) -> FunctionTool:
        return FunctionTool(
            name=name,
            description=description,
            function=function,
            input_schema=input_schema,
        )

    return decorator
