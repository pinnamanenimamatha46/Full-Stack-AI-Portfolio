"""Exceptions raised by shared AI-agent orchestration components."""


class AgentError(Exception):
    """Base exception for all shared AI-agent errors."""


class AgentRegistrationError(AgentError):
    """Raised when an agent cannot be registered."""


class AgentNotFoundError(AgentError):
    """Raised when a requested agent is not registered."""


class AgentExecutionError(AgentError):
    """Raised when an agent fails during execution."""


class AgentOrchestrationError(AgentError):
    """Raised when an orchestration workflow cannot be completed."""
