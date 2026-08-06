"""Core data models for retrieval-augmented generation workflows."""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class Document:
    """Represent a source document before text chunking."""

    content: str
    metadata: dict[str, Any] = field(default_factory=dict)
    document_id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        """Validate the document after initialization."""
        if not self.content.strip():
            raise ValueError("Document content must not be empty.")

        if not self.document_id.strip():
            raise ValueError("Document ID must not be empty.")


@dataclass(slots=True)
class DocumentChunk:
    """Represent a searchable chunk created from a source document."""

    document_id: str
    content: str
    chunk_index: int
    start_char: int
    end_char: int
    metadata: dict[str, Any] = field(default_factory=dict)
    chunk_id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        """Validate the document chunk after initialization."""
        if not self.document_id.strip():
            raise ValueError("Document ID must not be empty.")

        if not self.content.strip():
            raise ValueError("Chunk content must not be empty.")

        if self.chunk_index < 0:
            raise ValueError("Chunk index cannot be negative.")

        if self.start_char < 0:
            raise ValueError("Start character cannot be negative.")

        if self.end_char < self.start_char:
            raise ValueError(
                "End character must be greater than or equal to start character."
            )

        if not self.chunk_id.strip():
            raise ValueError("Chunk ID must not be empty.")


@dataclass(slots=True, frozen=True)
class SearchResult:
    """Represent a vector-search result and its similarity score."""

    chunk: DocumentChunk
    score: float

    def __post_init__(self) -> None:
        """Validate the search result."""
        if not -1.0 <= self.score <= 1.0:
            raise ValueError("Search result score must be between -1.0 and 1.0.")
