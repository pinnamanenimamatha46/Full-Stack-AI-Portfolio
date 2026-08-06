"""Tests for shared embedding and vector-store components."""

import pytest

from full_stack_ai_shared.rag import (
    DocumentChunk,
    HashEmbeddingProvider,
    InMemoryVectorStore,
)


def create_chunk(
    content: str,
    chunk_index: int,
    *,
    metadata: dict[str, str] | None = None,
    chunk_id: str | None = None,
) -> DocumentChunk:
    """Create a document chunk for vector-store tests."""
    if chunk_id is None:
        return DocumentChunk(
            document_id="document-123",
            content=content,
            chunk_index=chunk_index,
            start_char=0,
            end_char=len(content),
            metadata=metadata or {},
        )

    return DocumentChunk(
        document_id="document-123",
        content=content,
        chunk_index=chunk_index,
        start_char=0,
        end_char=len(content),
        metadata=metadata or {},
        chunk_id=chunk_id,
    )


def test_hash_embedding_provider_returns_expected_dimensions() -> None:
    """Embedding provider should return the configured vector size."""
    provider = HashEmbeddingProvider(dimensions=32)

    embedding = provider.embed_text("Predictive maintenance analysis")

    assert len(embedding) == 32


def test_hash_embedding_provider_is_deterministic() -> None:
    """Identical text should produce identical vectors."""
    provider = HashEmbeddingProvider(dimensions=32)

    first_embedding = provider.embed_text("Equipment vibration")
    second_embedding = provider.embed_text("Equipment vibration")

    assert first_embedding == second_embedding


def test_hash_embedding_provider_rejects_invalid_dimensions() -> None:
    """Embedding dimensions must be greater than zero."""
    with pytest.raises(
        ValueError,
        match="Embedding dimensions must be greater than zero.",
    ):
        HashEmbeddingProvider(dimensions=0)


def test_hash_embedding_provider_rejects_empty_text() -> None:
    """Empty text should not be embedded."""
    provider = HashEmbeddingProvider()

    with pytest.raises(
        ValueError,
        match="Text to embed must not be empty.",
    ):
        provider.embed_text("   ")


def test_vector_store_adds_chunks() -> None:
    """Vector store should add document chunks."""
    store = InMemoryVectorStore(HashEmbeddingProvider())

    chunks = [
        create_chunk("Pump vibration is elevated.", 0),
        create_chunk("Motor temperature is normal.", 1),
    ]

    store.add(chunks)

    assert store.count() == 2


def test_vector_store_returns_chunk_by_id() -> None:
    """Vector store should retrieve a chunk by identifier."""
    store = InMemoryVectorStore(HashEmbeddingProvider())
    chunk = create_chunk(
        "Bearing inspection is required.",
        0,
        chunk_id="chunk-123",
    )

    store.add([chunk])

    stored_chunk = store.get("chunk-123")

    assert stored_chunk == chunk


def test_vector_store_search_returns_ranked_results() -> None:
    """Search should return results ordered by similarity."""
    store = InMemoryVectorStore(HashEmbeddingProvider(dimensions=64))

    vibration_chunk = create_chunk(
        "Pump vibration indicates bearing wear.",
        0,
    )
    finance_chunk = create_chunk(
        "Quarterly finance report and revenue forecast.",
        1,
    )

    store.add([vibration_chunk, finance_chunk])

    results = store.search(
        "pump vibration bearing",
        top_k=2,
    )

    assert len(results) == 2
    assert results[0].score >= results[1].score
    assert results[0].chunk == vibration_chunk


def test_vector_store_limits_search_results() -> None:
    """Search should honor the requested top-k limit."""
    store = InMemoryVectorStore(HashEmbeddingProvider())

    store.add(
        [
            create_chunk("Pump maintenance record.", 0),
            create_chunk("Motor maintenance record.", 1),
            create_chunk("Compressor maintenance record.", 2),
        ]
    )

    results = store.search("maintenance", top_k=2)

    assert len(results) == 2


def test_vector_store_filters_by_metadata() -> None:
    """Search should filter chunks using metadata values."""
    store = InMemoryVectorStore(HashEmbeddingProvider())

    pump_chunk = create_chunk(
        "Pump vibration maintenance record.",
        0,
        metadata={
            "asset_type": "pump",
            "site": "los-angeles",
        },
    )
    motor_chunk = create_chunk(
        "Motor vibration maintenance record.",
        1,
        metadata={
            "asset_type": "motor",
            "site": "los-angeles",
        },
    )

    store.add([pump_chunk, motor_chunk])

    results = store.search(
        "vibration maintenance",
        metadata_filter={"asset_type": "pump"},
    )

    assert len(results) == 1
    assert results[0].chunk == pump_chunk


def test_vector_store_replaces_existing_chunk() -> None:
    """Adding the same chunk ID should replace its stored value."""
    store = InMemoryVectorStore(HashEmbeddingProvider())

    original_chunk = create_chunk(
        "Original maintenance content.",
        0,
        chunk_id="shared-chunk-id",
    )
    updated_chunk = create_chunk(
        "Updated maintenance content.",
        0,
        chunk_id="shared-chunk-id",
    )

    store.add([original_chunk])
    store.add([updated_chunk])

    assert store.count() == 1
    assert store.get("shared-chunk-id") == updated_chunk


def test_vector_store_deletes_chunks() -> None:
    """Vector store should delete chunks by identifier."""
    store = InMemoryVectorStore(HashEmbeddingProvider())

    first_chunk = create_chunk(
        "First chunk.",
        0,
        chunk_id="chunk-1",
    )
    second_chunk = create_chunk(
        "Second chunk.",
        1,
        chunk_id="chunk-2",
    )

    store.add([first_chunk, second_chunk])

    deleted_count = store.delete(["chunk-1"])

    assert deleted_count == 1
    assert store.count() == 1
    assert store.get("chunk-1") is None
    assert store.get("chunk-2") == second_chunk


def test_vector_store_clears_all_chunks() -> None:
    """Vector store should remove every stored chunk."""
    store = InMemoryVectorStore(HashEmbeddingProvider())

    store.add(
        [
            create_chunk("First chunk.", 0),
            create_chunk("Second chunk.", 1),
        ]
    )

    store.clear()

    assert store.count() == 0


@pytest.mark.parametrize(
    ("query", "top_k", "expected_message"),
    [
        ("", 5, "Search query must not be empty."),
        ("   ", 5, "Search query must not be empty."),
        ("maintenance", 0, "top_k must be greater than zero."),
        ("maintenance", -1, "top_k must be greater than zero."),
    ],
)
def test_vector_store_rejects_invalid_search_parameters(
    query: str,
    top_k: int,
    expected_message: str,
) -> None:
    """Search should reject invalid query parameters."""
    store = InMemoryVectorStore(HashEmbeddingProvider())

    with pytest.raises(ValueError, match=expected_message):
        store.search(query, top_k=top_k)
