"""Tests for the high-level RAG retrieval service."""

import pytest

from full_stack_ai_shared.rag import (
    Document,
    HashEmbeddingProvider,
    InMemoryVectorStore,
    RAGService,
    TextChunker,
)


def create_rag_service(
    *,
    chunk_size: int = 100,
    overlap: int = 20,
) -> RAGService:
    """Create a RAG service configured for testing."""
    embedding_provider = HashEmbeddingProvider(dimensions=32)

    vector_store = InMemoryVectorStore(
        embedding_provider=embedding_provider,
    )

    chunker = TextChunker(
        chunk_size=chunk_size,
        overlap=overlap,
    )

    return RAGService(
        chunker=chunker,
        vector_store=vector_store,
    )


def test_rag_service_exposes_configured_components() -> None:
    """RAGService should expose its chunker and vector store."""
    chunker = TextChunker(
        chunk_size=100,
        overlap=20,
    )

    vector_store = InMemoryVectorStore(
        embedding_provider=HashEmbeddingProvider(dimensions=32),
    )

    service = RAGService(
        chunker=chunker,
        vector_store=vector_store,
    )

    assert service.chunker is chunker
    assert service.vector_store is vector_store


def test_rag_service_ingests_document() -> None:
    """Ingesting a document should chunk and index its content."""
    service = create_rag_service()

    document = Document(
        content="Compressor maintenance requires regular vibration monitoring.",
        metadata={
            "asset_type": "compressor",
            "department": "maintenance",
        },
    )

    chunks = service.ingest(document)

    assert len(chunks) == 1
    assert chunks[0].document_id == document.document_id
    assert chunks[0].content == document.content
    assert chunks[0].metadata["asset_type"] == "compressor"
    assert chunks[0].metadata["department"] == "maintenance"
    assert chunks[0].metadata["chunk_index"] == 0
    assert chunks[0].metadata["start_char"] == 0
    assert chunks[0].metadata["end_char"] == len(document.content)

    stored_chunk = service.get_chunk(chunks[0].chunk_id)

    assert stored_chunk == chunks[0]


def test_rag_service_ingests_multiple_chunks() -> None:
    """Long documents should be split and indexed as multiple chunks."""
    service = create_rag_service(
        chunk_size=40,
        overlap=10,
    )

    document = Document(
        content=(
            "Industrial compressors require vibration monitoring, "
            "temperature analysis, pressure inspection, and scheduled "
            "preventive maintenance."
        ),
    )

    chunks = service.ingest(document)

    assert len(chunks) > 1

    for chunk in chunks:
        assert service.get_chunk(chunk.chunk_id) == chunk


def test_rag_service_retrieves_relevant_chunks() -> None:
    """The service should return chunks relevant to a search query."""
    service = create_rag_service()

    compressor_document = Document(
        content=(
            "Compressor maintenance includes vibration analysis and bearing inspection."
        ),
        metadata={"asset_type": "compressor"},
    )

    pump_document = Document(
        content=(
            "Centrifugal pump maintenance includes seal replacement "
            "and flow inspection."
        ),
        metadata={"asset_type": "pump"},
    )

    service.ingest(compressor_document)
    service.ingest(pump_document)

    results = service.retrieve(
        "compressor vibration maintenance",
        top_k=1,
    )

    assert len(results) == 1
    assert results[0].chunk.document_id == compressor_document.document_id
    assert results[0].chunk.metadata["asset_type"] == "compressor"


def test_rag_service_limits_retrieval_results() -> None:
    """Retrieval should respect the requested result limit."""
    service = create_rag_service()

    documents = [
        Document(content="Compressor maintenance and vibration monitoring."),
        Document(content="Pump maintenance and seal inspection."),
        Document(content="Motor maintenance and temperature monitoring."),
    ]

    for document in documents:
        service.ingest(document)

    results = service.retrieve(
        "maintenance monitoring",
        top_k=2,
    )

    assert len(results) == 2


def test_rag_service_filters_retrieval_by_metadata() -> None:
    """Retrieval should support metadata filtering."""
    service = create_rag_service()

    compressor_document = Document(
        content="Inspect compressor vibration and bearing temperature.",
        metadata={
            "asset_type": "compressor",
            "site": "los-angeles",
        },
    )

    pump_document = Document(
        content="Inspect pump vibration and bearing temperature.",
        metadata={
            "asset_type": "pump",
            "site": "los-angeles",
        },
    )

    service.ingest(compressor_document)
    service.ingest(pump_document)

    results = service.retrieve(
        "bearing vibration inspection",
        top_k=5,
        metadata_filter={"asset_type": "pump"},
    )

    assert len(results) == 1
    assert results[0].chunk.document_id == pump_document.document_id
    assert results[0].chunk.metadata["asset_type"] == "pump"


