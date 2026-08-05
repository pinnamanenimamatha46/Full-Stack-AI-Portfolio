##********************************************************************************************************
                                     ## Full-Stack-AI-Portfolio
##********************************************************************************************************

## 1) Project Overview

Full-Stack-AI-Portfolio is an enterprise-grade AI engineering portfolio that demonstrates modern Full Stack AI development using production-ready architecture, cloud-native technologies, Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), Agentic AI, and enterprise software engineering best practices.

The portfolio is designed to showcase the complete lifecycle of building AI applications—from backend APIs and databases to frontend interfaces, multi-agent systems, CI/CD pipelines, Docker deployments, Kubernetes orchestration, monitoring, testing, and production-ready infrastructure.

This portfolio represents how enterprise AI systems are designed and implemented in real-world organizations.

## 2) Create parent project and cd into it:
        ## mkdir Full-Stack-AI-Portfolio
        ## cd Full-Stack-AI-Portfolio

##  3) Initialize Git in the parent folder  :
        ## git init
    
        ##  3i) Rename the default branch to main:
                ## git branch -M main

        ##  3ii) Verify Git:
                    ## git status

##  4) Open the project in VS Code:
        ## code .


## 5) Create the portfolio folder structure:
        ## mkdir .github 
        ## mkdir architecture 
        ## mkdir deployments 
        ## mkdir docs 
        ## mkdir monitoring 
        ## mkdir scripts 
        ## mkdir shared-infrastructure 
        ## mkdir templates

##  6) Create the main AI project folders:
        ## mkdir enterprise-ai-operations-platform
        ## mkdir enterprise-knowledge-copilot
        ## mkdir ai-customer-support-multi-agent-platform
        ## mkdir ai-devops-incident-commander
        ## mkdir industrial-predictive-maintenance-ai
        ## mkdir healthcare-clinical-ai-platform
        ## mkdir financial-risk-intelligence-platform
        ## mkdir ai-software-engineering-assistant

##  7) Verify the structure:
        ## dir

C:\projects\Full-Stack-AI-Portfolio
│
├── .github
├── architecture
├── deployments
├── docs
├── monitoring
├── scripts
├── shared-infrastructure
├── templates
│
├── enterprise-ai-operations-platform
├── enterprise-knowledge-copilot
├── ai-customer-support-multi-agent-platform
├── ai-devops-incident-commander
├── industrial-predictive-maintenance-ai
├── healthcare-clinical-ai-platform
├── financial-risk-intelligence-platform
├── ai-software-engineering-assistant
│
└── portfolio-setup.md (currently named `porfolio-setup.md`)

##  8) Create the Parent README:
        ## New-Item README.md -ItemType File

# Full-Stack-AI-Portfolio

An enterprise-grade portfolio of Full Stack AI applications demonstrating modern AI engineering, Agentic AI, Retrieval-Augmented Generation (RAG), enterprise integrations, and cloud-native software development.

## Portfolio Goals

- Build production-ready AI platforms from scratch
- Demonstrate enterprise software architecture
- Showcase Agentic AI and multi-agent systems
- Implement Retrieval-Augmented Generation (RAG)
- Integrate Large Language Models (LLMs)
- Follow modern DevOps and CI/CD practices
- Create a strong portfolio for Full Stack AI Engineer roles

## Repository Structure

```
Full-Stack-AI-Portfolio/
│
├── .github/
├── architecture/
├── deployments/
├── docs/
├── monitoring/
├── scripts/
├── shared-infrastructure/
├── templates/
│
├── enterprise-ai-operations-platform/
├── enterprise-knowledge-copilot/
├── ai-customer-support-multi-agent-platform/
├── ai-devops-incident-commander/
├── industrial-predictive-maintenance-ai/
├── healthcare-clinical-ai-platform/
├── financial-risk-intelligence-platform/
└── ai-software-engineering-assistant/
```

## Technology Stack

### Backend
- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Redis

### Frontend
- React
- Next.js
- TypeScript
- Tailwind CSS

### AI
- OpenAI
- LangChain
- LangGraph
- MCP
- RAG
- FAISS / ChromaDB

### DevOps
- Docker
- Kubernetes
- GitHub Actions
- Prometheus
- Grafana

## Projects

1. Enterprise AI Operations Platform
2. Enterprise Knowledge Copilot
3. AI Customer Support Multi-Agent Platform
4. AI DevOps Incident Commander
5. Industrial Predictive Maintenance AI
6. Healthcare Clinical AI Platform
7. Financial Risk Intelligence Platform
8. AI Software Engineering Assistant

---

This repository is developed incrementally from scratch using VS Code, Git, GitHub, Docker, and modern AI engineering practices.


##  9) Create the Parent .gitignore:
        ## New-Item .gitignore -ItemType File

# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
.venv/
venv/

# Environment variables
.env
.env.*
!.env.example

# Testing and quality tools
.pytest_cache/
.ruff_cache/
.mypy_cache/
.coverage
coverage.xml
htmlcov/

# Python build files
build/
dist/
*.egg-info/

# Node.js
node_modules/
.next/
out/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*

# Frontend environment files
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE and editors
.vscode/
.idea/
*.swp
*.swo

# Operating systems
.DS_Store
Thumbs.db
desktop.ini

# Logs
*.log
logs/

# Databases
*.db
*.sqlite
*.sqlite3

# Docker
*.pid

# AI and vector storage
chroma/
chroma_db/
vector_store/
faiss_index/

# Machine learning artifacts
models/
artifacts/
checkpoints/
*.pkl
*.joblib
*.onnx
*.pt
*.pth

# Temporary files
tmp/
temp/
.cache/


##  10) Add placeholder files

@(
".github",
"architecture",
"deployments",
"docs",
"monitoring",
"scripts",
"shared-infrastructure",
"templates",
"enterprise-ai-operations-platform",
"enterprise-knowledge-copilot",
"ai-customer-support-multi-agent-platform",
"ai-devops-incident-commander",
"industrial-predictive-maintenance-ai",
"healthcare-clinical-ai-platform",
"financial-risk-intelligence-platform",
"ai-software-engineering-assistant"
) | ForEach-Object {
    New-Item -Path "$_\.gitkeep" -ItemType File -Force | Out-Null
}

## 11) Verify:
        ## git status

## 12) Create the first commit
        ## git add .
        ## git commit -m "Initial full stack AI portfolio structure"
        ## git remote add origin https://github.com/pinnamanenimamatha46/Full-Stack-AI-Portfolio.git
        ## git remote -v
        ## git push -u origin main
        ## git log --oneline

## 13) Run
        ##  git add .gitignore
        ##  git commit -m "Add parent gitignore"
        ##  git push origin main
        ##  git status
        ##  git log --oneline

        ## git add portfolio-setup.md
        ## git commit -m "Update portfolio setup guide"
        ## git push origin main

## 14) Create the shared foundation folders

$folders = @(
    "shared-infrastructure\docker\postgres",
    "shared-infrastructure\docker\redis",
    "shared-infrastructure\docker\pgadmin",
    "shared-infrastructure\python",
    "shared-infrastructure\shared\config",
    "shared-infrastructure\shared\database",
    "shared-infrastructure\shared\auth",
    "shared-infrastructure\shared\logging",
    "shared-infrastructure\shared\ai",
    "shared-infrastructure\shared\prompts",
    "shared-infrastructure\shared\rag",
    "shared-infrastructure\shared\agents",
    "shared-infrastructure\shared\llm",
    "shared-infrastructure\shared\utils",
    "monitoring\prometheus",
    "monitoring\grafana",
    "templates\fastapi",
    "templates\react",
    "templates\nextjs",
    "templates\streamlit"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Path $folder -Force | Out-Null
    New-Item -ItemType File -Path "$folder\.gitkeep" -Force | Out-Null
}

## 15) Verify the structure:
        ## tree /F

## 16) Commit the shared infrastructure foundation folders
        ## git add .
        ## git commit -m "Add shared infrastructure foundation"
        ## git push origin main
        ## git status
        ## git log --oneline

## 17) cd shared-infrastructure\python

        ## uv init --python 3.11

        ## remove: Remove-Item .gitkeep

        ## code pyproject.toml
[project]
name = "full-stack-ai-shared"
version = "0.1.0"
description = "Shared Python libraries and infrastructure for the Full Stack AI Portfolio."
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

        ## code main.py
def main() -> None:
    print("Full Stack AI shared infrastructure is ready.")


if __name__ == "__main__":
    main()

        ## Add Developmental Dependencies
        ## Auv add --dev pytest pytest-asyncio ruff mypy
        ## uv sync

## 18)  Verify the workspace:
        ## uv run python main.py
        Full Stack AI shared infrastructure is ready.

## 19)  Run
        ## uv run ruff check .
        All checks passed!
        ## uv run pytest
        no tests ran in 0.01

        ## cd ..
        ## git status

## 20)  create the shared Python package structure:

$folders = @(
    "shared-infrastructure\python\src\full_stack_ai_shared\config",
    "shared-infrastructure\python\src\full_stack_ai_shared\database",
    "shared-infrastructure\python\src\full_stack_ai_shared\logging",
    "shared-infrastructure\python\src\full_stack_ai_shared\ai",
    "shared-infrastructure\python\src\full_stack_ai_shared\rag",
    "shared-infrastructure\python\src\full_stack_ai_shared\agents",
    "shared-infrastructure\python\src\full_stack_ai_shared\llm",
    "shared-infrastructure\python\src\full_stack_ai_shared\utils",
    "shared-infrastructure\python\tests"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Path $folder -Force | Out-Null
}

        ## Create the Python package files:

