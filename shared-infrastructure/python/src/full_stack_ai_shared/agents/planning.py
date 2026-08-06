"""Planning models for shared AI-agent workflows."""

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any
from uuid import uuid4


class PlanStepStatus(StrEnum):
    """Represent the execution status of an agent plan step."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass(slots=True)
class AgentPlanStep:
    """Represent one executable step in an agent plan."""

    description: str
    step_id: str = field(default_factory=lambda: str(uuid4()))
    tool_name: str | None = None
    agent_name: str | None = None
    arguments: dict[str, Any] = field(default_factory=dict)
    status: PlanStepStatus = PlanStepStatus.PENDING
    result: Any = None
    error: str | None = None

    def __post_init__(self) -> None:
        """Validate the plan step after initialization."""
        if not self.description.strip():
            raise ValueError("Plan step description must not be empty.")

        if not self.step_id.strip():
            raise ValueError("Plan step ID must not be empty.")

        if self.tool_name is not None and not self.tool_name.strip():
            raise ValueError("Tool name must not be empty.")

        if self.agent_name is not None and not self.agent_name.strip():
            raise ValueError("Agent name must not be empty.")

    def mark_running(self) -> None:
        """Mark the plan step as currently running."""
        self.status = PlanStepStatus.RUNNING
        self.error = None

    def mark_completed(self, result: Any = None) -> None:
        """Mark the plan step as successfully completed."""
        self.status = PlanStepStatus.COMPLETED
        self.result = result
        self.error = None

    def mark_failed(self, error: str) -> None:
        """Mark the plan step as failed."""
        if not error.strip():
            raise ValueError("Plan step error must not be empty.")

        self.status = PlanStepStatus.FAILED
        self.error = error

    def mark_skipped(self) -> None:
        """Mark the plan step as skipped."""
        self.status = PlanStepStatus.SKIPPED


@dataclass(slots=True)
class AgentPlan:
    """Represent an ordered execution plan for an AI agent."""

    objective: str
    plan_id: str = field(default_factory=lambda: str(uuid4()))
    steps: list[AgentPlanStep] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate the agent plan after initialization."""
        if not self.objective.strip():
            raise ValueError("Agent plan objective must not be empty.")

        if not self.plan_id.strip():
            raise ValueError("Agent plan ID must not be empty.")

    @property
    def is_complete(self) -> bool:
        """Return whether every plan step has reached a terminal state."""
        terminal_statuses = {
            PlanStepStatus.COMPLETED,
            PlanStepStatus.FAILED,
            PlanStepStatus.SKIPPED,
        }

        return bool(self.steps) and all(
            step.status in terminal_statuses for step in self.steps
        )

    @property
    def has_failures(self) -> bool:
        """Return whether any plan step has failed."""
        return any(step.status == PlanStepStatus.FAILED for step in self.steps)

    def add_step(self, step: AgentPlanStep) -> None:
        """Append a step to the execution plan."""
        self.steps.append(step)

    def get_step(self, step_id: str) -> AgentPlanStep:
        """Return a plan step by its identifier."""
        for step in self.steps:
            if step.step_id == step_id:
                return step

        raise KeyError(f"Plan step '{step_id}' was not found.")
