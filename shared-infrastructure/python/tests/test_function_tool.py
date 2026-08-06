"""Tests for function-backed shared AI tools."""

from typing import Any

import pytest

from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.function import FunctionTool


def add_numbers(first: int, second: int) -> int:
    """Add two integers."""
    return first + second


async def multiply_numbers(first: int, second: int) -> int:
    """Multiply two integers asynchronously."""
    return first * second


def raise_tool_error() -> None:
    """Raise a predictable function error."""
    raise RuntimeError("Simulated tool failure.")


def return_asset(asset_id: str) -> dict[str, Any]:
    """Return an industrial asset record."""
    return {
        "asset_id": asset_id,
        "status": "operational",
    }


def test_function_tool_properties() -> None:
    """FunctionTool should expose its configured tool details."""
    tool = FunctionTool(
        name="add_numbers",
        description="Add two integer values.",
        function=add_numbers,
        input_schema={
            "type": "object",
            "properties": {
                "first": {"type": "integer"},
                "second": {"type": "integer"},
            },
            "required": ["first", "second"],
        },
    )

    assert tool.name == "add_numbers"
    assert tool.description == "Add two integer values."
    assert tool.input_schema["type"] == "object"


def test_function_tool_rejects_non_callable() -> None:
    """FunctionTool should reject a non-callable function value."""
    with pytest.raises(
        TypeError,
        match="Tool function must be callable",
    ):
        FunctionTool(
            name="invalid",
            description="Invalid tool.",
            function="not-callable",  # type: ignore[arg-type]
        )


@pytest.mark.asyncio
async def test_function_tool_executes_sync_function() -> None:
    """FunctionTool should execute synchronous Python functions."""
    tool = FunctionTool(
        name="add_numbers",
        description="Add two integer values.",
        function=add_numbers,
    )

    result = await tool.execute(
        {
            "first": 10,
            "second": 15,
        },
    )

    assert result.success is True
    assert result.tool_name == "add_numbers"
    assert result.output == 25
    assert result.error is None


@pytest.mark.asyncio
async def test_function_tool_executes_async_function() -> None:
    """FunctionTool should await asynchronous Python functions."""
    tool = FunctionTool(
        name="multiply_numbers",
        description="Multiply two integer values.",
        function=multiply_numbers,
    )

    result = await tool.execute(
        {
            "first": 6,
            "second": 7,
        },
    )

    assert result.success is True
    assert result.output == 42


@pytest.mark.asyncio
async def test_function_tool_returns_complex_output() -> None:
    """FunctionTool should preserve structured function output."""
    tool = FunctionTool(
        name="return_asset",
        description="Return an industrial asset.",
        function=return_asset,
    )

    result = await tool.execute(
        {
            "asset_id": "PUMP-101",
        },
    )

    assert result.success is True
    assert result.output == {
        "asset_id": "PUMP-101",
        "status": "operational",
    }


@pytest.mark.asyncio
async def test_function_tool_adds_context_metadata() -> None:
    """FunctionTool should include relevant execution context metadata."""
    tool = FunctionTool(
        name="add_numbers",
        description="Add two integer values.",
        function=add_numbers,
    )
    context = ToolContext(
        execution_id="execution-123",
        agent_name="calculation-agent",
        user_id="user-456",
    )

    result = await tool.execute(
        {
            "first": 2,
            "second": 3,
        },
        context=context,
    )

    assert result.success is True
    assert result.metadata == {
        "execution_id": "execution-123",
        "agent_name": "calculation-agent",
        "user_id": "user-456",
    }


@pytest.mark.asyncio
async def test_function_tool_handles_function_failure() -> None:
    """FunctionTool should return a failed result for function errors."""
    tool = FunctionTool(
        name="raise_tool_error",
        description="Raise a predictable error.",
        function=raise_tool_error,
    )

    result = await tool.execute({})

    assert result.success is False
    assert result.output is None
    assert result.error == "Simulated tool failure."
    assert result.metadata == {
        "error_type": "RuntimeError",
    }


@pytest.mark.asyncio
async def test_function_tool_handles_missing_argument() -> None:
    """FunctionTool should return failure when arguments are missing."""
    tool = FunctionTool(
        name="add_numbers",
        description="Add two integer values.",
        function=add_numbers,
    )

    result = await tool.execute(
        {
            "first": 10,
        },
    )

    assert result.success is False
    assert result.error is not None
    assert result.metadata["error_type"] == "TypeError"