$files = @(
    "shared-infrastructure\python\src\full_stack_ai_shared\__init__.py",
    "shared-infrastructure\python\src\full_stack_ai_shared\config\__init__.py",
    "shared-infrastructure\python\src\full_stack_ai_shared\database\__init__.py",
    "shared-infrastructure\python\src\full_stack_ai_shared\logging\__init__.py",
    "shared-infrastructure\python\src\full_stack_ai_shared\ai\__init__.py",
    "shared-infrastructure\python\src\full_stack_ai_shared\rag\__init__.py",
    "shared-infrastructure\python\src\full_stack_ai_shared\agents\__init__.py",
    "shared-infrastructure\python\src\full_stack_ai_shared\llm\__init__.py",
    "shared-infrastructure\python\src\full_stack_ai_shared\utils\__init__.py",
    "shared-infrastructure\python\tests\__init__.py"
)

foreach ($file in $files) {
    New-Item -ItemType File -Path $file -Force | Out-Null
}

        ## Update pyproject.toml
            ## code shared-infrastructure\python\pyproject.toml
[project]
name = "full-stack-ai-shared"
version = "0.1.0"
description = "Shared Python libraries for the Full Stack AI Portfolio."
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[dependency-groups]
dev = [
    "mypy>=1.17.0",
    "pytest>=8.4.0",
    "pytest-asyncio>=1.1.0",
    "ruff>=0.12.0",
]

[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]
asyncio_mode = "auto"

[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]

[tool.mypy]
python_version = "3.11"
strict = true
packages = ["full_stack_ai_shared"]
mypy_path = "src"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

## 21)  Update main.py
        ## code shared-infrastructure\python\main.py

from full_stack_ai_shared import __version__


def main() -> None:
    print(f"Full Stack AI shared infrastructure v{__version__} is ready.")


if __name__ == "__main__":
    main()

## 22)  Update the package initializer
        ## code shared-infrastructure\python\src\full_stack_ai_shared\__init__.py

"""Shared Python utilities for the Full Stack AI Portfolio."""

__version__ = "0.1.0"

## 23)  Synchronize and verify

        ##  cd shared-infrastructure\python
        ##  uv sync
        ##  uv run python main.py
        ##  uv run ruff check .
        ##  uv run mypy src
        ##  uv run pytest

## 24) Add the first shared configuration module

        ##  install Pydantic Settings:
        ##  uv add pydantic-settings
        ##  UV SYNC

## 25)  Create the configuration files:
        code src\full_stack_ai_shared\config\settings.py

"""Application configuration shared across portfolio projects."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Shared application settings."""

    app_name: str = "Full Stack AI Portfolio"
    environment: str = "development"
    debug: bool = True

    database_url: str = (
        "postgresql+psycopg://postgres:postgres@localhost:5432/full_stack_ai"
    )
    redis_url: str = "redis://localhost:6379/0"

    openai_api_key: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return a cached settings instance."""

    return Settings()

## 26)  updatw: code src\full_stack_ai_shared\config\__init__.py

"""Shared configuration utilities."""

from full_stack_ai_shared.config.settings import Settings, get_settings

__all__ = ["Settings", "get_settings"]

## 27)  Add the first test: code tests\test_settings.py

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

## 28)  Run
        ##  uv run ruff check .
        ## uv run mypy src
        ## uv run pytest -v
           2 passed in 0.57s
        
        ## git add shared-infrastructure/python
        ## git commit -m "Add shared Python foundation"
        ## git push origin main
        ## git status
        ## git log --oneline

## 29)  Build the shared SQLAlchemy database layer

        ## cd shared-infrastructure\python

        ## 1. Install database dependencies: 
                ## uv add sqlalchemy "psycopg[binary]"
                uv sync

        ## 2. Create the database files
                ## New-Item src\full_stack_ai_shared\database\base.py -ItemType File -Force
                ## New-Item src\full_stack_ai_shared\database\session.py -ItemType File -Force
                ## New-Item tests\test_database.py -ItemType File -Force
        
        ## Add the declarative base:    code src\full_stack_ai_shared\database\base.py

"""Shared SQLAlchemy declarative base."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""

        ## Add engine and session management: code src\full_stack_ai_shared\database\session.py

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

        ## 5. Export the database utilities:    code src\full_stack_ai_shared\database\__init__.py

"""Shared database utilities."""

from full_stack_ai_shared.database.base import Base
from full_stack_ai_shared.database.session import (
    create_database_engine,
    create_session_factory,
    get_database_session,
)

__all__ = [
    "Base",
    "create_database_engine",
    "create_session_factory",
    "get_database_session",
]

        ## Add database tests:  code tests\test_database.py

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

        ## 7. Format and validate

                ## uv run ruff format .
                ## uv run ruff check .
                ## uv run mypy src
                ## uv run pytest -v:    5 passed in 1.71s

                ## uv run python main.py
        
        ## 9. Return to the parent and inspect Git

                ## cd ..\..
                ## git status

                ## Commit the database layer
                    ## git add shared-infrastructure/python
                    ## git status
                    ## git commit -m "Add shared SQLAlchemy database layer"
                    ## git push origin main

## 30)  Phase 2.3 — Shared Enterprise Logging Framework

            ## cd shared-infrastructure\python 
            
            ##  Step 1 — Install logging dependencies

                ## uv add python-json-logger
                ## uv sync

            ## Step 2 — Create the logging files

                ## New-Item src\full_stack_ai_shared\logging\logger.py -ItemType File -Force
                ## New-Item src\full_stack_ai_shared\logging\formatter.py -ItemType File -Force
                ## New-Item src\full_stack_ai_shared\logging\request_context.py -ItemType File -Force
                ## New-Item src\full_stack_ai_shared\logging\middleware.py -ItemType File -Force
                ## New-Item tests\test_logging.py -ItemType File -Force

            ## Step 3 — Update the logging package export:   
                        code src\full_stack_ai_shared\logging\__init__.py
"""Shared logging utilities."""

from full_stack_ai_shared.logging.logger import get_logger

__all__ = ["get_logger"]

            ## Step 4 — Verify the structure
                        tree src\full_stack_ai_shared\logging /F
            

            ## Build:  code src\full_stack_ai_shared\logging\logger.py

"""Shared logger factory."""

from __future__ import annotations

import logging
import sys


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger instance."""

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.propagate = False

    return logger

            ## Create a unit test:      code tests\test_logging.py

"""Tests for the shared logger."""

import logging

from full_stack_ai_shared.logging import get_logger


def test_get_logger() -> None:
    logger = get_logger("portfolio")

    assert isinstance(logger, logging.Logger)
    assert logger.name == "portfolio"
    assert logger.level == logging.INFO

                ## Step 3 — Validate

                    ## uv run ruff format .
                    ## uv run ruff check .
                    ## uv run mypy src
                    ## uv run pytest -v:    6 passed in 0.58s 
        

                ## Add request correlation IDs

                    This allows every API request to carry a unique identifier through logs, which is useful for tracing errors across services.
                
                    ## code src\full_stack_ai_shared\logging\request_context.py

"""Request-scoped logging context."""

from contextvars import ContextVar
from uuid import uuid4

_request_id_context: ContextVar[str | None] = ContextVar(
    "request_id",
    default=None,
)


def create_request_id() -> str:
    """Create a new request identifier."""

    return str(uuid4())


def set_request_id(request_id: str) -> None:
    """Store the current request identifier."""

    _request_id_context.set(request_id)


def get_request_id() -> str | None:
    """Return the current request identifier."""

    return _request_id_context.get()


def clear_request_id() -> None:
    """Clear the current request identifier."""

    _request_id_context.set(None)

                ## Update: code src\full_stack_ai_shared\logging\__init__.py

"""Shared logging utilities."""

from full_stack_ai_shared.logging.logger import get_logger
from full_stack_ai_shared.logging.request_context import (
    clear_request_id,
    create_request_id,
    get_request_id,
    set_request_id,
)

__all__ = [
    "clear_request_id",
    "create_request_id",
    "get_logger",
    "get_request_id",
    "set_request_id",
]

                ## Add these tests to tests\test_logging.py: 

"""Tests for the shared logging utilities."""

import logging

from full_stack_ai_shared.logging import (
    clear_request_id,
    create_request_id,
    get_logger,
    get_request_id,
    set_request_id,
)


def test_get_logger() -> None:
    logger = get_logger("portfolio")

    assert isinstance(logger, logging.Logger)
    assert logger.name == "portfolio"
    assert logger.level == logging.INFO


def test_request_id_context() -> None:
    request_id = create_request_id()

    set_request_id(request_id)

    assert get_request_id() == request_id

    clear_request_id()

    assert get_request_id() is None


def test_create_request_id_is_unique() -> None:
    first = create_request_id()
    second = create_request_id()

    assert first != second

            ## Run
               ## uv run ruff format tests\test_logging.py
                ## uv run ruff check .
                ## uv run mypy src
                ## uv run pytest -v:    8 passed in 0.46s
            
            ## Add the request ID to every log record
                ## code src\full_stack_ai_shared\logging\formatter.py
"""Logging formatters and filters."""

import logging

from full_stack_ai_shared.logging.request_context import get_request_id


class RequestContextFilter(logging.Filter):
    """Attach the current request ID to each log record."""

    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = get_request_id() or "-"
        return True


def create_console_formatter() -> logging.Formatter:
    """Create the standard console log formatter."""

    return logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | "
        "request_id=%(request_id)s | %(message)s"
    )
            ##  Update: code src\full_stack_ai_shared\logging\logger.py

"""Shared logger factory."""

from __future__ import annotations

import logging
import sys

from full_stack_ai_shared.logging.formatter import (
    RequestContextFilter,
    create_console_formatter,
)


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger instance."""

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.addFilter(RequestContextFilter())
    handler.setFormatter(create_console_formatter())

    logger.addHandler(handler)
    logger.propagate = False

    return logger

            ##  code tests\test_logging.py
