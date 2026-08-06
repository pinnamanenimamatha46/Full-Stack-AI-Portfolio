"""Embedding provider abstractions for retrieval workflows."""

from abc import ABC, abstractmethod
from collections.abc import Sequence
from hashlib import sha256
from math import sqrt


class EmbeddingProvider(ABC):
    """Define the interface implemented by embedding providers."""

    @property
    @abstractmethod
    def dimensions(self) -> int:
        """Return the number of values in each embedding vector."""

    @abstractmethod
    def embed_text(self, text: str) -> list[float]:
        """Generate an embedding for one text value."""

    def embed_texts(self, texts: Sequence[str]) -> list[list[float]]:
        """Generate embeddings for multiple text values."""
        return [self.embed_text(text) for text in texts]


class HashEmbeddingProvider(EmbeddingProvider):
    """Generate deterministic local embeddings without an external API."""

    def __init__(self, dimensions: int = 64) -> None:
        """Initialize the deterministic embedding provider."""
        if dimensions <= 0:
            raise ValueError("Embedding dimensions must be greater than zero.")

        self._dimensions = dimensions

    @property
    def dimensions(self) -> int:
        """Return the configured embedding dimensions."""
        return self._dimensions

    def embed_text(self, text: str) -> list[float]:
        """Generate a normalized deterministic embedding."""
        normalized_text = text.strip()

        if not normalized_text:
            raise ValueError("Text to embed must not be empty.")

        vector = [0.0] * self.dimensions
        tokens = normalized_text.lower().split()

        for token in tokens:
            digest = sha256(token.encode("utf-8")).digest()

            for index, byte_value in enumerate(digest):
                vector_index = index % self.dimensions
                direction = 1.0 if byte_value % 2 == 0 else -1.0
                magnitude = 1.0 + (byte_value / 255.0)
                vector[vector_index] += direction * magnitude

        return self._normalize(vector)

    @staticmethod
    def _normalize(vector: list[float]) -> list[float]:
        """Normalize a vector to unit length."""
        magnitude = sqrt(sum(value * value for value in vector))

        if magnitude == 0:
            return vector

        return [value / magnitude for value in vector]
