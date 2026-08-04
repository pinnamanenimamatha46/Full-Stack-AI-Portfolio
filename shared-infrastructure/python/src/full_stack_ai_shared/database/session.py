"""Shared SQLAlchemy engine and session utilities."""

from collections.abc import Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from full_stack_ai_shared.config import Settings, get_settings


def create_database_engine(settings: Settings | None = None) -> Engine:
    """Create a SQLAlchemy engine using application settings."""

    resolved_settings = settings or get_settings()

    connect_args: dict[str, object] = {}

    if resolved_settings.database_url.startswith("sqlite"):
        connect_args["check_same_thread"] = False

    return create_engine(
        resolved_settings.database_url,
        pool_pre_ping=True,
        connect_args=connect_args,
    )


def create_session_factory(
    engine: Engine,
) -> sessionmaker[Session]:
    """Create a configured SQLAlchemy session factory."""

    return sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
        expire_on_commit=False,
    )


def get_database_session(
    session_factory: sessionmaker[Session],
) -> Generator[Session, None, None]:
    """Yield a database session and always close it afterward."""

    session = session_factory()

    try:
        yield session
    finally:
        session.close()