"""Tests for the shared logging utilities."""

import logging

from full_stack_ai_shared.logging import (
    clear_request_id,
    create_request_id,
    get_logger,
    get_request_id,
    set_request_id,
)


def test_get_logger() -> None:
    logger = get_logger("portfolio")

    assert isinstance(logger, logging.Logger)
    assert logger.name == "portfolio"
    assert logger.level == logging.INFO


def test_request_id_context() -> None:
    request_id = create_request_id()

    set_request_id(request_id)

    assert get_request_id() == request_id

    clear_request_id()

    assert get_request_id() is None


def test_create_request_id_is_unique() -> None:
    first = create_request_id()
    second = create_request_id()

    assert first != second


def test_logger_includes_request_id() -> None:
    logger = get_logger("portfolio.request-context")
    request_id = create_request_id()
    set_request_id(request_id)

    try:
        handler = logger.handlers[0]

        record = logger.makeRecord(
            logger.name,
            logging.INFO,
            __file__,
            1,
            "test message",
            (),
            None,
        )

        for log_filter in handler.filters:
            log_filter.filter(record)

        formatted_message = handler.format(record)

        assert request_id in formatted_message
        assert "test message" in formatted_message
    finally:
        clear_request_id()

                ## Run:
                    uv run ruff format tests\test_logging.py
                    uv run ruff check .
                    uv run mypy src
                    uv run pytest -v

                ## Add FastAPI request logging middleware

                    ## nstall FastAPI as a shared dependency: 
                        uv add fastapi
                        uv sync
                    ## code src\full_stack_ai_shared\logging\middleware.py
"""FastAPI request logging middleware."""

from __future__ import annotations

from time import perf_counter
from typing import Final

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from full_stack_ai_shared.logging.logger import get_logger
from full_stack_ai_shared.logging.request_context import (
    clear_request_id,
    create_request_id,
    set_request_id,
)

REQUEST_ID_HEADER: Final[str] = "X-Request-ID"

logger = get_logger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Log HTTP requests and attach a request ID to each response."""

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        request_id = request.headers.get(REQUEST_ID_HEADER) or create_request_id()
        set_request_id(request_id)

        started_at = perf_counter()

        try:
            response = await call_next(request)

            duration_ms = (perf_counter() - started_at) * 1000

            logger.info(
                "%s %s completed with status %s in %.2f ms",
                request.method,
                request.url.path,
                response.status_code,
                duration_ms,
            )

            response.headers[REQUEST_ID_HEADER] = request_id
            return response
        except Exception:
            duration_ms = (perf_counter() - started_at) * 1000

            logger.exception(
                "%s %s failed after %.2f ms",
                request.method,
                request.url.path,
                duration_ms,
            )

            raise
        finally:
            clear_request_id()

            ## Update: code src\full_stack_ai_shared\logging\__init__.py

"""Shared logging utilities."""

from full_stack_ai_shared.logging.logger import get_logger
from full_stack_ai_shared.logging.middleware import (
    REQUEST_ID_HEADER,
    RequestLoggingMiddleware,
)
from full_stack_ai_shared.logging.request_context import (
    clear_request_id,
    create_request_id,
    get_request_id,
    set_request_id,
)

__all__ = [
    "REQUEST_ID_HEADER",
    "RequestLoggingMiddleware",
    "clear_request_id",
    "create_request_id",
    "get_logger",
    "get_request_id",
    "set_request_id",
]

            ## code tests\test_logging_middleware.py
"""Tests for FastAPI request logging middleware."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from full_stack_ai_shared.logging import (
    REQUEST_ID_HEADER,
    RequestLoggingMiddleware,
)


def create_test_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(RequestLoggingMiddleware)

    @app.get("/health")
    async def health_check() -> dict[str, str]:
        return {"status": "healthy"}

    return app


def test_middleware_generates_request_id() -> None:
    client = TestClient(create_test_app())

    response = client.get("/health")

    assert response.status_code == 200
    assert response.headers[REQUEST_ID_HEADER]


def test_middleware_preserves_request_id() -> None:
    client = TestClient(create_test_app())
    request_id = "test-request-123"

    response = client.get(
        "/health",
        headers={REQUEST_ID_HEADER: request_id},
    )

    assert response.status_code == 200
    assert response.headers[REQUEST_ID_HEADER] == request_id

            ## Run

            uv run ruff format .
            uv run ruff check .
            uv run mypy src
            uv run pytest -v:   11 passed in 1.10s

            uv add --dev httpx2
            uv sync
        ## Run
           cd ..\..
            git add shared-infrastructure/python
            git status.
            git commit -m "Add shared request logging framework"
            git push origin main
            git status
            git log --oneline

## 31)  Phase 2.4 — Shared API & Exception Framework:

        ## Step 1 — Create the directories

                    New-Item src\full_stack_ai_shared\api -ItemType Directory -Force
                    New-Item src\full_stack_ai_shared\exceptions -ItemType Directory -Force

        ## Step 2 — Create the files

                    New-Item src\full_stack_ai_shared\api\__init__.py -ItemType File -Force
                    New-Item src\full_stack_ai_shared\api\responses.py -ItemType File -Force
                    New-Item src\full_stack_ai_shared\api\health.py -ItemType File -Force

                    New-Item src\full_stack_ai_shared\exceptions\__init__.py -ItemType File -Force
                    New-Item src\full_stack_ai_shared\exceptions\errors.py -ItemType File -Force
                    New-Item src\full_stack_ai_shared\exceptions\handlers.py -ItemType File -Force

                    New-Item tests\test_api.py -ItemType File -Force
                    New-Item tests\test_exceptions.py -ItemType File -Force

## Step 3 — Verify

            tree src\full_stack_ai_shared /F

## Step 1: Implement reusable API response models: code src\full_stack_ai_shared\api\responses.py

"""Reusable API response models."""

from typing import Generic, TypeVar

from pydantic import BaseModel, Field

DataT = TypeVar("DataT")


class SuccessResponse(BaseModel, Generic[DataT]):
    """Standard successful API response."""

    success: bool = True
    message: str
    data: DataT | None = None


class ErrorDetail(BaseModel):
    """Structured API error information."""

    code: str
    message: str
    field: str | None = None


class ErrorResponse(BaseModel):
    """Standard API error response."""

    success: bool = False
    message: str
    errors: list[ErrorDetail] = Field(default_factory=list)
    request_id: str | None = None

## Step 2: Export the response models: code src\full_stack_ai_shared\api\__init__.py

"""Shared API utilities."""

from full_stack_ai_shared.api.responses import (
    ErrorDetail,
    ErrorResponse,
    SuccessResponse,
)

__all__ = [
    "ErrorDetail",
    "ErrorResponse",
    "SuccessResponse",
]

## Step 3: Add response-model tests:    code tests\test_api.py

"""Tests for shared API response models."""

from full_stack_ai_shared.api import (
    ErrorDetail,
    ErrorResponse,
    SuccessResponse,
)


def test_success_response() -> None:
    response = SuccessResponse[dict[str, str]](
        message="Operation completed.",
        data={"status": "ready"},
    )

    assert response.success is True
    assert response.message == "Operation completed."
    assert response.data == {"status": "ready"}


def test_error_response() -> None:
    response = ErrorResponse(
        message="Validation failed.",
        errors=[
            ErrorDetail(
                code="invalid_value",
                message="The supplied value is invalid.",
                field="name",
            )
        ],
        request_id="request-123",
    )

    assert response.success is False
    assert response.request_id == "request-123"
    assert response.errors[0].code == "invalid_value"
    assert response.errors[0].field == "name"


def test_error_response_defaults_to_empty_errors() -> None:
    response = ErrorResponse(message="Unexpected error.")

    assert response.errors == []

## Verify:

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## Implement the reusable health endpoint

code src\full_stack_ai_shared\api\health.py

"""Reusable health-check API router."""

from datetime import UTC, datetime

from fastapi import APIRouter

from full_stack_ai_shared import __version__
from full_stack_ai_shared.api.responses import SuccessResponse

health_router = APIRouter(tags=["Health"])


@health_router.get(
    "/health",
    response_model=SuccessResponse[dict[str, str]],
)
async def health_check() -> SuccessResponse[dict[str, str]]:
    """Return the shared service health status."""

    return SuccessResponse(
        message="Service is healthy.",
        data={
            "status": "healthy",
            "version": __version__,
            "timestamp": datetime.now(UTC).isoformat(),
        },
    )

## Update: code src\full_stack_ai_shared\api\__init__.py

"""Shared API utilities."""

from full_stack_ai_shared.api.health import health_router
from full_stack_ai_shared.api.responses import (
    ErrorDetail,
    ErrorResponse,
    SuccessResponse,
)

__all__ = [
    "ErrorDetail",
    "ErrorResponse",
    "SuccessResponse",
    "health_router",
]

## Add health endpoint tests code tests\test_api.p

