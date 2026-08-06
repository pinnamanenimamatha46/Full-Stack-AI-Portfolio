"""In-memory storage for agent messages and working data."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class MemoryEntry(BaseModel):
    """Single value stored in agent memory."""

    key: str
    value: Any
    metadata: dict[str, Any] = Field(default_factory=dict)


class AgentMemory:
    """Simple reusable in-memory store for agent workflows."""

    def __init__(self) -> None:
        self._entries: dict[str, MemoryEntry] = {}

    def set(
        self,
        key: str,
        value: Any,
        *,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store or replace a memory entry."""

        normalized_key = key.strip()

        if not normalized_key:
            raise ValueError("Memory key cannot be empty.")

        entry = MemoryEntry(
            key=normalized_key,
            value=value,
            metadata=metadata or {},
        )

        self._entries[normalized_key] = entry
        return entry

    def get(self, key: str) -> MemoryEntry | None:
        """Return a memory entry by key."""

        return self._entries.get(key)

    def remove(self, key: str) -> MemoryEntry | None:
        """Remove and return a memory entry."""

        return self._entries.pop(key, None)

    def contains(self, key: str) -> bool:
        """Return whether a key exists in memory."""

        return key in self._entries

    def list_entries(self) -> list[MemoryEntry]:
        """Return all memory entries."""

        return list(self._entries.values())

    def clear(self) -> None:
        """Remove every entry from memory."""

        self._entries.clear()

    def __len__(self) -> int:
        """Return the number of memory entries."""

        return len(self._entries)
