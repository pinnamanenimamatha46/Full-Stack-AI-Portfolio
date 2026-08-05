"""Factory for constructing LLM providers."""

from collections.abc import Callable
from typing import Any

from full_stack_ai_shared.llm.base import BaseLLMProvider


class UnsupportedLLMProviderError(ValueError):
    """Raised when a requested LLM provider is not registered."""


ProviderFactory = Callable[..., BaseLLMProvider]

_PROVIDER_REGISTRY: dict[str, ProviderFactory] = {}


def register_llm_provider(
    name: str,
    factory: ProviderFactory,
) -> None:
    """Register an LLM provider factory."""

    normalized_name = name.strip().lower()

    if not normalized_name:
        raise ValueError("Provider name cannot be empty.")

    _PROVIDER_REGISTRY[normalized_name] = factory


def create_llm_provider(
    name: str,
    **kwargs: Any,
) -> BaseLLMProvider:
    """Create a registered LLM provider."""

    normalized_name = name.strip().lower()

    try:
        factory = _PROVIDER_REGISTRY[normalized_name]
    except KeyError as exc:
        raise UnsupportedLLMProviderError(f"Unsupported LLM provider: {name}") from exc

    return factory(**kwargs)


def list_llm_providers() -> tuple[str, ...]:
    """Return registered LLM provider names."""

    return tuple(sorted(_PROVIDER_REGISTRY))


def clear_llm_provider_registry() -> None:
    """Clear the provider registry.

    Intended primarily for isolated tests.
    """

    _PROVIDER_REGISTRY.clear()