"""Tests for shared API utilities."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from full_stack_ai_shared.api import (
    ErrorDetail,
    ErrorResponse,
    SuccessResponse,
    health_router,
)


def create_test_app() -> FastAPI:
    app = FastAPI()
    app.include_router(health_router, prefix="/api/v1")
    return app


def test_success_response() -> None:
    response = SuccessResponse[dict[str, str]](
        message="Operation completed.",
        data={"status": "ready"},
    )

    assert response.success is True
    assert response.message == "Operation completed."
    assert response.data == {"status": "ready"}


def test_error_response() -> None:
    response = ErrorResponse(
        message="Validation failed.",
        errors=[
            ErrorDetail(
                code="invalid_value",
                message="The supplied value is invalid.",
                field="name",
            )
        ],
        request_id="request-123",
    )

    assert response.success is False
    assert response.request_id == "request-123"
    assert response.errors[0].code == "invalid_value"
    assert response.errors[0].field == "name"


def test_error_response_defaults_to_empty_errors() -> None:
    response = ErrorResponse(message="Unexpected error.")

    assert response.errors == []


def test_health_endpoint() -> None:
    client = TestClient(create_test_app())

    response = client.get("/api/v1/health")
    payload = response.json()

    assert response.status_code == 200
    assert payload["success"] is True
    assert payload["message"] == "Service is healthy."
    assert payload["data"]["status"] == "healthy"
    assert payload["data"]["version"] == "0.1.0"
    assert payload["data"]["timestamp"]

## Run
uv run ruff format tests\test_api.py
uv run ruff check .
uv run mypy src
uv run pytest -v

## Implement custom exceptions:

## code src\full_stack_ai_shared\exceptions\errors.py

"""Custom application exceptions."""

from __future__ import annotations


class ApplicationError(Exception):
    """Base exception for application-level errors."""

    def __init__(
        self,
        message: str,
        *,
        code: str = "application_error",
        status_code: int = 400,
        field: str | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.status_code = status_code
        self.field = field


class NotFoundError(ApplicationError):
    """Raised when a requested resource cannot be found."""

    def __init__(
        self,
        message: str = "Resource not found.",
        *,
        code: str = "not_found",
    ) -> None:
        super().__init__(
            message,
            code=code,
            status_code=404,
        )


class ConflictError(ApplicationError):
    """Raised when a request conflicts with existing state."""

    def __init__(
        self,
        message: str = "Resource conflict.",
        *,
        code: str = "conflict",
        field: str | None = None,
    ) -> None:
        super().__init__(
            message,
            code=code,
            status_code=409,
            field=field,
        )


class ValidationError(ApplicationError):
    """Raised when application-level validation fails."""

    def __init__(
        self,
        message: str = "Validation failed.",
        *,
        code: str = "validation_error",
        field: str | None = None,
    ) -> None:
        super().__init__(
            message,
            code=code,
            status_code=422,
            field=field,
        )

## Update: code src\full_stack_ai_shared\exceptions\__init__.py

"""Shared application exceptions."""

from full_stack_ai_shared.exceptions.errors import (
    ApplicationError,
    ConflictError,
    NotFoundError,
    ValidationError,
)

__all__ = [
    "ApplicationError",
    "ConflictError",
    "NotFoundError",
    "ValidationError",
]

## Add exception tests: code tests\test_exceptions.py

"""Tests for shared application exceptions."""

from full_stack_ai_shared.exceptions import (
    ApplicationError,
    ConflictError,
    NotFoundError,
    ValidationError,
)


def test_application_error() -> None:
    error = ApplicationError(
        "Operation failed.",
        code="operation_failed",
        status_code=400,
        field="name",
    )

    assert str(error) == "Operation failed."
    assert error.message == "Operation failed."
    assert error.code == "operation_failed"
    assert error.status_code == 400
    assert error.field == "name"


def test_not_found_error() -> None:
    error = NotFoundError("Asset not found.")

    assert error.status_code == 404
    assert error.code == "not_found"
    assert error.message == "Asset not found."


def test_conflict_error() -> None:
    error = ConflictError(
        "Asset already exists.",
        field="asset_id",
    )

    assert error.status_code == 409
    assert error.code == "conflict"
    assert error.field == "asset_id"


def test_validation_error() -> None:
    error = ValidationError(
        "Amount must be positive.",
        field="amount",
    )

    assert error.status_code == 422
    assert error.code == "validation_error"
    assert error.field == "amount"

## Run

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## Add global FastAPI exception handlers

## Implement:   code src\full_stack_ai_shared\exceptions\handlers.py

"""FastAPI exception handlers."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Any, cast

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.responses import Response

from full_stack_ai_shared.api import ErrorDetail, ErrorResponse
from full_stack_ai_shared.exceptions.errors import ApplicationError
from full_stack_ai_shared.logging import get_logger, get_request_id

logger = get_logger(__name__)

ExceptionHandler = Callable[
    [Request, Exception],
    Response | Awaitable[Response],
]


def build_error_response(
    *,
    message: str,
    errors: list[ErrorDetail],
) -> dict[str, Any]:
    """Build a serializable standard error response."""

    response = ErrorResponse(
        message=message,
        errors=errors,
        request_id=get_request_id(),
    )
    return response.model_dump()


async def application_error_handler(
    request: Request,
    exc: ApplicationError,
) -> JSONResponse:
    """Handle known application exceptions."""

    logger.warning(
        "%s %s failed: %s",
        request.method,
        request.url.path,
        exc.message,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=build_error_response(
            message=exc.message,
            errors=[
                ErrorDetail(
                    code=exc.code,
                    message=exc.message,
                    field=exc.field,
                )
            ],
        ),
    )


async def request_validation_error_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    """Handle FastAPI request-validation failures."""

    errors = [
        ErrorDetail(
            code=str(error["type"]),
            message=str(error["msg"]),
            field=".".join(str(part) for part in error["loc"]),
        )
        for error in exc.errors()
    ]

    logger.warning(
        "%s %s validation failed",
        request.method,
        request.url.path,
    )

    return JSONResponse(
        status_code=422,
        content=build_error_response(
            message="Request validation failed.",
            errors=errors,
        ),
    )


async def unhandled_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    """Handle unexpected exceptions without exposing internal details."""

    logger.exception(
        "%s %s raised an unexpected exception",
        request.method,
        request.url.path,
        exc_info=exc,
    )

    return JSONResponse(
        status_code=500,
        content=build_error_response(
            message="An unexpected error occurred.",
            errors=[
                ErrorDetail(
                    code="internal_server_error",
                    message="The server could not complete the request.",
                )
            ],
        ),
    )


def register_exception_handlers(app: FastAPI) -> None:
    """Register all shared exception handlers on a FastAPI application."""

    app.add_exception_handler(
        ApplicationError,
        cast(ExceptionHandler, application_error_handler),
    )
    app.add_exception_handler(
        RequestValidationError,
        cast(ExceptionHandler, request_validation_error_handler),
    )
    app.add_exception_handler(
        Exception,
        unhandled_exception_handler,
    )

## Update: code src\full_stack_ai_shared\exceptions\__init__.py

"""Shared application exceptions."""

from full_stack_ai_shared.exceptions.errors import (
    ApplicationError,
    ConflictError,
    NotFoundError,
    ValidationError,
)
from full_stack_ai_shared.exceptions.handlers import (
    register_exception_handlers,
)

__all__ = [
    "ApplicationError",
    "ConflictError",
    "NotFoundError",
    "ValidationError",
    "register_exception_handlers",
]

## Replace: code tests\test_exceptions.py

"""Tests for shared exceptions and FastAPI handlers."""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

from full_stack_ai_shared.exceptions import (
    ApplicationError,
    ConflictError,
    NotFoundError,
    ValidationError,
    register_exception_handlers,
)
from full_stack_ai_shared.logging import RequestLoggingMiddleware


class ItemRequest(BaseModel):
    """Test request model."""

    quantity: int


def create_test_app() -> FastAPI:
    """Create a FastAPI application with shared handlers."""

    app = FastAPI()
    app.add_middleware(RequestLoggingMiddleware)
    register_exception_handlers(app)

    @app.get("/missing")
    async def missing() -> None:
        raise NotFoundError("Asset not found.")

    @app.get("/conflict")
    async def conflict() -> None:
        raise ConflictError(
            "Asset already exists.",
            field="asset_id",
        )

    @app.post("/items")
    async def create_item(payload: ItemRequest) -> dict[str, int]:
        return {"quantity": payload.quantity}

    @app.get("/unexpected")
    async def unexpected() -> None:
        raise RuntimeError("Sensitive internal failure.")

    return app


def test_application_error() -> None:
    error = ApplicationError(
        "Operation failed.",
        code="operation_failed",
        status_code=400,
        field="name",
    )

    assert str(error) == "Operation failed."
    assert error.message == "Operation failed."
    assert error.code == "operation_failed"
    assert error.status_code == 400
    assert error.field == "name"


def test_not_found_error() -> None:
    error = NotFoundError("Asset not found.")

    assert error.status_code == 404
    assert error.code == "not_found"
    assert error.message == "Asset not found."


def test_conflict_error() -> None:
    error = ConflictError(
        "Asset already exists.",
        field="asset_id",
    )

    assert error.status_code == 409
    assert error.code == "conflict"
    assert error.field == "asset_id"


def test_validation_error() -> None:
    error = ValidationError(
        "Amount must be positive.",
        field="amount",
    )

    assert error.status_code == 422
    assert error.code == "validation_error"
    assert error.field == "amount"


