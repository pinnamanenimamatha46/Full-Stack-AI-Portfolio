"""Orchestration service for executing registered AI agents."""

from full_stack_ai_shared.agents.base import AgentRequest, AgentResult
from full_stack_ai_shared.agents.context import AgentExecutionContext
from full_stack_ai_shared.agents.exceptions import (
    AgentExecutionError,
    AgentNotFoundError,
)
from full_stack_ai_shared.agents.registry import AgentRegistry


class AgentOrchestrator:
    """Coordinate execution of registered AI agents."""

    def __init__(
        self,
        registry: AgentRegistry | None = None,
        context: AgentExecutionContext | None = None,
    ) -> None:
        """Initialize the orchestrator with shared agent services."""
        self.registry = registry if registry is not None else AgentRegistry()
        self.context = context if context is not None else AgentExecutionContext()

    async def execute(
        self,
        agent_name: str,
        request: AgentRequest,
    ) -> AgentResult:
        """Execute a registered agent using the supplied request."""
        normalized_name = agent_name.strip()

        if not normalized_name:
            raise ValueError("Agent name must not be empty.")

        try:
            agent = self.registry.get(normalized_name)
        except KeyError as error:
            raise AgentNotFoundError(
                f"Agent '{normalized_name}' is not registered."
            ) from error

        try:
            result = await agent.run(request)
        except Exception as error:
            raise AgentExecutionError(
                f"Agent '{normalized_name}' execution failed."
            ) from error

        if result.agent_name != normalized_name:
            raise AgentExecutionError(
                "Agent result name does not match the executed agent: "
                f"expected '{normalized_name}', received "
                f"'{result.agent_name}'."
            )

        return result

    async def execute_task(
        self,
        agent_name: str,
        task: str,
        context: dict[str, object] | None = None,
    ) -> AgentResult:
        """Create an agent request and execute the selected agent."""
        if not task.strip():
            raise ValueError("Agent task must not be empty.")

        request = AgentRequest(
            task=task,
            context=context if context is not None else {},
        )

        return await self.execute(agent_name, request)
