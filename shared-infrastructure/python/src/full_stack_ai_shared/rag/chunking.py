"""Text-chunking utilities for retrieval-augmented generation."""

from full_stack_ai_shared.rag.models import Document, DocumentChunk


class TextChunker:
    """Split documents into overlapping text chunks.

    Args:
        chunk_size: Maximum number of characters in each chunk.
        overlap: Number of characters shared between consecutive chunks.

    Raises:
        ValueError: If the chunk configuration is invalid.
    """

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 100,
    ) -> None:
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than zero.")

        if overlap < 0:
            raise ValueError("overlap cannot be negative.")

        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size.")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, document: Document) -> list[DocumentChunk]:
        """Split a document into overlapping chunks.

        Args:
            document: Document whose content should be split.

        Returns:
            A list of document chunks in their original order.
        """
        content = document.content

        if not content:
            return []

        chunks: list[DocumentChunk] = []
        step_size = self.chunk_size - self.overlap
        start_char = 0
        chunk_index = 0

        while start_char < len(content):
            end_char = min(start_char + self.chunk_size, len(content))
            chunk_content = content[start_char:end_char]

            chunk_metadata = {
                **document.metadata,
                "chunk_index": chunk_index,
                "start_char": start_char,
                "end_char": end_char,
            }

            chunks.append(
                DocumentChunk(
                    document_id=document.document_id,
                    content=chunk_content,
                    chunk_index=chunk_index,
                    start_char=start_char,
                    end_char=end_char,
                    metadata=chunk_metadata,
                )
            )

            if end_char == len(content):
                break

            start_char += step_size
            chunk_index += 1

        return chunks