def test_application_exception_handler() -> None:
    client = TestClient(create_test_app())

    response = client.get("/missing")
    payload = response.json()

    assert response.status_code == 404
    assert payload["success"] is False
    assert payload["message"] == "Asset not found."
    assert payload["errors"][0]["code"] == "not_found"
    assert payload["request_id"]


def test_conflict_exception_handler() -> None:
    client = TestClient(create_test_app())

    response = client.get("/conflict")
    payload = response.json()

    assert response.status_code == 409
    assert payload["errors"][0]["code"] == "conflict"
    assert payload["errors"][0]["field"] == "asset_id"


def test_request_validation_exception_handler() -> None:
    client = TestClient(create_test_app())

    response = client.post(
        "/items",
        json={"quantity": "invalid"},
    )
    payload = response.json()

    assert response.status_code == 422
    assert payload["success"] is False
    assert payload["message"] == "Request validation failed."
    assert payload["errors"]
    assert payload["errors"][0]["field"] == "body.quantity"


def test_unhandled_exception_handler() -> None:
    client = TestClient(
        create_test_app(),
        raise_server_exceptions=False,
    )

    response = client.get("/unexpected")
    payload = response.json()

    assert response.status_code == 500
    assert payload["success"] is False
    assert payload["message"] == "An unexpected error occurred."
    assert payload["errors"][0]["code"] == "internal_server_error"
    assert "Sensitive internal failure" not in response.text

## Verify everything

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## Commit the changes from parent:

cd ..\..
git add shared-infrastructure/python
git status
git commit -m "Add shared API and exception framework"
git push origin main
git status
git log --oneline

## Shared authentication and security

# Move into : cd shared-infrastructure\python

## Install authentication dependencies: 
uv add "pwdlib[argon2]" pyjwt
uv sync

## create folders and files

New-Item src\full_stack_ai_shared\auth -ItemType Directory -Force
New-Item src\full_stack_ai_shared\security -ItemType Directory -Force

New-Item src\full_stack_ai_shared\auth\__init__.py -ItemType File -Force
New-Item src\full_stack_ai_shared\auth\passwords.py -ItemType File -Force
New-Item src\full_stack_ai_shared\auth\tokens.py -ItemType File -Force
New-Item src\full_stack_ai_shared\auth\dependencies.py -ItemType File -Force

New-Item src\full_stack_ai_shared\security\__init__.py -ItemType File -Force
New-Item src\full_stack_ai_shared\security\settings.py -ItemType File -Force

New-Item tests\test_auth.py -ItemType File -Force

## Implement password hashing: code src\full_stack_ai_shared\auth\passwords.py

"""Password hashing and verification utilities."""

from pwdlib import PasswordHash

_password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """Return a secure hash for a plaintext password."""

    if not password:
        raise ValueError("Password cannot be empty.")

    return _password_hash.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """Return whether a plaintext password matches a stored hash."""

    if not plain_password or not hashed_password:
        return False

    return _password_hash.verify(
        plain_password,
        hashed_password,
    )

## Export password utilities: code src\full_stack_ai_shared\auth\__init__.py

"""Shared authentication utilities."""

from full_stack_ai_shared.auth.passwords import (
    hash_password,
    verify_password,
)

__all__ = [
    "hash_password",
    "verify_password",
]

## code tests\test_auth.py

"""Tests for shared authentication utilities."""

import pytest

from full_stack_ai_shared.auth import (
    hash_password,
    verify_password,
)


def test_hash_password() -> None:
    password = "StrongPassword123!"
    hashed_password = hash_password(password)

    assert hashed_password != password
    assert verify_password(password, hashed_password) is True


def test_verify_password_rejects_invalid_password() -> None:
    hashed_password = hash_password("CorrectPassword123!")

    assert verify_password(
        "WrongPassword123!",
        hashed_password,
    ) is False


def test_hash_password_uses_unique_salt() -> None:
    password = "StrongPassword123!"

    first_hash = hash_password(password)
    second_hash = hash_password(password)

    assert first_hash != second_hash
    assert verify_password(password, first_hash) is True
    assert verify_password(password, second_hash) is True


def test_hash_password_rejects_empty_password() -> None:
    with pytest.raises(
        ValueError,
        match="Password cannot be empty",
    ):
        hash_password("")


def test_verify_password_rejects_empty_values() -> None:
    assert verify_password("", "stored-hash") is False
    assert verify_password("password", "") is False

## Verify

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## Add JWT access tokens

## code src\full_stack_ai_shared\security\settings.py

"""Authentication and token settings."""

from pydantic import BaseModel, Field


class TokenSettings(BaseModel):
    """JWT configuration."""

    secret_key: str = Field(min_length=32)
    algorithm: str = "HS256"
    access_token_expire_minutes: int = Field(default=30, gt=0)
    issuer: str = "full-stack-ai-portfolio"
    audience: str = "full-stack-ai-applications"

## code src\full_stack_ai_shared\security\__init__.py

"""Shared security settings."""

from full_stack_ai_shared.security.settings import TokenSettings

__all__ = ["TokenSettings"]

## code src\full_stack_ai_shared\auth\tokens.py

"""JWT access-token creation and validation."""

from datetime import UTC, datetime, timedelta
from typing import Any

import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from pydantic import BaseModel

from full_stack_ai_shared.security import TokenSettings


class TokenPayload(BaseModel):
    """Validated JWT payload."""

    subject: str
    issued_at: datetime
    expires_at: datetime
    issuer: str
    audience: str


class TokenError(ValueError):
    """Raised when an access token cannot be validated."""


def create_access_token(
    subject: str,
    settings: TokenSettings,
    *,
    expires_delta: timedelta | None = None,
    additional_claims: dict[str, Any] | None = None,
) -> str:
    """Create a signed JWT access token."""

    if not subject.strip():
        raise ValueError("Token subject cannot be empty.")

    issued_at = datetime.now(UTC)
    expires_at = issued_at + (
        expires_delta
        or timedelta(minutes=settings.access_token_expire_minutes)
    )

    payload: dict[str, Any] = {
        "sub": subject,
        "iat": issued_at,
        "exp": expires_at,
        "iss": settings.issuer,
        "aud": settings.audience,
    }

    if additional_claims:
        protected_claims = {"sub", "iat", "exp", "iss", "aud"}
        conflicting_claims = protected_claims.intersection(additional_claims)

        if conflicting_claims:
            names = ", ".join(sorted(conflicting_claims))
            raise ValueError(
                f"Additional claims cannot override protected claims: {names}"
            )

        payload.update(additional_claims)

    return jwt.encode(
        payload,
        settings.secret_key,
        algorithm=settings.algorithm,
    )


def decode_access_token(
    token: str,
    settings: TokenSettings,
) -> TokenPayload:
    """Decode and validate a JWT access token."""

    if not token:
        raise TokenError("Access token cannot be empty.")

    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm],
            audience=settings.audience,
            issuer=settings.issuer,
        )
    except ExpiredSignatureError as exc:
        raise TokenError("Access token has expired.") from exc
    except InvalidTokenError as exc:
        raise TokenError("Access token is invalid.") from exc

    subject = payload.get("sub")

    if not isinstance(subject, str) or not subject:
        raise TokenError("Access token subject is invalid.")

    return TokenPayload(
        subject=subject,
        issued_at=datetime.fromtimestamp(payload["iat"], tz=UTC),
        expires_at=datetime.fromtimestamp(payload["exp"], tz=UTC),
        issuer=payload["iss"],
        audience=payload["aud"],
    )

## code src\full_stack_ai_shared\auth\__init__.py

"""Shared authentication utilities."""

from full_stack_ai_shared.auth.passwords import (
    hash_password,
    verify_password,
)
from full_stack_ai_shared.auth.tokens import (
    TokenError,
    TokenPayload,
    create_access_token,
    decode_access_token,
)

__all__ = [
    "TokenError",
    "TokenPayload",
    "create_access_token",
    "decode_access_token",
    "hash_password",
    "verify_password",
]

## code tests\test_auth.py:

from datetime import timedelta

import jwt

from full_stack_ai_shared.auth import (
    TokenError,
    create_access_token,
    decode_access_token,
)
from full_stack_ai_shared.security import TokenSettings


def create_token_settings() -> TokenSettings:
    return TokenSettings(
        secret_key="test-secret-key-that-is-at-least-32-characters",
        access_token_expire_minutes=30,
    )


def test_create_and_decode_access_token() -> None:
    settings = create_token_settings()

    token = create_access_token("user-123", settings)
    payload = decode_access_token(token, settings)

    assert payload.subject == "user-123"
    assert payload.issuer == settings.issuer
    assert payload.audience == settings.audience
    assert payload.expires_at > payload.issued_at

"""Tests for shared authentication utilities."""

from datetime import timedelta

import jwt
import pytest

from full_stack_ai_shared.auth import (
    TokenError,
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)
from full_stack_ai_shared.security import TokenSettings


def create_token_settings() -> TokenSettings:
    return TokenSettings(
        secret_key="test-secret-key-that-is-at-least-32-characters",
        access_token_expire_minutes=30,
    )


def test_hash_password() -> None:
    password = "StrongPassword123!"
    hashed_password = hash_password(password)

    assert hashed_password != password
    assert verify_password(password, hashed_password) is True


def test_verify_password_rejects_invalid_password() -> None:
    hashed_password = hash_password("CorrectPassword123!")

    assert verify_password(
        "WrongPassword123!",
        hashed_password,
    ) is False


