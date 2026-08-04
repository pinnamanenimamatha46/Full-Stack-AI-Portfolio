"""Tests for shared application settings."""

from full_stack_ai_shared.config import Settings, get_settings


def test_default_settings() -> None:
    settings = Settings()

    assert settings.app_name == "Full Stack AI Portfolio"
    assert settings.environment == "development"
    assert settings.debug is True
    assert settings.redis_url == "redis://localhost:6379/0"


def test_get_settings_is_cached() -> None:
    first = get_settings()
    second = get_settings()

    assert first is second