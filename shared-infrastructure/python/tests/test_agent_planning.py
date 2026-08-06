"""Tests for shared AI-agent planning models."""

import pytest

from full_stack_ai_shared.agents import (
    AgentPlan,
    AgentPlanStep,
    PlanStepStatus,
)


def test_plan_step_defaults() -> None:
    """AgentPlanStep should provide valid default values."""
    step = AgentPlanStep(description="Retrieve maintenance records")

    assert step.description == "Retrieve maintenance records"
    assert step.step_id
    assert step.tool_name is None
    assert step.agent_name is None
    assert step.arguments == {}
    assert step.status == PlanStepStatus.PENDING
    assert step.result is None
    assert step.error is None


def test_plan_step_custom_values() -> None:
    """AgentPlanStep should preserve supplied execution details."""
    step = AgentPlanStep(
        description="Analyze equipment telemetry",
        step_id="step-001",
        tool_name="telemetry-analyzer",
        agent_name="diagnostic-agent",
        arguments={"equipment_id": "EQ-100"},
    )

    assert step.step_id == "step-001"
    assert step.tool_name == "telemetry-analyzer"
    assert step.agent_name == "diagnostic-agent"
    assert step.arguments == {"equipment_id": "EQ-100"}


@pytest.mark.parametrize("description", ["", "   "])
def test_plan_step_rejects_empty_description(description: str) -> None:
    """AgentPlanStep should reject an empty description."""
    with pytest.raises(
        ValueError,
        match="Plan step description must not be empty",
    ):
        AgentPlanStep(description=description)


@pytest.mark.parametrize("step_id", ["", "   "])
def test_plan_step_rejects_empty_step_id(step_id: str) -> None:
    """AgentPlanStep should reject an empty explicit step identifier."""
    with pytest.raises(
        ValueError,
        match="Plan step ID must not be empty",
    ):
        AgentPlanStep(
            description="Validate data",
            step_id=step_id,
        )


@pytest.mark.parametrize("tool_name", ["", "   "])
def test_plan_step_rejects_empty_tool_name(tool_name: str) -> None:
    """AgentPlanStep should reject an empty tool name."""
    with pytest.raises(
        ValueError,
        match="Tool name must not be empty",
    ):
        AgentPlanStep(
            description="Execute tool",
            tool_name=tool_name,
        )


@pytest.mark.parametrize("agent_name", ["", "   "])
def test_plan_step_rejects_empty_agent_name(agent_name: str) -> None:
    """AgentPlanStep should reject an empty agent name."""
    with pytest.raises(
        ValueError,
        match="Agent name must not be empty",
    ):
        AgentPlanStep(
            description="Delegate task",
            agent_name=agent_name,
        )


def test_plan_step_mark_running() -> None:
    """mark_running should update the step status and clear errors."""
    step = AgentPlanStep(description="Run diagnostic")
    step.error = "Previous error"

    step.mark_running()

    assert step.status == PlanStepStatus.RUNNING
    assert step.error is None


def test_plan_step_mark_completed() -> None:
    """mark_completed should store the result and clear errors."""
    step = AgentPlanStep(description="Complete analysis")
    step.error = "Previous error"

    step.mark_completed(result={"risk_level": "low"})

    assert step.status == PlanStepStatus.COMPLETED
    assert step.result == {"risk_level": "low"}
    assert step.error is None


def test_plan_step_mark_failed() -> None:
    """mark_failed should store the failure message."""
    step = AgentPlanStep(description="Process telemetry")

    step.mark_failed("Telemetry service unavailable")

    assert step.status == PlanStepStatus.FAILED
    assert step.error == "Telemetry service unavailable"


@pytest.mark.parametrize("error", ["", "   "])
def test_plan_step_rejects_empty_failure_error(error: str) -> None:
    """mark_failed should reject an empty error message."""
    step = AgentPlanStep(description="Process telemetry")

    with pytest.raises(
        ValueError,
        match="Plan step error must not be empty",
    ):
        step.mark_failed(error)


def test_plan_step_mark_skipped() -> None:
    """mark_skipped should update the step status."""
    step = AgentPlanStep(description="Optional validation")

    step.mark_skipped()

    assert step.status == PlanStepStatus.SKIPPED


def test_agent_plan_defaults() -> None:
    """AgentPlan should provide generated identifiers and empty collections."""
    plan = AgentPlan(objective="Diagnose equipment failure")

    assert plan.objective == "Diagnose equipment failure"
    assert plan.plan_id
    assert plan.steps == []
    assert plan.metadata == {}
    assert plan.is_complete is False
    assert plan.has_failures is False


@pytest.mark.parametrize("objective", ["", "   "])
def test_agent_plan_rejects_empty_objective(objective: str) -> None:
    """AgentPlan should reject an empty objective."""
    with pytest.raises(
        ValueError,
        match="Agent plan objective must not be empty",
    ):
        AgentPlan(objective=objective)


@pytest.mark.parametrize("plan_id", ["", "   "])
def test_agent_plan_rejects_empty_plan_id(plan_id: str) -> None:
    """AgentPlan should reject an empty explicit plan identifier."""
    with pytest.raises(
        ValueError,
        match="Agent plan ID must not be empty",
    ):
        AgentPlan(
            objective="Analyze system health",
            plan_id=plan_id,
        )


def test_agent_plan_add_and_get_step() -> None:
    """AgentPlan should append and retrieve steps by identifier."""
    plan = AgentPlan(objective="Analyze equipment health")
    step = AgentPlanStep(
        description="Retrieve sensor data",
        step_id="step-001",
    )

    plan.add_step(step)

    assert plan.steps == [step]
    assert plan.get_step("step-001") is step


def test_agent_plan_get_step_raises_for_unknown_id() -> None:
    """get_step should raise KeyError for an unknown identifier."""
    plan = AgentPlan(objective="Analyze equipment health")

    with pytest.raises(
        KeyError,
        match="Plan step 'missing-step' was not found",
    ):
        plan.get_step("missing-step")


def test_agent_plan_is_complete_when_all_steps_are_terminal() -> None:
    """A plan should be complete when every step is terminal."""
    completed_step = AgentPlanStep(description="Completed step")
    failed_step = AgentPlanStep(description="Failed step")
    skipped_step = AgentPlanStep(description="Skipped step")

    completed_step.mark_completed()
    failed_step.mark_failed("Execution failed")
    skipped_step.mark_skipped()

    plan = AgentPlan(
        objective="Execute workflow",
        steps=[
            completed_step,
            failed_step,
            skipped_step,
        ],
    )

    assert plan.is_complete is True


def test_agent_plan_is_not_complete_with_pending_step() -> None:
    """A plan should remain incomplete while a step is pending."""
    completed_step = AgentPlanStep(description="Completed step")
    pending_step = AgentPlanStep(description="Pending step")

    completed_step.mark_completed()

    plan = AgentPlan(
        objective="Execute workflow",
        steps=[completed_step, pending_step],
    )

    assert plan.is_complete is False


def test_agent_plan_is_not_complete_without_steps() -> None:
    """An empty plan should not be considered complete."""
    plan = AgentPlan(objective="Execute workflow")

    assert plan.is_complete is False


def test_agent_plan_detects_failures() -> None:
    """has_failures should return true when any step failed."""
    successful_step = AgentPlanStep(description="Successful step")
    failed_step = AgentPlanStep(description="Failed step")

    successful_step.mark_completed()
    failed_step.mark_failed("Agent execution failed")

    plan = AgentPlan(
        objective="Execute workflow",
        steps=[successful_step, failed_step],
    )

    assert plan.has_failures is True