def test_hash_password_uses_unique_salt() -> None:
    password = "StrongPassword123!"

    first_hash = hash_password(password)
    second_hash = hash_password(password)

    assert first_hash != second_hash
    assert verify_password(password, first_hash) is True
    assert verify_password(password, second_hash) is True


def test_hash_password_rejects_empty_password() -> None:
    with pytest.raises(
        ValueError,
        match="Password cannot be empty",
    ):
        hash_password("")


def test_verify_password_rejects_empty_values() -> None:
    assert verify_password("", "stored-hash") is False
    assert verify_password("password", "") is False


def test_create_and_decode_access_token() -> None:
    settings = create_token_settings()

    token = create_access_token("user-123", settings)
    payload = decode_access_token(token, settings)

    assert payload.subject == "user-123"
    assert payload.issuer == settings.issuer
    assert payload.audience == settings.audience
    assert payload.expires_at > payload.issued_at


def test_create_access_token_rejects_empty_subject() -> None:
    settings = create_token_settings()

    with pytest.raises(
        ValueError,
        match="Token subject cannot be empty",
    ):
        create_access_token("", settings)


def test_access_token_rejects_protected_claim_override() -> None:
    settings = create_token_settings()

    with pytest.raises(
        ValueError,
        match="cannot override protected claims",
    ):
        create_access_token(
            "user-123",
            settings,
            additional_claims={"sub": "other-user"},
        )


def test_decode_access_token_rejects_expired_token() -> None:
    settings = create_token_settings()

    token = create_access_token(
        "user-123",
        settings,
        expires_delta=timedelta(seconds=-1),
    )

    with pytest.raises(
        TokenError,
        match="Access token has expired",
    ):
        decode_access_token(token, settings)


def test_decode_access_token_rejects_invalid_signature() -> None:
    settings = create_token_settings()
    different_settings = TokenSettings(
        secret_key="different-secret-key-that-is-also-long-enough",
    )

    token = create_access_token("user-123", settings)

    with pytest.raises(
        TokenError,
        match="Access token is invalid",
    ):
        decode_access_token(token, different_settings)


def test_decode_access_token_rejects_missing_subject() -> None:
    settings = create_token_settings()

    token = jwt.encode(
        {
            "iat": 1_700_000_000,
            "exp": 4_000_000_000,
            "iss": settings.issuer,
            "aud": settings.audience,
        },
        settings.secret_key,
        algorithm=settings.algorithm,
    )

    with pytest.raises(
        TokenError,
        match="Access token subject is invalid",
    ):
        decode_access_token(token, settings)

## Run

uv run ruff format tests\test_auth.py
uv run ruff check .
uv run mypy src
uv run pytest -v

## Add reusable FastAPI bearer authentication

"""Reusable FastAPI authentication dependencies."""

from collections.abc import Callable
from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from full_stack_ai_shared.auth.tokens import (
    TokenError,
    TokenPayload,
    decode_access_token,
)
from full_stack_ai_shared.exceptions import ApplicationError
from full_stack_ai_shared.security import TokenSettings

bearer_scheme = HTTPBearer(auto_error=False)


def create_current_token_dependency(
    settings: TokenSettings,
) -> Callable[..., TokenPayload]:
    """Create a FastAPI dependency that validates bearer tokens."""

    def get_current_token(
        credentials: Annotated[
            HTTPAuthorizationCredentials | None,
            Depends(bearer_scheme),
        ],
    ) -> TokenPayload:
        if credentials is None:
            raise ApplicationError(
                "Authentication credentials were not provided.",
                code="not_authenticated",
                status_code=401,
            )

        if credentials.scheme.lower() != "bearer":
            raise ApplicationError(
                "Unsupported authentication scheme.",
                code="invalid_authentication_scheme",
                status_code=401,
            )

        try:
            return decode_access_token(
                credentials.credentials,
                settings,
            )
        except TokenError as exc:
            raise ApplicationError(
                str(exc),
                code="invalid_access_token",
                status_code=401,
            ) from exc

    return get_current_token

    ## Update: code src\full_stack_ai_shared\auth\__init__.py

    """Shared authentication utilities."""

from full_stack_ai_shared.auth.dependencies import (
    bearer_scheme,
    create_current_token_dependency,
)
from full_stack_ai_shared.auth.passwords import (
    hash_password,
    verify_password,
)
from full_stack_ai_shared.auth.tokens import (
    TokenError,
    TokenPayload,
    create_access_token,
    decode_access_token,
)

__all__ = [
    "TokenError",
    "TokenPayload",
    "bearer_scheme",
    "create_access_token",
    "create_current_token_dependency",
    "decode_access_token",
    "hash_password",
    "verify_password",
]

## code tests\test_auth.py:

"""Tests for shared authentication utilities."""

from datetime import timedelta
from typing import Annotated

import jwt
import pytest
from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from full_stack_ai_shared.auth import (
    TokenError,
    TokenPayload,
    create_access_token,
    create_current_token_dependency,
    decode_access_token,
    hash_password,
    verify_password,
)
from full_stack_ai_shared.exceptions import register_exception_handlers
from full_stack_ai_shared.logging import RequestLoggingMiddleware
from full_stack_ai_shared.security import TokenSettings


def create_token_settings() -> TokenSettings:
    """Return isolated token settings for tests."""

    return TokenSettings(
        secret_key="test-secret-key-that-is-at-least-32-characters",
        access_token_expire_minutes=30,
    )


def create_auth_test_app(settings: TokenSettings) -> FastAPI:
    """Create a FastAPI application with bearer authentication."""

    app = FastAPI()
    app.add_middleware(RequestLoggingMiddleware)
    register_exception_handlers(app)

    current_token = create_current_token_dependency(settings)

    @app.get("/protected")
    async def protected_route(
        token: Annotated[TokenPayload, Depends(current_token)],
    ) -> dict[str, str]:
        return {"subject": token.subject}

    return app


def test_hash_password() -> None:
    password = "StrongPassword123!"
    hashed_password = hash_password(password)

    assert hashed_password != password
    assert verify_password(password, hashed_password) is True


def test_verify_password_rejects_invalid_password() -> None:
    hashed_password = hash_password("CorrectPassword123!")

    assert verify_password(
        "WrongPassword123!",
        hashed_password,
    ) is False


def test_hash_password_uses_unique_salt() -> None:
    password = "StrongPassword123!"

    first_hash = hash_password(password)
    second_hash = hash_password(password)

    assert first_hash != second_hash
    assert verify_password(password, first_hash) is True
    assert verify_password(password, second_hash) is True


def test_hash_password_rejects_empty_password() -> None:
    with pytest.raises(
        ValueError,
        match="Password cannot be empty",
    ):
        hash_password("")


def test_verify_password_rejects_empty_values() -> None:
    assert verify_password("", "stored-hash") is False
    assert verify_password("password", "") is False


def test_create_and_decode_access_token() -> None:
    settings = create_token_settings()

    token = create_access_token("user-123", settings)
    payload = decode_access_token(token, settings)

    assert payload.subject == "user-123"
    assert payload.issuer == settings.issuer
    assert payload.audience == settings.audience
    assert payload.expires_at > payload.issued_at


def test_create_access_token_rejects_empty_subject() -> None:
    settings = create_token_settings()

    with pytest.raises(
        ValueError,
        match="Token subject cannot be empty",
    ):
        create_access_token("", settings)


def test_access_token_rejects_protected_claim_override() -> None:
    settings = create_token_settings()

    with pytest.raises(
        ValueError,
        match="cannot override protected claims",
    ):
        create_access_token(
            "user-123",
            settings,
            additional_claims={"sub": "other-user"},
        )


def test_decode_access_token_rejects_expired_token() -> None:
    settings = create_token_settings()

    token = create_access_token(
        "user-123",
        settings,
        expires_delta=timedelta(seconds=-1),
    )

    with pytest.raises(
        TokenError,
        match="Access token has expired",
    ):
        decode_access_token(token, settings)


def test_decode_access_token_rejects_invalid_signature() -> None:
    settings = create_token_settings()
    different_settings = TokenSettings(
        secret_key="different-secret-key-that-is-also-long-enough",
    )

    token = create_access_token("user-123", settings)

    with pytest.raises(
        TokenError,
        match="Access token is invalid",
    ):
        decode_access_token(token, different_settings)


def test_decode_access_token_rejects_missing_subject() -> None:
    settings = create_token_settings()

    token = jwt.encode(
        {
            "iat": 1_700_000_000,
            "exp": 4_000_000_000,
            "iss": settings.issuer,
            "aud": settings.audience,
        },
        settings.secret_key,
        algorithm=settings.algorithm,
    )

    with pytest.raises(
        TokenError,
        match="Access token subject is invalid",
    ):
        decode_access_token(token, settings)


