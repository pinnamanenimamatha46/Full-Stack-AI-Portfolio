"""Function-backed implementation of the shared AI tool interface."""

import inspect
from collections.abc import Awaitable, Callable
from typing import Any

from full_stack_ai_shared.tools.base import BaseTool
from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.models import ToolResult

ToolFunction = Callable[..., Any]
AsyncToolFunction = Callable[..., Awaitable[Any]]


class FunctionTool(BaseTool):
    """Expose a synchronous or asynchronous Python function as an AI tool."""

    def __init__(
        self,
        name: str,
        description: str,
        function: ToolFunction | AsyncToolFunction,
        input_schema: dict[str, Any] | None = None,
    ) -> None:
        """Initialize the function-backed tool."""
        if not callable(function):
            raise TypeError("Tool function must be callable.")

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
        """Execute the wrapped function and return a standardized result."""
        try:
            output = self._function(**arguments)

            if inspect.isawaitable(output):
                output = await output

            metadata: dict[str, Any] = {}

            if context is not None:
                metadata["execution_id"] = context.execution_id

                if context.agent_name is not None:
                    metadata["agent_name"] = context.agent_name

                if context.user_id is not None:
                    metadata["user_id"] = context.user_id

            return ToolResult(
                tool_name=self.name,
                success=True,
                output=output,
                metadata=metadata,
            )
        except Exception as error:
            return ToolResult(
                tool_name=self.name,
                success=False,
                error=str(error),
                metadata={
                    "error_type": type(error).__name__,
                },
            )
