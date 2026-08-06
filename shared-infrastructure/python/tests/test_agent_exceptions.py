"""Tests for shared AI-agent exceptions."""

import pytest

from full_stack_ai_shared.agents import (
    AgentError,
    AgentExecutionError,
    AgentNotFoundError,
    AgentOrchestrationError,
    AgentRegistrationError,
)


@pytest.mark.parametrize(
    "exception_type",
    [
        AgentRegistrationError,
        AgentNotFoundError,
        AgentExecutionError,
        AgentOrchestrationError,
    ],
)
def test_agent_exceptions_inherit_from_agent_error(
    exception_type: type[AgentError],
) -> None:
    """Specialized agent exceptions should inherit from AgentError."""
    error = exception_type("Agent operation failed.")

    assert isinstance(error, AgentError)
    assert isinstance(error, Exception)


@pytest.mark.parametrize(
    ("exception_type", "message"),
    [
        (
            AgentError,
            "Generic agent failure.",
        ),
        (
            AgentRegistrationError,
            "Agent registration failed.",
        ),
        (
            AgentNotFoundError,
            "Requested agent was not found.",
        ),
        (
            AgentExecutionError,
            "Agent execution failed.",
        ),
        (
            AgentOrchestrationError,
            "Agent orchestration failed.",
        ),
    ],
)
def test_agent_exceptions_preserve_messages(
    exception_type: type[AgentError],
    message: str,
) -> None:
    """Agent exceptions should preserve their supplied messages."""
    error = exception_type(message)

    assert str(error) == message


def test_agent_error_can_be_raised_and_caught() -> None:
    """AgentError should behave like a normal exception."""
    with pytest.raises(
        AgentError,
        match="Shared agent failure.",
    ):
        raise AgentError("Shared agent failure.")


def test_specialized_exception_can_be_caught_as_agent_error() -> None:
    """Specialized exceptions should be catchable as AgentError."""
    with pytest.raises(
        AgentError,
        match="Agent could not be executed.",
    ):
        raise AgentExecutionError("Agent could not be executed.")