def test_protected_route_accepts_valid_token() -> None:
    settings = create_token_settings()
    client = TestClient(create_auth_test_app(settings))
    token = create_access_token("user-123", settings)

    response = client.get(
        "/protected",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json() == {"subject": "user-123"}


def test_protected_route_rejects_missing_token() -> None:
    settings = create_token_settings()
    client = TestClient(create_auth_test_app(settings))

    response = client.get("/protected")
    payload = response.json()

    assert response.status_code == 401
    assert payload["errors"][0]["code"] == "not_authenticated"


def test_protected_route_rejects_invalid_token() -> None:
    settings = create_token_settings()
    client = TestClient(create_auth_test_app(settings))

    response = client.get(
        "/protected",
        headers={"Authorization": "Bearer invalid-token"},
    )
    payload = response.json()

    assert response.status_code == 401
    assert payload["errors"][0]["code"] == "invalid_access_token"

## Run

uv run ruff check .
uv run mypy src
uv run pytest -v

## commit the changes

cd ..\..
git add shared-infrastructure/python
git status
git commit -m "Add shared authentication and JWT framework"
git push origin main
git status

## Phase 2.6 — Shared Authorization (RBAC)

## Step 1 — Create the folder and files

New-Item src\full_stack_ai_shared\authorization -ItemType Directory -Force

New-Item src\full_stack_ai_shared\authorization\__init__.py -ItemType File -Force
New-Item src\full_stack_ai_shared\authorization\roles.py -ItemType File -Force
New-Item src\full_stack_ai_shared\authorization\permissions.py -ItemType File -Force
New-Item src\full_stack_ai_shared\authorization\dependencies.py -ItemType File -Force
New-Item src\full_stack_ai_shared\authorization\decorators.py -ItemType File -Force

New-Item tests\test_authorization.py -ItemType File -Force

## Step 2 — Create roles
code src\full_stack_ai_shared\authorization\roles.py

"""Application roles."""

from enum import StrEnum


class Role(StrEnum):
    ADMIN = "admin"
    ENGINEER = "engineer"
    ANALYST = "analyst"
    OPERATOR = "operator"
    AUDITOR = "auditor"
    VIEWER = "viewer"

## Step 3 — Create permissions
code src\full_stack_ai_shared\authorization\permissions.py

"""Permission definitions."""

from enum import StrEnum

from full_stack_ai_shared.authorization.roles import Role


class Permission(StrEnum):
    READ = "read"
    WRITE = "write"
    DELETE = "delete"
    ADMIN = "admin"
    EXECUTE = "execute"


ROLE_PERMISSIONS: dict[Role, set[Permission]] = {
    Role.ADMIN: {
        Permission.READ,
        Permission.WRITE,
        Permission.DELETE,
        Permission.ADMIN,
        Permission.EXECUTE,
    },
    Role.ENGINEER: {
        Permission.READ,
        Permission.WRITE,
        Permission.EXECUTE,
    },
    Role.ANALYST: {
        Permission.READ,
        Permission.EXECUTE,
    },
    Role.OPERATOR: {
        Permission.READ,
        Permission.WRITE,
    },
    Role.AUDITOR: {
        Permission.READ,
    },
    Role.VIEWER: {
        Permission.READ,
    },
}

## Step 4 — Export the module
code src\full_stack_ai_shared\authorization\__init__.py

"""Authorization utilities."""

from full_stack_ai_shared.authorization.permissions import (
    Permission,
    ROLE_PERMISSIONS,
)
from full_stack_ai_shared.authorization.roles import Role

__all__ = [
    "Permission",
    "ROLE_PERMISSIONS",
    "Role",
]

## Step 5 — Create authorization tests
code tests\test_authorization.py

"""Tests for authorization roles and permissions."""

from full_stack_ai_shared.authorization import (
    Permission,
    ROLE_PERMISSIONS,
    Role,
)


def test_admin_permissions() -> None:
    permissions = ROLE_PERMISSIONS[Role.ADMIN]

    assert Permission.ADMIN in permissions
    assert Permission.DELETE in permissions
    assert Permission.WRITE in permissions
    assert Permission.READ in permissions


def test_engineer_permissions() -> None:
    permissions = ROLE_PERMISSIONS[Role.ENGINEER]

    assert Permission.WRITE in permissions
    assert Permission.EXECUTE in permissions
    assert Permission.DELETE not in permissions


def test_viewer_permissions() -> None:
    permissions = ROLE_PERMISSIONS[Role.VIEWER]

    assert permissions == {Permission.READ}

## Verify

uv run ruff format .
uv run ruff check . --fix
uv run ruff check .
uv run mypy src
uv run pytest -v

## Add reusable permission dependencies
code src\full_stack_ai_shared\authorization\dependencies.py

"""FastAPI authorization dependencies."""

from collections.abc import Callable

from full_stack_ai_shared.auth import TokenPayload
from full_stack_ai_shared.authorization.permissions import (
    ROLE_PERMISSIONS,
    Permission,
)
from full_stack_ai_shared.authorization.roles import Role
from full_stack_ai_shared.exceptions import ApplicationError


def extract_roles(token: TokenPayload) -> set[Role]:
    """Extract validated roles from a token payload."""

    raw_roles = getattr(token, "roles", None)

    if raw_roles is None:
        return set()

    roles: set[Role] = set()

    for raw_role in raw_roles:
        try:
            roles.add(Role(raw_role))
        except ValueError:
            continue

    return roles


def require_permission(
    permission: Permission,
) -> Callable[[TokenPayload], TokenPayload]:
    """Create a dependency requiring a specific permission."""

    def dependency(token: TokenPayload) -> TokenPayload:
        roles = extract_roles(token)

        has_permission = any(
            permission in ROLE_PERMISSIONS.get(role, set())
            for role in roles
        )

        if not has_permission:
            raise ApplicationError(
                "You do not have permission to perform this action.",
                code="permission_denied",
                status_code=403,
            )

        return token

    return dependency

## code src\full_stack_ai_shared\auth\tokens.py

"""JWT access-token creation and validation."""

from datetime import UTC, datetime, timedelta
from typing import Any

import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from pydantic import BaseModel, Field

from full_stack_ai_shared.security import TokenSettings


class TokenPayload(BaseModel):
    """Validated JWT payload."""

    subject: str
    issued_at: datetime
    expires_at: datetime
    issuer: str
    audience: str
    roles: list[str] = Field(default_factory=list)


class TokenError(ValueError):
    """Raised when an access token cannot be validated."""


def create_access_token(
    subject: str,
    settings: TokenSettings,
    *,
    expires_delta: timedelta | None = None,
    additional_claims: dict[str, Any] | None = None,
) -> str:
    """Create a signed JWT access token."""

    if not subject.strip():
        raise ValueError("Token subject cannot be empty.")

    issued_at = datetime.now(UTC)
    expires_at = issued_at + (
        expires_delta or timedelta(minutes=settings.access_token_expire_minutes)
    )

    payload: dict[str, Any] = {
        "sub": subject,
        "iat": issued_at,
        "exp": expires_at,
        "iss": settings.issuer,
        "aud": settings.audience,
    }

    if additional_claims:
        protected_claims = {"sub", "iat", "exp", "iss", "aud"}
        conflicting_claims = protected_claims.intersection(additional_claims)

        if conflicting_claims:
            names = ", ".join(sorted(conflicting_claims))
            raise ValueError(
                f"Additional claims cannot override protected claims: {names}"
            )

        payload.update(additional_claims)

    return jwt.encode(
        payload,
        settings.secret_key,
        algorithm=settings.algorithm,
    )


def decode_access_token(
    token: str,
    settings: TokenSettings,
) -> TokenPayload:
    """Decode and validate a JWT access token."""

    if not token:
        raise TokenError("Access token cannot be empty.")

    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm],
            audience=settings.audience,
            issuer=settings.issuer,
        )
    except ExpiredSignatureError as exc:
        raise TokenError("Access token has expired.") from exc
    except InvalidTokenError as exc:
        raise TokenError("Access token is invalid.") from exc

    subject = payload.get("sub")

    if not isinstance(subject, str) or not subject:
        raise TokenError("Access token subject is invalid.")

    issued_at = payload.get("iat")
    expires_at = payload.get("exp")
    issuer = payload.get("iss")
    audience = payload.get("aud")
    raw_roles = payload.get("roles", [])

    if not isinstance(issued_at, int | float):
        raise TokenError("Access token issued-at claim is invalid.")

    if not isinstance(expires_at, int | float):
        raise TokenError("Access token expiration claim is invalid.")

    if not isinstance(issuer, str) or not issuer:
        raise TokenError("Access token issuer claim is invalid.")

    if not isinstance(audience, str) or not audience:
        raise TokenError("Access token audience claim is invalid.")

    if not isinstance(raw_roles, list) or not all(
        isinstance(role, str) for role in raw_roles
    ):
        raise TokenError("Access token roles claim is invalid.")

    return TokenPayload(
        subject=subject,
        issued_at=datetime.fromtimestamp(issued_at, tz=UTC),
        expires_at=datetime.fromtimestamp(expires_at, tz=UTC),
        issuer=issuer,
        audience=audience,
        roles=raw_roles,
    )

## Run

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## Add RBAC dependency tests

code tests\test_authorization.py

"""Tests for authorization roles and permissions."""

from datetime import UTC, datetime, timedelta

import pytest

from full_stack_ai_shared.auth import TokenPayload
from full_stack_ai_shared.authorization import (
    ROLE_PERMISSIONS,
    Permission,
    Role,
    extract_roles,
    require_permission,
)
from full_stack_ai_shared.exceptions import ApplicationError


def create_token_with_roles(*roles: Role) -> TokenPayload:
    """Create a token payload with assigned roles."""

    now = datetime.now(UTC)

    return TokenPayload(
        subject="user-123",
        issued_at=now,
        expires_at=now + timedelta(minutes=30),
        issuer="full-stack-ai-portfolio",
        audience="full-stack-ai-applications",
        roles=[role.value for role in roles],
    )


def test_admin_permissions() -> None:
    permissions = ROLE_PERMISSIONS[Role.ADMIN]

    assert Permission.ADMIN in permissions
    assert Permission.DELETE in permissions
    assert Permission.WRITE in permissions
    assert Permission.READ in permissions


