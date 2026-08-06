"""Tests for shared retrieval-augmented generation components."""

import pytest

from full_stack_ai_shared.rag import (
    Document,
    DocumentChunk,
    TextChunker,
)


def test_document_defaults() -> None:
    """Document should provide generated identifiers and empty metadata."""
    document = Document(content="Enterprise maintenance document.")

    assert document.document_id
    assert document.content == "Enterprise maintenance document."
    assert document.metadata == {}


def test_document_rejects_empty_content() -> None:
    """Document should reject empty or whitespace-only content."""
    with pytest.raises(
        ValueError,
        match="Document content must not be empty.",
    ):
        Document(content="")


def test_document_chunk_defaults() -> None:
    """DocumentChunk should store chunk location information."""
    chunk = DocumentChunk(
        document_id="document-123",
        content="Chunk content",
        chunk_index=0,
        start_char=0,
        end_char=13,
    )

    assert chunk.document_id == "document-123"
    assert chunk.content == "Chunk content"
    assert chunk.chunk_index == 0
    assert chunk.start_char == 0
    assert chunk.end_char == 13
    assert chunk.metadata == {}


def test_text_chunker_returns_single_chunk_for_short_document() -> None:
    """Text shorter than the configured size should remain one chunk."""
    document = Document(content="Short enterprise document.")

    chunker = TextChunker(
        chunk_size=100,
        overlap=20,
    )

    chunks = chunker.chunk(document)

    assert len(chunks) == 1
    assert chunks[0].document_id == document.document_id
    assert chunks[0].content == document.content
    assert chunks[0].chunk_index == 0
    assert chunks[0].start_char == 0
    assert chunks[0].end_char == len(document.content)


def test_text_chunker_splits_document_with_overlap() -> None:
    """Consecutive chunks should contain the configured overlap."""
    document = Document(content="ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    chunker = TextChunker(
        chunk_size=10,
        overlap=3,
    )

    chunks = chunker.chunk(document)

    assert [chunk.content for chunk in chunks] == [
        "ABCDEFGHIJ",
        "HIJKLMNOPQ",
        "OPQRSTUVWX",
        "VWXYZ",
    ]

    assert [chunk.chunk_index for chunk in chunks] == [0, 1, 2, 3]
    assert [chunk.start_char for chunk in chunks] == [0, 7, 14, 21]
    assert [chunk.end_char for chunk in chunks] == [10, 17, 24, 26]

    assert chunks[0].content[-3:] == chunks[1].content[:3]
    assert chunks[1].content[-3:] == chunks[2].content[:3]
    assert chunks[2].content[-3:] == chunks[3].content[:3]


def test_text_chunker_preserves_document_metadata() -> None:
    """Each chunk should contain the source document metadata."""
    document = Document(
        content="ABCDEFGHIJKLMNO",
        metadata={
            "source": "maintenance-manual.pdf",
            "department": "engineering",
        },
    )

    chunker = TextChunker(
        chunk_size=10,
        overlap=2,
    )

    chunks = chunker.chunk(document)

    assert len(chunks) == 2

    for chunk in chunks:
        assert chunk.metadata["source"] == "maintenance-manual.pdf"
        assert chunk.metadata["department"] == "engineering"
        assert chunk.metadata["chunk_index"] == chunk.chunk_index
        assert chunk.metadata["start_char"] == chunk.start_char
        assert chunk.metadata["end_char"] == chunk.end_char


@pytest.mark.parametrize(
    ("chunk_size", "overlap", "expected_message"),
    [
        (0, 0, "chunk_size must be greater than zero."),
        (-1, 0, "chunk_size must be greater than zero."),
        (100, -1, "overlap cannot be negative."),
        (100, 100, "overlap must be smaller than chunk_size."),
        (100, 101, "overlap must be smaller than chunk_size."),
    ],
)
def test_text_chunker_rejects_invalid_configuration(
    chunk_size: int,
    overlap: int,
    expected_message: str,
) -> None:
    """Invalid chunk settings should raise clear errors."""
    with pytest.raises(ValueError, match=expected_message):
        TextChunker(
            chunk_size=chunk_size,
            overlap=overlap,
        )
