"""Shared state models for AI-agent execution."""

from datetime import UTC, datetime
from enum import StrEnum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


class AgentStatus(StrEnum):
    """Supported agent execution states."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class AgentState(BaseModel):
    """Mutable execution state shared across agent workflow steps."""

    execution_id: str = Field(default_factory=lambda: str(uuid4()))
    status: AgentStatus = AgentStatus.PENDING
    current_step: str | None = None
    inputs: dict[str, Any] = Field(default_factory=dict)
    outputs: dict[str, Any] = Field(default_factory=dict)
    errors: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    def mark_running(self, step: str | None = None) -> None:
        """Mark the workflow as running."""

        self.status = AgentStatus.RUNNING
        self.current_step = step
        self.updated_at = datetime.now(UTC)

    def mark_completed(self, outputs: dict[str, Any] | None = None) -> None:
        """Mark the workflow as completed."""

        self.status = AgentStatus.COMPLETED
        self.current_step = None

        if outputs:
            self.outputs.update(outputs)

        self.updated_at = datetime.now(UTC)

    def mark_failed(self, error: str) -> None:
        """Mark the workflow as failed and record an error."""

        self.status = AgentStatus.FAILED
        self.current_step = None
        self.errors.append(error)
        self.updated_at = datetime.now(UTC)
