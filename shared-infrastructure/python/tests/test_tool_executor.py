"""Tests for the shared AI tool executor."""

from typing import Any

import pytest

from full_stack_ai_shared.tools import (
    BaseTool,
    ToolContext,
    ToolExecutor,
    ToolRegistry,
    ToolRequest,
    ToolResult,
)


class EchoTool(BaseTool):
    """Return the submitted message."""

    def __init__(self) -> None:
        """Initialize the echo tool."""
        super().__init__(
            name="echo",
            description="Return a submitted message.",
            input_schema={
                "type": "object",
                "properties": {
                    "message": {"type": "string"},
                },
                "required": ["message"],
            },
        )

    async def execute(
        self,
        arguments: dict[str, Any],
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Return the message supplied in the arguments."""
        return ToolResult(
            tool_name=self.name,
            success=True,
            output=arguments["message"],
            metadata={
                "execution_id": (context.execution_id if context is not None else None),
            },
        )


class FailingTool(BaseTool):
    """Raise an exception during execution."""

    def __init__(self) -> None:
        """Initialize the failing tool."""
        super().__init__(
            name="failing-tool",
            description="Raise an execution error.",
        )

    async def execute(
        self,
        arguments: dict[str, Any],
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Raise an intentional execution exception."""
        raise RuntimeError("Intentional tool failure.")


@pytest.mark.asyncio
async def test_executor_runs_registered_tool() -> None:
    """Executor should run a registered tool successfully."""
    registry = ToolRegistry()
    registry.register(EchoTool())

    executor = ToolExecutor(registry)
    request = ToolRequest(
        tool_name="echo",
        arguments={"message": "Hello from the executor."},
    )

    result = await executor.execute(request)

    assert result.success is True
    assert result.tool_name == "echo"
    assert result.output == "Hello from the executor."
    assert result.error is None
    assert result.request_id == request.request_id


@pytest.mark.asyncio
async def test_executor_creates_default_context() -> None:
    """Executor should create a context using the request identifier."""
    registry = ToolRegistry()
    registry.register(EchoTool())

    executor = ToolExecutor(registry)
    request = ToolRequest(
        tool_name="echo",
        arguments={"message": "Context test"},
    )

    result = await executor.execute(request)

    assert result.success is True
    assert result.metadata["execution_id"] == request.request_id


@pytest.mark.asyncio
async def test_executor_uses_supplied_context() -> None:
    """Executor should pass a supplied context to the tool."""
    registry = ToolRegistry()
    registry.register(EchoTool())

    executor = ToolExecutor(registry)
    request = ToolRequest(
        tool_name="echo",
        arguments={"message": "Custom context"},
    )
    context = ToolContext(
        execution_id="custom-execution-id",
        metadata={"source": "test"},
    )

    result = await executor.execute(
        request=request,
        context=context,
    )

    assert result.success is True
    assert result.metadata["execution_id"] == "custom-execution-id"
    assert result.request_id == request.request_id


@pytest.mark.asyncio
async def test_executor_returns_failure_for_unknown_tool() -> None:
    """Executor should normalize unknown-tool errors."""
    executor = ToolExecutor(ToolRegistry())
    request = ToolRequest(tool_name="missing-tool")

    result = await executor.execute(request)

    assert result.success is False
    assert result.tool_name == "missing-tool"
    assert result.output is None
    assert result.error is not None
    assert "missing-tool" in result.error
    assert result.request_id == request.request_id


@pytest.mark.asyncio
async def test_executor_returns_failure_for_tool_exception() -> None:
    """Executor should normalize unexpected execution exceptions."""
    registry = ToolRegistry()
    registry.register(FailingTool())

    executor = ToolExecutor(registry)
    request = ToolRequest(tool_name="failing-tool")

    result = await executor.execute(request)

    assert result.success is False
    assert result.tool_name == "failing-tool"
    assert result.error == ("Tool execution failed: Intentional tool failure.")
    assert result.request_id == request.request_id


def test_executor_exposes_registry() -> None:
    """Executor should expose its configured registry."""
    registry = ToolRegistry()
    executor = ToolExecutor(registry)

    assert executor.registry is registry
