"""Tests for the shared AI tool base class."""

from typing import Any

import pytest

from full_stack_ai_shared.tools.base import BaseTool
from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.models import ToolResult


class EchoTool(BaseTool):
    """Simple tool implementation used for testing."""

    async def execute(
        self,
        arguments: dict[str, Any],
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Return the supplied arguments."""
        return ToolResult(
            tool_name=self.name,
            success=True,
            output=arguments,
            metadata={
                "execution_id": (context.execution_id if context is not None else None),
            },
        )


def test_base_tool_properties() -> None:
    """BaseTool should expose its configured definition."""
    tool = EchoTool(
        name="echo",
        description="Return the supplied arguments.",
        input_schema={
            "type": "object",
            "properties": {
                "message": {"type": "string"},
            },
        },
    )

    assert tool.name == "echo"
    assert tool.description == "Return the supplied arguments."
    assert tool.input_schema == {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
        },
    }


def test_base_tool_definition() -> None:
    """BaseTool should return a complete tool definition."""
    tool = EchoTool(
        name="echo",
        description="Return the supplied arguments.",
    )

    definition = tool.definition

    assert definition.name == "echo"
    assert definition.description == "Return the supplied arguments."
    assert definition.input_schema == {}


def test_base_tool_returns_schema_copy() -> None:
    """Changing a returned schema should not change the tool."""
    tool = EchoTool(
        name="echo",
        description="Return the supplied arguments.",
        input_schema={"type": "object"},
    )

    schema = tool.input_schema
    schema["type"] = "array"

    assert tool.input_schema == {"type": "object"}


@pytest.mark.asyncio
async def test_base_tool_execution() -> None:
    """Concrete tools should implement asynchronous execution."""
    tool = EchoTool(
        name="echo",
        description="Return the supplied arguments.",
    )
    context = ToolContext(execution_id="execution-123")

    result = await tool.execute(
        arguments={"message": "hello"},
        context=context,
    )

    assert result.success is True
    assert result.tool_name == "echo"
    assert result.output == {"message": "hello"}
    assert result.metadata == {"execution_id": "execution-123"}


def test_base_tool_cannot_be_instantiated() -> None:
    """BaseTool should remain abstract."""
    with pytest.raises(TypeError):
        BaseTool(  # type: ignore[abstract]
            name="invalid",
            description="Invalid direct construction.",
        )
