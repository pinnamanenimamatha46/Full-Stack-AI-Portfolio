"""Tests for shared LLM abstractions."""

import pytest

from full_stack_ai_shared.llm import (
    BaseLLMProvider,
    LLMMessage,
    LLMRequest,
    LLMResponse,
    UnsupportedLLMProviderError,
    clear_llm_provider_registry,
    create_llm_provider,
    list_llm_providers,
    register_llm_provider,
)


class FakeLLMProvider(BaseLLMProvider):
    """Test provider for validating the shared interface."""

    @property
    def provider_name(self) -> str:
        return "fake"

    async def generate(self, request: LLMRequest) -> LLMResponse:
        content = request.messages[-1].content

        return LLMResponse(
            content=f"Echo: {content}",
            model="fake-model",
            provider=self.provider_name,
            input_tokens=3,
            output_tokens=4,
        )


def test_llm_request_defaults() -> None:
    request = LLMRequest(
        messages=[
            LLMMessage(
                role="user",
                content="Hello",
            )
        ]
    )

    assert request.temperature == 0.2
    assert request.max_tokens is None
    assert request.messages[0].role == "user"


def test_llm_response() -> None:
    response = LLMResponse(
        content="Hello back",
        model="fake-model",
        provider="fake",
    )

    assert response.content == "Hello back"
    assert response.model == "fake-model"
    assert response.provider == "fake"


@pytest.mark.asyncio
async def test_fake_llm_provider() -> None:
    provider = FakeLLMProvider()
    request = LLMRequest(
        messages=[
            LLMMessage(
                role="user",
                content="Explain predictive maintenance.",
            )
        ]
    )

    response = await provider.generate(request)

    assert provider.provider_name == "fake"
    assert response.provider == "fake"
    assert response.content == "Echo: Explain predictive maintenance."


def test_register_and_create_llm_provider() -> None:
    clear_llm_provider_registry()
    register_llm_provider("fake", FakeLLMProvider)

    provider = create_llm_provider("FAKE")

    assert isinstance(provider, FakeLLMProvider)
    assert provider.provider_name == "fake"


def test_list_llm_providers() -> None:
    clear_llm_provider_registry()
    register_llm_provider("zeta", FakeLLMProvider)
    register_llm_provider("alpha", FakeLLMProvider)

    assert list_llm_providers() == ("alpha", "zeta")


def test_register_llm_provider_rejects_empty_name() -> None:
    clear_llm_provider_registry()

    with pytest.raises(
        ValueError,
        match="Provider name cannot be empty",
    ):
        register_llm_provider("", FakeLLMProvider)


def test_create_llm_provider_rejects_unknown_provider() -> None:
    clear_llm_provider_registry()

    with pytest.raises(
        UnsupportedLLMProviderError,
        match="Unsupported LLM provider",
    ):
        create_llm_provider("unknown")
