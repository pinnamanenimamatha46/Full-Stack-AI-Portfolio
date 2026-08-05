"""Abstract interfaces and models for LLM providers."""

from abc import ABC, abstractmethod

from pydantic import BaseModel, Field


class LLMMessage(BaseModel):
    """Single chat message sent to an LLM provider."""

    role: str
    content: str


class LLMRequest(BaseModel):
    """Provider-independent LLM request."""

    messages: list[LLMMessage]
    temperature: float = Field(default=0.2, ge=0.0, le=2.0)
    max_tokens: int | None = Field(default=None, gt=0)


class LLMResponse(BaseModel):
    """Provider-independent LLM response."""

    content: str
    model: str
    provider: str
    input_tokens: int | None = None
    output_tokens: int | None = None


class BaseLLMProvider(ABC):
    """Base interface implemented by all LLM providers."""

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Return the provider identifier."""

    @abstractmethod
    async def generate(self, request: LLMRequest) -> LLMResponse:
        """Generate a response for a provider-independent request."""
