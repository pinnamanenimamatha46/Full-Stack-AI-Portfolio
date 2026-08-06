"""Shared retrieval-augmented generation abstractions."""

from full_stack_ai_shared.rag.chunking import TextChunker
from full_stack_ai_shared.rag.embeddings import (
    EmbeddingProvider,
    HashEmbeddingProvider,
)
from full_stack_ai_shared.rag.generation import (
    RAGGenerationService,
    RAGRequest,
    RAGResponse,
)
from full_stack_ai_shared.rag.models import (
    Document,
    DocumentChunk,
    SearchResult,
)
from full_stack_ai_shared.rag.service import RAGService
from full_stack_ai_shared.rag.vector_store import InMemoryVectorStore

__all__ = [
    "Document",
    "DocumentChunk",
    "EmbeddingProvider",
    "HashEmbeddingProvider",
    "InMemoryVectorStore",
    "RAGGenerationService",
    "RAGRequest",
    "RAGResponse",
    "RAGService",
    "SearchResult",
    "TextChunker",
]