def test_rag_service_returns_chunk_by_id() -> None:
    """A stored chunk should be retrievable by its identifier."""
    service = create_rag_service()

    document = Document(
        content="Enterprise asset-health documentation.",
    )

    chunks = service.ingest(document)

    stored_chunk = service.get_chunk(chunks[0].chunk_id)

    assert stored_chunk == chunks[0]


def test_rag_service_returns_none_for_unknown_chunk() -> None:
    """An unknown chunk identifier should return None."""
    service = create_rag_service()

    assert service.get_chunk("unknown-chunk-id") is None


def test_rag_service_deletes_document_chunks() -> None:
    """Deleting a document should remove all of its stored chunks."""
    service = create_rag_service(
        chunk_size=40,
        overlap=10,
    )

    document = Document(
        content=(
            "Compressor vibration monitoring identifies bearing wear. "
            "Temperature monitoring identifies lubrication problems."
        ),
    )

    chunks = service.ingest(document)

    deleted_count = service.delete_document(document.document_id)

    assert deleted_count == len(chunks)

    for chunk in chunks:
        assert service.get_chunk(chunk.chunk_id) is None


def test_rag_service_delete_document_preserves_other_documents() -> None:
    """Deleting one document should not remove unrelated chunks."""
    service = create_rag_service()

    first_document = Document(
        content="Compressor vibration monitoring procedures.",
    )

    second_document = Document(
        content="Pump seal inspection procedures.",
    )

    first_chunks = service.ingest(first_document)
    second_chunks = service.ingest(second_document)

    deleted_count = service.delete_document(first_document.document_id)

    assert deleted_count == len(first_chunks)
    assert service.get_chunk(first_chunks[0].chunk_id) is None
    assert service.get_chunk(second_chunks[0].chunk_id) == second_chunks[0]


def test_rag_service_delete_unknown_document_returns_zero() -> None:
    """Deleting an unknown document should report no deleted chunks."""
    service = create_rag_service()

    deleted_count = service.delete_document("unknown-document-id")

    assert deleted_count == 0


def test_rag_service_reingests_existing_document() -> None:
    """Reingesting a document should replace its previous chunks."""
    service = create_rag_service(
        chunk_size=50,
        overlap=10,
    )

    original_document = Document(
        document_id="maintenance-document",
        content=(
            "Original compressor maintenance instructions for vibration inspection."
        ),
    )

    original_chunks = service.ingest(original_document)

    updated_document = Document(
        document_id="maintenance-document",
        content=(
            "Updated compressor maintenance instructions for temperature monitoring."
        ),
    )

    updated_chunks = service.ingest(updated_document)

    for chunk in original_chunks:
        assert service.get_chunk(chunk.chunk_id) is None

    for chunk in updated_chunks:
        assert service.get_chunk(chunk.chunk_id) == chunk


def test_rag_service_clear_removes_all_chunks() -> None:
    """Clearing the service should remove every indexed chunk."""
    service = create_rag_service()

    first_chunks = service.ingest(
        Document(content="Compressor maintenance documentation.")
    )

    second_chunks = service.ingest(Document(content="Pump maintenance documentation."))

    service.clear()

    for chunk in first_chunks + second_chunks:
        assert service.get_chunk(chunk.chunk_id) is None


@pytest.mark.parametrize(
    ("query", "error_message"),
    [
        ("", "Search query must not be empty."),
        ("   ", "Search query must not be empty."),
    ],
)
def test_rag_service_rejects_empty_query(
    query: str,
    error_message: str,
) -> None:
    """Retrieval should reject empty search queries."""
    service = create_rag_service()

    with pytest.raises(ValueError, match=error_message):
        service.retrieve(query)


@pytest.mark.parametrize("top_k", [0, -1])
def test_rag_service_rejects_invalid_top_k(top_k: int) -> None:
    """Retrieval should reject non-positive result limits."""
    service = create_rag_service()

    with pytest.raises(
        ValueError,
        match="top_k must be greater than zero.",
    ):
        service.retrieve(
            "compressor maintenance",
            top_k=top_k,
        )


@pytest.mark.parametrize(
    ("chunk_id", "error_message"),
    [
        ("", "Chunk ID must not be empty."),
        ("   ", "Chunk ID must not be empty."),
    ],
)
def test_rag_service_rejects_empty_chunk_id(
    chunk_id: str,
    error_message: str,
) -> None:
    """Chunk lookup should reject empty identifiers."""
    service = create_rag_service()

    with pytest.raises(ValueError, match=error_message):
        service.get_chunk(chunk_id)


@pytest.mark.parametrize(
    ("document_id", "error_message"),
    [
        ("", "Document ID must not be empty."),
        ("   ", "Document ID must not be empty."),
    ],
)
def test_rag_service_rejects_empty_document_id(
    document_id: str,
    error_message: str,
) -> None:
    """Document deletion should reject empty identifiers."""
    service = create_rag_service()

    with pytest.raises(ValueError, match=error_message):
        service.delete_document(document_id)
