"""Tests for shared database utilities."""

from sqlalchemy import Engine, text
from sqlalchemy.orm import Session

from full_stack_ai_shared.config import Settings
from full_stack_ai_shared.database import (
    create_database_engine,
    create_session_factory,
    get_database_session,
)


def create_test_settings() -> Settings:
    """Return isolated SQLite settings for database tests."""

    return Settings(
        database_url="sqlite+pysqlite:///:memory:",
        openai_api_key=None,
    )


def test_create_database_engine() -> None:
    engine = create_database_engine(create_test_settings())

    assert isinstance(engine, Engine)
    assert engine.url.drivername == "sqlite+pysqlite"

    engine.dispose()


def test_session_factory_executes_query() -> None:
    engine = create_database_engine(create_test_settings())
    session_factory = create_session_factory(engine)

    with session_factory() as session:
        result = session.execute(text("SELECT 1")).scalar_one()

    assert result == 1

    engine.dispose()


def test_get_database_session_closes_session() -> None:
    engine = create_database_engine(create_test_settings())
    session_factory = create_session_factory(engine)

    dependency = get_database_session(session_factory)
    session = next(dependency)

    assert isinstance(session, Session)

    try:
        next(dependency)
    except StopIteration:
        pass

    assert session.is_active is True

    engine.dispose()
