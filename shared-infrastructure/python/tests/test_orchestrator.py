"""Tests for the shared AI-agent orchestrator."""

import pytest

from full_stack_ai_shared.agents import (
    AgentExecutionContext,
    AgentExecutionError,
    AgentNotFoundError,
    AgentOrchestrator,
    AgentRegistry,
    AgentRequest,
    AgentResult,
    BaseAgent,
)


class EchoAgent(BaseAgent):
    """Agent that returns the submitted task."""

    async def run(self, request: AgentRequest) -> AgentResult:
        """Return a successful result containing the request task."""
        return AgentResult(
            agent_name=self.name,
            success=True,
            output=f"Processed: {request.task}",
            metadata={
                "context": request.context,
            },
        )


class FailingAgent(BaseAgent):
    """Agent that raises an exception during execution."""

    async def run(self, request: AgentRequest) -> AgentResult:
        """Raise an execution failure."""
        raise RuntimeError(f"Unable to process: {request.task}")


class InvalidResultAgent(BaseAgent):
    """Agent that returns a result with an incorrect agent name."""

    async def run(self, request: AgentRequest) -> AgentResult:
        """Return a result associated with another agent."""
        return AgentResult(
            agent_name="different-agent",
            success=True,
            output=request.task,
        )


def test_agent_orchestrator_creates_default_dependencies() -> None:
    """Orchestrator should create default shared dependencies."""
    orchestrator = AgentOrchestrator()

    assert isinstance(orchestrator.registry, AgentRegistry)
    assert isinstance(orchestrator.context, AgentExecutionContext)
    assert len(orchestrator.registry) == 0


def test_agent_orchestrator_uses_supplied_dependencies() -> None:
    """Orchestrator should preserve explicitly supplied dependencies."""
    registry = AgentRegistry()
    context = AgentExecutionContext()

    orchestrator = AgentOrchestrator(
        registry=registry,
        context=context,
    )

    assert orchestrator.registry is registry
    assert orchestrator.context is context


@pytest.mark.asyncio
async def test_agent_orchestrator_executes_registered_agent() -> None:
    """Orchestrator should execute a registered agent."""
    registry = AgentRegistry()
    registry.register(EchoAgent(name="echo-agent"))
    orchestrator = AgentOrchestrator(registry=registry)
    request = AgentRequest(task="Analyze equipment health")

    result = await orchestrator.execute(
        agent_name="echo-agent",
        request=request,
    )

    assert result.agent_name == "echo-agent"
    assert result.success is True
    assert result.output == "Processed: Analyze equipment health"


@pytest.mark.asyncio
async def test_agent_orchestrator_passes_request_context() -> None:
    """Orchestrator should pass request context to the selected agent."""
    registry = AgentRegistry()
    registry.register(EchoAgent(name="echo-agent"))
    orchestrator = AgentOrchestrator(registry=registry)
    request = AgentRequest(
        task="Review maintenance history",
        context={
            "asset_id": "pump-101",
            "priority": "high",
        },
    )

    result = await orchestrator.execute(
        agent_name="echo-agent",
        request=request,
    )

    assert result.metadata["context"] == {
        "asset_id": "pump-101",
        "priority": "high",
    }


@pytest.mark.asyncio
async def test_agent_orchestrator_rejects_unknown_agent() -> None:
    """Orchestrator should raise an error for an unknown agent."""
    orchestrator = AgentOrchestrator()

    with pytest.raises(
        AgentNotFoundError,
        match="Agent 'missing-agent' is not registered.",
    ):
        await orchestrator.execute(
            agent_name="missing-agent",
            request=AgentRequest(task="Analyze asset"),
        )


@pytest.mark.asyncio
async def test_agent_orchestrator_rejects_empty_agent_name() -> None:
    """Orchestrator should reject an empty agent name."""
    orchestrator = AgentOrchestrator()

    with pytest.raises(
        ValueError,
        match="Agent name must not be empty.",
    ):
        await orchestrator.execute(
            agent_name="   ",
            request=AgentRequest(task="Analyze asset"),
        )


@pytest.mark.asyncio
async def test_agent_orchestrator_wraps_agent_failure() -> None:
    """Orchestrator should wrap exceptions raised by agents."""
    registry = AgentRegistry()
    registry.register(FailingAgent(name="failing-agent"))
    orchestrator = AgentOrchestrator(registry=registry)

    with pytest.raises(
        AgentExecutionError,
        match="Agent 'failing-agent' execution failed.",
    ) as exception_info:
        await orchestrator.execute(
            agent_name="failing-agent",
            request=AgentRequest(task="Analyze asset"),
        )

    assert isinstance(exception_info.value.__cause__, RuntimeError)


@pytest.mark.asyncio
async def test_agent_orchestrator_rejects_mismatched_result_name() -> None:
    """Orchestrator should reject results associated with another agent."""
    registry = AgentRegistry()
    registry.register(InvalidResultAgent(name="invalid-result-agent"))
    orchestrator = AgentOrchestrator(registry=registry)

    with pytest.raises(
        AgentExecutionError,
        match=(
            "Agent result name does not match the executed agent: "
            "expected 'invalid-result-agent', received "
            "'different-agent'."
        ),
    ):
        await orchestrator.execute(
            agent_name="invalid-result-agent",
            request=AgentRequest(task="Analyze asset"),
        )


@pytest.mark.asyncio
async def test_agent_orchestrator_executes_task() -> None:
    """Orchestrator should create a request from a task."""
    registry = AgentRegistry()
    registry.register(EchoAgent(name="echo-agent"))
    orchestrator = AgentOrchestrator(registry=registry)

    result = await orchestrator.execute_task(
        agent_name="echo-agent",
        task="Generate maintenance recommendation",
        context={
            "asset_id": "compressor-202",
        },
    )

    assert result.output == "Processed: Generate maintenance recommendation"
    assert result.metadata["context"] == {
        "asset_id": "compressor-202",
    }


@pytest.mark.asyncio
async def test_agent_orchestrator_execute_task_uses_empty_context() -> None:
    """Task execution should use an empty context by default."""
    registry = AgentRegistry()
    registry.register(EchoAgent(name="echo-agent"))
    orchestrator = AgentOrchestrator(registry=registry)

    result = await orchestrator.execute_task(
        agent_name="echo-agent",
        task="Inspect asset",
    )

    assert result.metadata["context"] == {}


@pytest.mark.asyncio
async def test_agent_orchestrator_rejects_empty_task() -> None:
    """Task execution should reject empty task descriptions."""
    registry = AgentRegistry()
    registry.register(EchoAgent(name="echo-agent"))
    orchestrator = AgentOrchestrator(registry=registry)

    with pytest.raises(
        ValueError,
        match="Agent task must not be empty.",
    ):
        await orchestrator.execute_task(
            agent_name="echo-agent",
            task="   ",
        )
