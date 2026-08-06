"""
Shared AI agent abstractions.

This package exposes the public API for the shared AI agent framework,
including base agent interfaces, execution state, and agent memory.
"""

from full_stack_ai_shared.agents.base import (
    AgentRequest,
    AgentResult,
    BaseAgent,
)
from full_stack_ai_shared.agents.memory import (
    AgentMemory,
    MemoryEntry,
)
from full_stack_ai_shared.agents.state import (
    AgentState,
    AgentStatus,
)

__all__ = [
    "AgentMemory",
    "AgentRequest",
    "AgentResult",
    "AgentState",
    "AgentStatus",
    "BaseAgent",
    "MemoryEntry",
]
