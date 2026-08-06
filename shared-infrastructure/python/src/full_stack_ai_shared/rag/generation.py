"""Shared retrieval-augmented generation service."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

from full_stack_ai_shared.rag.models import SearchResult
from full_stack_ai_shared.rag.service import RAGService


@dataclass(slots=True)
class RAGRequest:
    """Represent a retrieval-augmented generation request."""

    query: str
    top_k: int = 5
    metadata_filter: Mapping[str, Any] | None = None

    def __post_init__(self) -> None:
        """Validate the request."""
        if not self.query.strip():
            raise ValueError("Query must not be empty.")

        if self.top_k <= 0:
            raise ValueError("top_k must be greater than zero.")


@dataclass(slots=True)
class RAGResponse:
    """Represent the response returned by the RAG generation service."""

    answer: str
    search_results: list[SearchResult] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


class RAGGenerationService:
    """Generate answers from retrieved document context."""

    def __init__(self, rag_service: RAGService) -> None:
        """Initialize the generation service."""
        self._rag_service = rag_service

    @property
    def rag_service(self) -> RAGService:
        """Return the configured retrieval service."""
        return self._rag_service

    def generate(self, request: RAGRequest) -> RAGResponse:
        """Generate an answer using retrieved document chunks."""
        search_results = self._rag_service.retrieve(
            request.query,
            top_k=request.top_k,
            metadata_filter=request.metadata_filter,
        )

        if not search_results:
            return RAGResponse(
                answer="No relevant information found.",
                search_results=[],
                sources=[],
            )

        context = "\n\n".join(result.chunk.content for result in search_results)

        answer = f"Generated answer based on retrieved context:\n\n{context}"

        sources = list({result.chunk.document_id for result in search_results})

        return RAGResponse(
            answer=answer,
            search_results=search_results,
            sources=sources,
            metadata={
                "retrieved_chunks": len(search_results),
            },
        )
