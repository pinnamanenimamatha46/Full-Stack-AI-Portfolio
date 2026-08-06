"""Tests for the shared AI tool registry."""

import pytest

from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.exceptions import (
    ToolAlreadyRegisteredError,
    ToolNotFoundError,
)
from full_stack_ai_shared.tools.function import FunctionTool
from full_stack_ai_shared.tools.models import ToolRequest
from full_stack_ai_shared.tools.registry import ToolRegistry


def add_numbers(first: int, second: int) -> int:
    """Add two integers."""
    return first + second


def subtract_numbers(first: int, second: int) -> int:
    """Subtract the second integer from the first."""
    return first - second


def create_add_tool() -> FunctionTool:
    """Create a reusable addition tool."""
    return FunctionTool(
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


def test_tool_registry_defaults() -> None:
    """ToolRegistry should start empty."""
    registry = ToolRegistry()

    assert len(registry) == 0
    assert registry.list_tools() == []


def test_tool_registry_registers_tool() -> None:
    """ToolRegistry should register a tool by name."""
    registry = ToolRegistry()
    tool = create_add_tool()

    registry.register(tool)

    assert len(registry) == 1
    assert registry.contains("add_numbers") is True
    assert "add_numbers" in registry
    assert registry.get("add_numbers") is tool


def test_tool_registry_rejects_duplicate_tool() -> None:
    """ToolRegistry should reject duplicate names by default."""
    registry = ToolRegistry()
    registry.register(create_add_tool())

    with pytest.raises(
        ToolAlreadyRegisteredError,
        match="Tool 'add_numbers' is already registered",
    ):
        registry.register(create_add_tool())


def test_tool_registry_replaces_existing_tool() -> None:
    """ToolRegistry should replace a tool when explicitly requested."""
    registry = ToolRegistry()
    original = create_add_tool()
    replacement = FunctionTool(
        name="add_numbers",
        description="Subtract two integer values.",
        function=subtract_numbers,
    )

    registry.register(original)
    registry.register(replacement, replace=True)

    assert len(registry) == 1
    assert registry.get("add_numbers") is replacement


def test_tool_registry_gets_missing_tool() -> None:
    """ToolRegistry should raise when a requested tool is absent."""
    registry = ToolRegistry()

    with pytest.raises(
        ToolNotFoundError,
        match="Tool 'missing_tool' is not registered",
    ):
        registry.get("missing_tool")


def test_tool_registry_unregisters_tool() -> None:
    """ToolRegistry should remove and return a registered tool."""
    registry = ToolRegistry()
    tool = create_add_tool()
    registry.register(tool)

    removed_tool = registry.unregister("add_numbers")

    assert removed_tool is tool
    assert len(registry) == 0
    assert "add_numbers" not in registry


def test_tool_registry_unregisters_missing_tool() -> None:
    """ToolRegistry should raise when removing an absent tool."""
    registry = ToolRegistry()

    with pytest.raises(
        ToolNotFoundError,
        match="Tool 'missing_tool' is not registered",
    ):
        registry.unregister("missing_tool")


def test_tool_registry_lists_sorted_definitions() -> None:
    """ToolRegistry should return sorted tool definitions."""
    registry = ToolRegistry()
    registry.register(
        FunctionTool(
            name="subtract_numbers",
            description="Subtract two integer values.",
            function=subtract_numbers,
        ),
    )
    registry.register(create_add_tool())

    definitions = registry.list_tools()

    assert [definition.name for definition in definitions] == [
        "add_numbers",
        "subtract_numbers",
    ]
    assert definitions[0].description == "Add two integer values."
    assert definitions[0].input_schema["type"] == "object"


@pytest.mark.asyncio
async def test_tool_registry_executes_tool() -> None:
    """ToolRegistry should execute a registered tool."""
    registry = ToolRegistry()
    registry.register(create_add_tool())

    result = await registry.execute(
        "add_numbers",
        {
            "first": 20,
            "second": 22,
        },
    )

    assert result.success is True
    assert result.tool_name == "add_numbers"
    assert result.output == 42


@pytest.mark.asyncio
async def test_tool_registry_executes_with_context() -> None:
    """ToolRegistry should pass execution context to the tool."""
    registry = ToolRegistry()
    registry.register(create_add_tool())
    context = ToolContext(
        execution_id="execution-123",
        agent_name="math-agent",
    )

    result = await registry.execute(
        "add_numbers",
        {
            "first": 2,
            "second": 3,
        },
        context=context,
    )

    assert result.success is True
    assert result.output == 5
    assert result.metadata == {
        "execution_id": "execution-123",
        "agent_name": "math-agent",
    }


@pytest.mark.asyncio
async def test_tool_registry_executes_with_default_arguments() -> None:
    """ToolRegistry should use empty arguments when none are supplied."""

    def return_status() -> str:
        return "operational"

    registry = ToolRegistry()
    registry.register(
        FunctionTool(
            name="return_status",
            description="Return the current status.",
            function=return_status,
        ),
    )

    result = await registry.execute("return_status")

    assert result.success is True
    assert result.output == "operational"


@pytest.mark.asyncio
async def test_tool_registry_executes_missing_tool() -> None:
    """ToolRegistry should raise when executing an absent tool."""
    registry = ToolRegistry()

    with pytest.raises(
        ToolNotFoundError,
        match="Tool 'missing_tool' is not registered",
    ):
        await registry.execute("missing_tool")


def test_tool_registry_clears_tools() -> None:
    """ToolRegistry should remove all registered tools."""
    registry = ToolRegistry()
    registry.register(create_add_tool())
    registry.register(
        FunctionTool(
            name="subtract_numbers",
            description="Subtract two integer values.",
            function=subtract_numbers,
        ),
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list_tools() == []


@pytest.mark.asyncio
async def test_tool_registry_executes_tool_request() -> None:
    """ToolRegistry should execute a complete ToolRequest."""
    registry = ToolRegistry()
    registry.register(create_add_tool())

    request = ToolRequest(
        tool_name="add_numbers",
        arguments={
            "first": 19,
            "second": 23,
        },
        request_id="request-123",
    )

    result = await registry.execute_request(request)

    assert result.success is True
    assert result.output == 42
    assert result.request_id == "request-123"


@pytest.mark.asyncio
async def test_tool_registry_generated_request_id_is_preserved() -> None:
    """Name-based execution should preserve its generated request ID."""
    registry = ToolRegistry()
    registry.register(create_add_tool())

    result = await registry.execute(
        "add_numbers",
        {
            "first": 10,
            "second": 5,
        },
    )

    assert result.success is True
    assert result.output == 15
    assert result.request_id is not None
