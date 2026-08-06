"""High-level retrieval-augmented generation service."""

from collections.abc import Mapping
from typing import Any

from full_stack_ai_shared.rag.chunking import TextChunker
from full_stack_ai_shared.rag.models import (
    Document,
    DocumentChunk,
    SearchResult,
)
from full_stack_ai_shared.rag.vector_store import InMemoryVectorStore


class RAGService:
    """Coordinate document chunking, storage, and semantic retrieval."""

    def __init__(
        self,
        *,
        chunker: TextChunker,
        vector_store: InMemoryVectorStore,
    ) -> None:
        """Initialize the retrieval service."""
        self._chunker = chunker
        self._vector_store = vector_store
        self._document_chunks: dict[str, set[str]] = {}

    @property
    def chunker(self) -> TextChunker:
        """Return the configured text chunker."""
        return self._chunker

    @property
    def vector_store(self) -> InMemoryVectorStore:
        """Return the configured vector store."""
        return self._vector_store

    def ingest(self, document: Document) -> list[DocumentChunk]:
        """Chunk and index a document."""
        chunks = self._chunker.chunk(document)
        self._vector_store.add(chunks)

        previous_chunk_ids = self._document_chunks.get(document.document_id, set())
        current_chunk_ids = {chunk.chunk_id for chunk in chunks}

        stale_chunk_ids = previous_chunk_ids - current_chunk_ids
        if stale_chunk_ids:
            self._vector_store.delete(list(stale_chunk_ids))

        self._document_chunks[document.document_id] = current_chunk_ids

        return chunks

    def retrieve(
        self,
        query: str,
        *,
        top_k: int = 5,
        metadata_filter: Mapping[str, Any] | None = None,
    ) -> list[SearchResult]:
        """Retrieve document chunks that are most relevant to a query."""
        if not query.strip():
            raise ValueError("Search query must not be empty.")

        if top_k <= 0:
            raise ValueError("top_k must be greater than zero.")

        return self._vector_store.search(
            query,
            top_k=top_k,
            metadata_filter=metadata_filter,
        )

    def get_chunk(self, chunk_id: str) -> DocumentChunk | None:
        """Return a stored document chunk by its identifier."""
        if not chunk_id.strip():
            raise ValueError("Chunk ID must not be empty.")

        return self._vector_store.get(chunk_id)

    def delete_document(self, document_id: str) -> int:
        """Delete all chunks associated with a source document."""
        if not document_id.strip():
            raise ValueError("Document ID must not be empty.")

        chunk_ids = self._document_chunks.pop(document_id, set())

        if not chunk_ids:
            return 0

        self._vector_store.delete(list(chunk_ids))

        return len(chunk_ids)

    def clear(self) -> None:
        """Remove every indexed chunk from the service."""
        self._vector_store.clear()
        self._document_chunks.clear()