def test_engineer_permissions() -> None:
    permissions = ROLE_PERMISSIONS[Role.ENGINEER]

    assert Permission.WRITE in permissions
    assert Permission.EXECUTE in permissions
    assert Permission.DELETE not in permissions


def test_viewer_permissions() -> None:
    permissions = ROLE_PERMISSIONS[Role.VIEWER]

    assert permissions == {Permission.READ}


def test_extract_roles() -> None:
    token = create_token_with_roles(
        Role.ADMIN,
        Role.ANALYST,
    )

    assert extract_roles(token) == {
        Role.ADMIN,
        Role.ANALYST,
    }


def test_extract_roles_ignores_unknown_roles() -> None:
    now = datetime.now(UTC)

    token = TokenPayload(
        subject="user-123",
        issued_at=now,
        expires_at=now + timedelta(minutes=30),
        issuer="full-stack-ai-portfolio",
        audience="full-stack-ai-applications",
        roles=["admin", "unknown-role"],
    )

    assert extract_roles(token) == {Role.ADMIN}


def test_require_permission_allows_authorized_role() -> None:
    token = create_token_with_roles(Role.ENGINEER)
    dependency = require_permission(Permission.WRITE)

    result = dependency(token)

    assert result is token


def test_require_permission_allows_admin() -> None:
    token = create_token_with_roles(Role.ADMIN)
    dependency = require_permission(Permission.DELETE)

    result = dependency(token)

    assert result is token


def test_require_permission_denies_unauthorized_role() -> None:
    token = create_token_with_roles(Role.VIEWER)
    dependency = require_permission(Permission.WRITE)

    with pytest.raises(ApplicationError) as exc_info:
        dependency(token)

    assert exc_info.value.status_code == 403
    assert exc_info.value.code == "permission_denied"


def test_require_permission_denies_token_without_roles() -> None:
    token = create_token_with_roles()
    dependency = require_permission(Permission.READ)

    with pytest.raises(ApplicationError) as exc_info:
        dependency(token)

    assert exc_info.value.status_code == 403
    assert exc_info.value.code == "permission_denied"

## code src\full_stack_ai_shared\authorization\__init__.py

"""Authorization utilities."""

from full_stack_ai_shared.authorization.dependencies import (
    extract_roles,
    require_permission,
)
from full_stack_ai_shared.authorization.permissions import (
    ROLE_PERMISSIONS,
    Permission,
)
from full_stack_ai_shared.authorization.roles import Role

__all__ = [
    "ROLE_PERMISSIONS",
    "Permission",
    "Role",
    "extract_roles",
    "require_permission",
]

## Run

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## Commit the RBAC framework run From the parent folder:

cd ..\..
git add shared-infrastructure/python
git status
git commit -m "Add shared role-based authorization framework"
git push origin main
git status

## FastAPI authentication + RBAC integration:

## cd shared-infrastructure\python

## code tests\test_authorization_api.py

"""Tests for FastAPI authentication and authorization integration."""

from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

from full_stack_ai_shared.auth import (
    TokenPayload,
    create_access_token,
    create_current_token_dependency,
)
from full_stack_ai_shared.authorization import (
    Permission,
    require_permission,
)
from full_stack_ai_shared.exceptions import register_exception_handlers
from full_stack_ai_shared.logging import RequestLoggingMiddleware
from full_stack_ai_shared.security import TokenSettings


def create_token_settings() -> TokenSettings:
    """Return token settings for API authorization tests."""

    return TokenSettings(
        secret_key="test-secret-key-that-is-at-least-32-characters",
        access_token_expire_minutes=30,
    )


def create_authorization_test_app(settings: TokenSettings) -> FastAPI:
    """Create a test application with authentication and RBAC."""

    app = FastAPI()
    app.add_middleware(RequestLoggingMiddleware)
    register_exception_handlers(app)

    current_token = create_current_token_dependency(settings)
    require_write = require_permission(Permission.WRITE)

    @app.get("/protected")
    async def protected_route(
        token: Annotated[TokenPayload, Depends(current_token)],
    ) -> dict[str, str]:
        return {"subject": token.subject}

    @app.post("/write")
    async def write_route(
        token: Annotated[TokenPayload, Depends(current_token)],
    ) -> dict[str, str]:
        authorized_token = require_write(token)

        return {
            "subject": authorized_token.subject,
            "status": "write-authorized",
        }

    return app


def test_engineer_can_access_write_endpoint() -> None:
    settings = create_token_settings()
    client = TestClient(create_authorization_test_app(settings))

    token = create_access_token(
        "engineer-123",
        settings,
        additional_claims={"roles": ["engineer"]},
    )

    response = client.post(
        "/write",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "subject": "engineer-123",
        "status": "write-authorized",
    }


def test_viewer_cannot_access_write_endpoint() -> None:
    settings = create_token_settings()
    client = TestClient(create_authorization_test_app(settings))

    token = create_access_token(
        "viewer-123",
        settings,
        additional_claims={"roles": ["viewer"]},
    )

    response = client.post(
        "/write",
        headers={"Authorization": f"Bearer {token}"},
    )
    payload = response.json()

    assert response.status_code == 403
    assert payload["success"] is False
    assert payload["errors"][0]["code"] == "permission_denied"


def test_missing_token_cannot_access_protected_endpoint() -> None:
    settings = create_token_settings()
    client = TestClient(create_authorization_test_app(settings))

    response = client.get("/protected")
    payload = response.json()

    assert response.status_code == 401
    assert payload["errors"][0]["code"] == "not_authenticated"


def test_admin_can_access_write_endpoint() -> None:
    settings = create_token_settings()
    client = TestClient(create_authorization_test_app(settings))

    token = create_access_token(
        "admin-123",
        settings,
        additional_claims={"roles": ["admin"]},
    )

    response = client.post(
        "/write",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "write-authorized"

## Run

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## commit

cd ..\..
git add shared-infrastructure/python
git commit -m "Add FastAPI authorization integration tests"
git push origin main
git status

## Phase 3 — Shared AI Foundation:


## Step 1 — Build the LLM Abstraction
New-Item src\full_stack_ai_shared\llm\base.py -ItemType File -Force
New-Item src\full_stack_ai_shared\llm\factory.py -ItemType File -Force
New-Item src\full_stack_ai_shared\llm\openai_provider.py -ItemType File -Force
New-Item src\full_stack_ai_shared\llm\ollama_provider.py -ItemType File -Force
New-Item src\full_stack_ai_shared\llm\anthropic_provider.py -ItemType File -Force

New-Item tests\test_llm.py -ItemType File -Force

# Step 2 — LLM Interface

code src\full_stack_ai_shared\llm\base.py

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

## update code src\full_stack_ai_shared\llm\__init__.py

"""Shared LLM abstractions."""

from full_stack_ai_shared.llm.base import (
    BaseLLMProvider,
    LLMMessage,
    LLMRequest,
    LLMResponse,
)

__all__ = [
    "BaseLLMProvider",
    "LLMMessage",
    "LLMRequest",
    "LLMResponse",
]

## code tests\test_llm.py

"""Tests for shared LLM abstractions."""

import pytest

from full_stack_ai_shared.llm import (
    BaseLLMProvider,
    LLMMessage,
    LLMRequest,
    LLMResponse,
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

## Verify:

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## Step 3 — Build the LLM provider factory
code src\full_stack_ai_shared\llm\factory.py

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
        raise UnsupportedLLMProviderError(
            f"Unsupported LLM provider: {name}"
        ) from exc

    return factory(**kwargs)


def list_llm_providers() -> tuple[str, ...]:
    """Return registered LLM provider names."""

    return tuple(sorted(_PROVIDER_REGISTRY))


def clear_llm_provider_registry() -> None:
    """Clear the provider registry.

    Intended primarily for isolated tests.
    """

    _PROVIDER_REGISTRY.clear()

## Update - code src\full_stack_ai_shared\llm\__init__.py

"""Shared LLM abstractions."""

from full_stack_ai_shared.llm.base import (
    BaseLLMProvider,
    LLMMessage,
    LLMRequest,
    LLMResponse,
)
from full_stack_ai_shared.llm.factory import (
    UnsupportedLLMProviderError,
    clear_llm_provider_registry,
    create_llm_provider,
    list_llm_providers,
    register_llm_provider,
)

__all__ = [
    "BaseLLMProvider",
    "LLMMessage",
    "LLMRequest",
    "LLMResponse",
    "UnsupportedLLMProviderError",
    "clear_llm_provider_registry",
    "create_llm_provider",
    "list_llm_providers",
    "register_llm_provider",
]

## code src\full_stack_ai_shared\llm\__init__.py

"""Shared LLM abstractions."""

from full_stack_ai_shared.llm.base import (
    BaseLLMProvider,
    LLMMessage,
    LLMRequest,
    LLMResponse,
)
from full_stack_ai_shared.llm.factory import (
    UnsupportedLLMProviderError,
    clear_llm_provider_registry,
    create_llm_provider,
    list_llm_providers,
    register_llm_provider,
)

__all__ = [
    "BaseLLMProvider",
    "LLMMessage",
    "LLMRequest",
    "LLMResponse",
    "UnsupportedLLMProviderError",
    "clear_llm_provider_registry",
    "create_llm_provider",
    "list_llm_providers",
    "register_llm_provider",
]

## Eun

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## Commit from parent folder:

cd ..\..
git add shared-infrastructure/python
git status
git commit -m "Add shared LLM abstraction and provider factory"
git push origin main
git status





