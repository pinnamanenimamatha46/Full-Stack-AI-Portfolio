"""Vector-store abstractions and in-memory implementation."""

from abc import ABC, abstractmethod
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from math import sqrt
from typing import Any

from full_stack_ai_shared.rag.embeddings import EmbeddingProvider
from full_stack_ai_shared.rag.models import DocumentChunk, SearchResult


class VectorStore(ABC):
    """Define the interface implemented by vector stores."""

    @abstractmethod
    def add(self, chunks: Sequence[DocumentChunk]) -> None:
        """Add document chunks to the vector store."""

    @abstractmethod
    def search(
        self,
        query: str,
        *,
        top_k: int = 5,
        metadata_filter: Mapping[str, Any] | None = None,
    ) -> list[SearchResult]:
        """Search for chunks similar to a query."""

    @abstractmethod
    def delete(self, chunk_ids: Sequence[str]) -> int:
        """Delete chunks and return the number removed."""

    @abstractmethod
    def clear(self) -> None:
        """Remove all stored chunks."""

    @abstractmethod
    def count(self) -> int:
        """Return the number of stored chunks."""


@dataclass(slots=True)
class _StoredVector:
    """Store a document chunk and its embedding."""

    chunk: DocumentChunk
    embedding: list[float]


class InMemoryVectorStore(VectorStore):
    """Store embeddings in memory and perform cosine-similarity search."""

    def __init__(self, embedding_provider: EmbeddingProvider) -> None:
        """Initialize the in-memory vector store."""
        self._embedding_provider = embedding_provider
        self._vectors: dict[str, _StoredVector] = {}

    def add(self, chunks: Sequence[DocumentChunk]) -> None:
        """Add or replace document chunks in the vector store."""
        if not chunks:
            return

        embeddings = self._embedding_provider.embed_texts(
            [chunk.content for chunk in chunks]
        )

        for chunk, embedding in zip(chunks, embeddings, strict=True):
            self._validate_embedding(embedding)

            self._vectors[chunk.chunk_id] = _StoredVector(
                chunk=chunk,
                embedding=embedding,
            )

    def search(
        self,
        query: str,
        *,
        top_k: int = 5,
        metadata_filter: Mapping[str, Any] | None = None,
    ) -> list[SearchResult]:
        """Search stored chunks using cosine similarity."""
        if not query.strip():
            raise ValueError("Search query must not be empty.")

        if top_k <= 0:
            raise ValueError("top_k must be greater than zero.")

        query_embedding = self._embedding_provider.embed_text(query)
        self._validate_embedding(query_embedding)

        results: list[SearchResult] = []

        for stored_vector in self._vectors.values():
            if not self._matches_metadata(
                stored_vector.chunk,
                metadata_filter,
            ):
                continue

            score = self._cosine_similarity(
                query_embedding,
                stored_vector.embedding,
            )

            results.append(
                SearchResult(
                    chunk=stored_vector.chunk,
                    score=score,
                )
            )

        results.sort(
            key=lambda result: result.score,
            reverse=True,
        )

        return results[:top_k]

    def delete(self, chunk_ids: Sequence[str]) -> int:
        """Delete chunks and return the number removed."""
        deleted_count = 0

        for chunk_id in set(chunk_ids):
            if self._vectors.pop(chunk_id, None) is not None:
                deleted_count += 1

        return deleted_count

    def clear(self) -> None:
        """Remove all stored vectors."""
        self._vectors.clear()

    def count(self) -> int:
        """Return the number of stored vectors."""
        return len(self._vectors)

    def get(self, chunk_id: str) -> DocumentChunk | None:
        """Return a stored chunk by its identifier."""
        stored_vector = self._vectors.get(chunk_id)

        if stored_vector is None:
            return None

        return stored_vector.chunk

    def _validate_embedding(
        self,
        embedding: Sequence[float],
    ) -> None:
        """Validate that an embedding matches provider dimensions."""
        if len(embedding) != self._embedding_provider.dimensions:
            raise ValueError(
                "Embedding dimensions do not match the configured provider."
            )

    @staticmethod
    def _matches_metadata(
        chunk: DocumentChunk,
        metadata_filter: Mapping[str, Any] | None,
    ) -> bool:
        """Return whether a chunk matches requested metadata."""
        if metadata_filter is None:
            return True

        return all(
            chunk.metadata.get(key) == expected_value
            for key, expected_value in metadata_filter.items()
        )

    @staticmethod
    def _cosine_similarity(
        first: Sequence[float],
        second: Sequence[float],
    ) -> float:
        """Calculate cosine similarity between two vectors."""
        if len(first) != len(second):
            raise ValueError("Vectors must have matching dimensions.")

        dot_product = sum(
            first_value * second_value
            for first_value, second_value in zip(
                first,
                second,
                strict=True,
            )
        )
        first_magnitude = sqrt(sum(value * value for value in first))
        second_magnitude = sqrt(sum(value * value for value in second))

        if first_magnitude == 0 or second_magnitude == 0:
            return 0.0

        score = dot_product / (first_magnitude * second_magnitude)

        return max(-1.0, min(1.0, score))
