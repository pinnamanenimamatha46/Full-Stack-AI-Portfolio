"""Tests for the shared RAG generation service."""

import pytest

from full_stack_ai_shared.rag import (
    Document,
    HashEmbeddingProvider,
    InMemoryVectorStore,
    RAGGenerationService,
    RAGRequest,
    RAGResponse,
    RAGService,
    TextChunker,
)


def create_generation_service() -> RAGGenerationService:
    """Create a RAG generation service configured for testing."""
    embedding_provider = HashEmbeddingProvider(dimensions=32)

    vector_store = InMemoryVectorStore(
        embedding_provider=embedding_provider,
    )

    rag_service = RAGService(
        chunker=TextChunker(
            chunk_size=100,
            overlap=20,
        ),
        vector_store=vector_store,
    )

    return RAGGenerationService(rag_service=rag_service)


def test_rag_request_defaults() -> None:
    """RAGRequest should provide default retrieval settings."""
    request = RAGRequest(query="How should compressor bearings be maintained?")

    assert request.query == "How should compressor bearings be maintained?"
    assert request.top_k == 5
    assert request.metadata_filter is None


def test_rag_request_accepts_custom_values() -> None:
    """RAGRequest should accept custom retrieval settings."""
    request = RAGRequest(
        query="How should pump seals be inspected?",
        top_k=3,
        metadata_filter={"asset_type": "pump"},
    )

    assert request.query == "How should pump seals be inspected?"
    assert request.top_k == 3
    assert request.metadata_filter == {"asset_type": "pump"}


@pytest.mark.parametrize("query", ["", "   "])
def test_rag_request_rejects_empty_query(query: str) -> None:
    """RAGRequest should reject empty queries."""
    with pytest.raises(
        ValueError,
        match="Query must not be empty.",
    ):
        RAGRequest(query=query)


@pytest.mark.parametrize("top_k", [0, -1])
def test_rag_request_rejects_invalid_top_k(top_k: int) -> None:
    """RAGRequest should reject non-positive result limits."""
    with pytest.raises(
        ValueError,
        match="top_k must be greater than zero.",
    ):
        RAGRequest(
            query="Compressor maintenance",
            top_k=top_k,
        )


def test_rag_response_defaults() -> None:
    """RAGResponse should provide empty result collections by default."""
    response = RAGResponse(
        answer="Generated maintenance answer.",
    )

    assert response.answer == "Generated maintenance answer."
    assert response.search_results == []
    assert response.sources == []
    assert response.metadata == {}


def test_generation_service_exposes_rag_service() -> None:
    """The generation service should expose its retrieval service."""
    generation_service = create_generation_service()

    assert isinstance(generation_service.rag_service, RAGService)


def test_generation_service_returns_no_information_response() -> None:
    """Generation should return a fallback when no chunks are available."""
    generation_service = create_generation_service()

    response = generation_service.generate(
        RAGRequest(
            query="How should compressor bearings be maintained?",
        )
    )

    assert response.answer == "No relevant information found."
    assert response.search_results == []
    assert response.sources == []
    assert response.metadata == {}


def test_generation_service_generates_answer_from_retrieved_context() -> None:
    """Generation should build an answer from retrieved chunks."""
    generation_service = create_generation_service()

    document = Document(
        content=(
            "Compressor bearings should be inspected for vibration, "
            "temperature, and lubrication condition."
        ),
        metadata={
            "asset_type": "compressor",
            "source": "maintenance-manual",
        },
    )

    generation_service.rag_service.ingest(document)

    response = generation_service.generate(
        RAGRequest(
            query="How should compressor bearings be maintained?",
            top_k=1,
        )
    )

    assert isinstance(response, RAGResponse)
    assert response.answer.startswith("Generated answer based on retrieved context:")
    assert document.content in response.answer
    assert len(response.search_results) == 1
    assert response.search_results[0].chunk.document_id == document.document_id
    assert response.sources == [document.document_id]
    assert response.metadata == {"retrieved_chunks": 1}


def test_generation_service_returns_unique_sources() -> None:
    """Generation should return each source document only once."""
    generation_service = create_generation_service()

    document = Document(
        content=(
            "Compressor vibration should be monitored regularly. "
            "Bearing temperature should also be checked frequently. "
            "Lubrication condition should be inspected during maintenance."
        ),
    )

    generation_service.rag_service.ingest(document)

    response = generation_service.generate(
        RAGRequest(
            query="compressor bearing maintenance",
            top_k=5,
        )
    )

    assert response.sources == [document.document_id]


def test_generation_service_filters_context_by_metadata() -> None:
    """Generation should pass metadata filters to retrieval."""
    generation_service = create_generation_service()

    compressor_document = Document(
        content="Inspect compressor bearings and vibration levels.",
        metadata={"asset_type": "compressor"},
    )

    pump_document = Document(
        content="Inspect pump seals and flow conditions.",
        metadata={"asset_type": "pump"},
    )

    generation_service.rag_service.ingest(compressor_document)
    generation_service.rag_service.ingest(pump_document)

    response = generation_service.generate(
        RAGRequest(
            query="inspection procedures",
            top_k=5,
            metadata_filter={"asset_type": "pump"},
        )
    )

    assert len(response.search_results) == 1
    assert response.search_results[0].chunk.document_id == (pump_document.document_id)
    assert response.sources == [pump_document.document_id]
    assert pump_document.content in response.answer
    assert compressor_document.content not in response.answer


def test_generation_service_respects_top_k() -> None:
    """Generation should limit the number of retrieved chunks."""
    generation_service = create_generation_service()

    documents = [
        Document(content="Compressor maintenance documentation."),
        Document(content="Pump maintenance documentation."),
        Document(content="Motor maintenance documentation."),
    ]

    for document in documents:
        generation_service.rag_service.ingest(document)

    response = generation_service.generate(
        RAGRequest(
            query="maintenance documentation",
            top_k=2,
        )
    )

    assert len(response.search_results) == 2
    assert response.metadata["retrieved_chunks"] == 2
