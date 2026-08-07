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

## Phase 3: Agent Framework
The next step is to build a reusable agent framework that every AI application in your portfolio will use.

## Build the shared Agent Framework that every AI platform in your portfolio will use.

## Step 1 — Navigate to the agents package
cd C:\projects\Full-Stack-AI-Portfolio\shared-infrastructure\python

## Step 2 — Create the directory structure
New-Item -ItemType Directory -Force src\full_stack_ai_shared\agents | Out-Null

## Step 3 — Create the files

New-Item src\full_stack_ai_shared\agents\__init__.py -ItemType File -Force
New-Item src\full_stack_ai_shared\agents\base.py -ItemType File -Force
New-Item src\full_stack_ai_shared\agents\state.py -ItemType File -Force
New-Item src\full_stack_ai_shared\agents\memory.py -ItemType File -Force
New-Item src\full_stack_ai_shared\agents\planner.py -ItemType File -Force
New-Item src\full_stack_ai_shared\agents\executor.py -ItemType File -Force
New-Item src\full_stack_ai_shared\agents\tools.py -ItemType File -Force
New-Item src\full_stack_ai_shared\agents\messages.py -ItemType File -Force

## Step 4 — Create tests
New-Item tests\test_agents.py -ItemType File -Force

## step 5 — Run the quality checks

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## Implement the base agent models
code src\full_stack_ai_shared\agents\base.py

"""Base abstractions for reusable AI agents."""

from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    """Input passed to an AI agent."""

    task: str = Field(min_length=1)
    context: dict[str, Any] = Field(default_factory=dict)


class AgentResult(BaseModel):
    """Standard result returned by an AI agent."""

    agent_name: str
    success: bool
    output: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class BaseAgent(ABC):
    """Base interface implemented by all portfolio agents."""

    def __init__(self, name: str) -> None:
        normalized_name = name.strip()

        if not normalized_name:
            raise ValueError("Agent name cannot be empty.")

        self._name = normalized_name

    @property
    def name(self) -> str:
        """Return the agent name."""

        return self._name

    @abstractmethod
    async def run(self, request: AgentRequest) -> AgentResult:
        """Execute an agent task and return a standard result."""

## Update - code src\full_stack_ai_shared\agents\__init__.py

"""Shared AI agent abstractions."""

from full_stack_ai_shared.agents.base import (
    AgentRequest,
    AgentResult,
    BaseAgent,
)

__all__ = [
    "AgentRequest",
    "AgentResult",
    "BaseAgent",
]

## Add - code tests\test_agents.py

"""Tests for shared agent abstractions."""

import pytest

from full_stack_ai_shared.agents import (
    AgentRequest,
    AgentResult,
    BaseAgent,
)


class EchoAgent(BaseAgent):
    """Simple test agent."""

    async def run(self, request: AgentRequest) -> AgentResult:
        return AgentResult(
            agent_name=self.name,
            success=True,
            output=f"Processed: {request.task}",
            metadata={"context_size": len(request.context)},
        )


def test_agent_request_defaults() -> None:
    request = AgentRequest(task="Analyze equipment health")

    assert request.task == "Analyze equipment health"
    assert request.context == {}


def test_agent_result() -> None:
    result = AgentResult(
        agent_name="diagnostic-agent",
        success=True,
        output="No critical anomaly detected.",
    )

    assert result.agent_name == "diagnostic-agent"
    assert result.success is True
    assert result.metadata == {}


def test_agent_rejects_empty_name() -> None:
    with pytest.raises(
        ValueError,
        match="Agent name cannot be empty",
    ):
        EchoAgent("")


@pytest.mark.asyncio
async def test_agent_run() -> None:
    agent = EchoAgent("echo-agent")
    request = AgentRequest(
        task="Inspect compressor vibration",
        context={"asset_id": "CMP-1001"},
    )

    result = await agent.run(request)

    assert agent.name == "echo-agent"
    assert result.success is True
    assert result.output == "Processed: Inspect compressor vibration"
    assert result.metadata["context_size"] == 1

## Run

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## Implement agent state:

## code src\full_stack_ai_shared\agents\state.py

"""Shared state models for AI-agent execution."""

from datetime import UTC, datetime
from enum import StrEnum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


class AgentStatus(StrEnum):
    """Supported agent execution states."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class AgentState(BaseModel):
    """Mutable execution state shared across agent workflow steps."""

    execution_id: str = Field(default_factory=lambda: str(uuid4()))
    status: AgentStatus = AgentStatus.PENDING
    current_step: str | None = None
    inputs: dict[str, Any] = Field(default_factory=dict)
    outputs: dict[str, Any] = Field(default_factory=dict)
    errors: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    def mark_running(self, step: str | None = None) -> None:
        """Mark the workflow as running."""

        self.status = AgentStatus.RUNNING
        self.current_step = step
        self.updated_at = datetime.now(UTC)

    def mark_completed(self, outputs: dict[str, Any] | None = None) -> None:
        """Mark the workflow as completed."""

        self.status = AgentStatus.COMPLETED
        self.current_step = None

        if outputs:
            self.outputs.update(outputs)

        self.updated_at = datetime.now(UTC)

    def mark_failed(self, error: str) -> None:
        """Mark the workflow as failed and record an error."""

        self.status = AgentStatus.FAILED
        self.current_step = None
        self.errors.append(error)
        self.updated_at = datetime.now(UTC)

## Update - code src\full_stack_ai_shared\agents\__init__.py

"""
Shared AI agent abstractions.

This package exposes the public API for the shared AI agent framework.
"""

from full_stack_ai_shared.agents.base import (
    AgentRequest,
    AgentResult,
    BaseAgent,
)
from full_stack_ai_shared.agents.state import (
    AgentState,
    AgentStatus,
)

__all__ = [
    "AgentRequest",
    "AgentResult",
    "AgentState",
    "AgentStatus",
    "BaseAgent",
]

## Append - code tests\test_agents.py

"""Tests for shared AI-agent abstractions and execution state."""

import pytest

from full_stack_ai_shared.agents import (
    AgentRequest,
    AgentResult,
    AgentState,
    AgentStatus,
    BaseAgent,
)


class EchoAgent(BaseAgent):
    """Simple agent implementation used for testing."""

    async def run(self, request: AgentRequest) -> AgentResult:
        """Return the submitted task as a successful result."""
        return AgentResult(
            agent_name=self.name,
            success=True,
            output=f"Processed: {request.task}",
            metadata={"context_size": len(request.context)},
        )


def test_agent_request_defaults() -> None:
    """AgentRequest should provide an empty context by default."""
    request = AgentRequest(task="Analyze equipment health")

    assert request.task == "Analyze equipment health"
    assert request.context == {}


def test_agent_result_defaults() -> None:
    """AgentResult should provide empty metadata by default."""
    result = AgentResult(
        agent_name="diagnostic-agent",
        success=True,
        output="No critical anomaly detected.",
    )

    assert result.agent_name == "diagnostic-agent"
    assert result.success is True
    assert result.output == "No critical anomaly detected."
    assert result.metadata == {}


def test_agent_rejects_empty_name() -> None:
    """BaseAgent should reject an empty agent name."""
    with pytest.raises(
        ValueError,
        match="Agent name cannot be empty",
    ):
        EchoAgent("")


@pytest.mark.asyncio
async def test_agent_run() -> None:
    """An agent should process a request and return an AgentResult."""
    agent = EchoAgent("echo-agent")
    request = AgentRequest(
        task="Inspect compressor vibration",
        context={"asset_id": "CMP-1001"},
    )

    result = await agent.run(request)

    assert agent.name == "echo-agent"
    assert result.agent_name == "echo-agent"
    assert result.success is True
    assert result.output == "Processed: Inspect compressor vibration"
    assert result.metadata == {"context_size": 1}


def test_agent_state_defaults() -> None:
    """AgentState should initialize with pending execution defaults."""
    state = AgentState()

    assert state.execution_id
    assert state.status == AgentStatus.PENDING
    assert state.current_step is None
    assert state.inputs == {}
    assert state.outputs == {}
    assert state.errors == []


def test_agent_state_marks_running() -> None:
    """AgentState should transition to running."""
    state = AgentState()

    state.mark_running("planning")

    assert state.status == AgentStatus.RUNNING
    assert state.current_step == "planning"


def test_agent_state_marks_completed() -> None:
    """AgentState should store outputs when execution completes."""
    state = AgentState()
    state.mark_running("execution")

    state.mark_completed({"result": "success"})

    assert state.status == AgentStatus.COMPLETED
    assert state.current_step is None
    assert state.outputs == {"result": "success"}
    assert state.errors == []


def test_agent_state_marks_failed() -> None:
    """AgentState should store an error when execution fails."""
    state = AgentState()
    state.mark_running("tool-execution")

    state.mark_failed("Tool invocation failed.")

    assert state.status == AgentStatus.FAILED
    assert state.current_step is None
    assert state.errors == ["Tool invocation failed."]

## Run

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## Implement shared agent memory: 

## code src\full_stack_ai_shared\agents\memory.py

"""In-memory storage for agent messages and working data."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class MemoryEntry(BaseModel):
    """Single value stored in agent memory."""

    key: str
    value: Any
    metadata: dict[str, Any] = Field(default_factory=dict)


class AgentMemory:
    """Simple reusable in-memory store for agent workflows."""

    def __init__(self) -> None:
        self._entries: dict[str, MemoryEntry] = {}

    def set(
        self,
        key: str,
        value: Any,
        *,
        metadata: dict[str, Any] | None = None,
    ) -> MemoryEntry:
        """Store or replace a memory entry."""

        normalized_key = key.strip()

        if not normalized_key:
            raise ValueError("Memory key cannot be empty.")

        entry = MemoryEntry(
            key=normalized_key,
            value=value,
            metadata=metadata or {},
        )

        self._entries[normalized_key] = entry
        return entry

    def get(self, key: str) -> MemoryEntry | None:
        """Return a memory entry by key."""

        return self._entries.get(key)

    def remove(self, key: str) -> MemoryEntry | None:
        """Remove and return a memory entry."""

        return self._entries.pop(key, None)

    def contains(self, key: str) -> bool:
        """Return whether a key exists in memory."""

        return key in self._entries

    def list_entries(self) -> list[MemoryEntry]:
        """Return all memory entries."""

        return list(self._entries.values())

    def clear(self) -> None:
        """Remove every entry from memory."""

        self._entries.clear()

    def __len__(self) -> int:
        """Return the number of memory entries."""

        return len(self._entries)

## Update - code src\full_stack_ai_shared\agents\__init__.py

"""
Shared AI agent abstractions.

This package exposes the public API for the shared AI agent framework,
including base agent interfaces, execution state, and agent memory.
"""

from full_stack_ai_shared.agents.base import (
    AgentRequest,
    AgentResult,
    BaseAgent,
)
from full_stack_ai_shared.agents.memory import (
    AgentMemory,
    MemoryEntry,
)
from full_stack_ai_shared.agents.state import (
    AgentState,
    AgentStatus,
)

__all__ = [
    "AgentMemory",
    "AgentRequest",
    "AgentResult",
    "AgentState",
    "AgentStatus",
    "BaseAgent",
    "MemoryEntry",
]

## Append - code tests\test_agents.py:

"""Tests for shared AI-agent abstractions, execution state, and memory."""

import pytest

from full_stack_ai_shared.agents import (
    AgentMemory,
    AgentRequest,
    AgentResult,
    AgentState,
    AgentStatus,
    BaseAgent,
)


class EchoAgent(BaseAgent):
    """Simple agent implementation used for testing."""

    async def run(self, request: AgentRequest) -> AgentResult:
        """Return the submitted task as a successful result."""
        return AgentResult(
            agent_name=self.name,
            success=True,
            output=f"Processed: {request.task}",
            metadata={"context_size": len(request.context)},
        )


def test_agent_request_defaults() -> None:
    """AgentRequest should provide an empty context by default."""
    request = AgentRequest(task="Analyze equipment health")

    assert request.task == "Analyze equipment health"
    assert request.context == {}


def test_agent_result_defaults() -> None:
    """AgentResult should provide empty metadata by default."""
    result = AgentResult(
        agent_name="diagnostic-agent",
        success=True,
        output="No critical anomaly detected.",
    )

    assert result.agent_name == "diagnostic-agent"
    assert result.success is True
    assert result.output == "No critical anomaly detected."
    assert result.metadata == {}


def test_agent_rejects_empty_name() -> None:
    """BaseAgent should reject an empty agent name."""
    with pytest.raises(
        ValueError,
        match="Agent name cannot be empty",
    ):
        EchoAgent("")


@pytest.mark.asyncio
async def test_agent_run() -> None:
    """An agent should process a request and return an AgentResult."""
    agent = EchoAgent("echo-agent")
    request = AgentRequest(
        task="Inspect compressor vibration",
        context={"asset_id": "CMP-1001"},
    )

    result = await agent.run(request)

    assert agent.name == "echo-agent"
    assert result.agent_name == "echo-agent"
    assert result.success is True
    assert result.output == "Processed: Inspect compressor vibration"
    assert result.metadata == {"context_size": 1}


def test_agent_state_defaults() -> None:
    """AgentState should initialize with pending execution defaults."""
    state = AgentState()

    assert state.execution_id
    assert state.status == AgentStatus.PENDING
    assert state.current_step is None
    assert state.inputs == {}
    assert state.outputs == {}
    assert state.errors == []


def test_agent_state_marks_running() -> None:
    """AgentState should transition to running."""
    state = AgentState()

    state.mark_running("planning")

    assert state.status == AgentStatus.RUNNING
    assert state.current_step == "planning"


def test_agent_state_marks_completed() -> None:
    """AgentState should store outputs when execution completes."""
    state = AgentState()
    state.mark_running("execution")

    state.mark_completed({"result": "success"})

    assert state.status == AgentStatus.COMPLETED
    assert state.current_step is None
    assert state.outputs == {"result": "success"}
    assert state.errors == []


def test_agent_state_marks_failed() -> None:
    """AgentState should store an error when execution fails."""
    state = AgentState()
    state.mark_running("tool-execution")

    state.mark_failed("Tool invocation failed.")

    assert state.status == AgentStatus.FAILED
    assert state.current_step is None
    assert state.errors == ["Tool invocation failed."]


def test_agent_memory_stores_and_reads_entry() -> None:
    """AgentMemory should store and retrieve an entry."""
    memory = AgentMemory()

    entry = memory.set(
        "asset_id",
        "CMP-1001",
        metadata={"source": "request"},
    )

    stored_entry = memory.get("asset_id")

    assert entry.key == "asset_id"
    assert stored_entry is not None
    assert stored_entry.value == "CMP-1001"
    assert stored_entry.metadata == {"source": "request"}
    assert memory.contains("asset_id") is True
    assert len(memory) == 1


def test_agent_memory_replaces_existing_entry() -> None:
    """AgentMemory should replace an entry with the same key."""
    memory = AgentMemory()

    memory.set("status", "pending")
    memory.set("status", "completed")

    entry = memory.get("status")

    assert entry is not None
    assert entry.value == "completed"
    assert len(memory) == 1


def test_agent_memory_removes_entry() -> None:
    """AgentMemory should remove and return an existing entry."""
    memory = AgentMemory()
    memory.set("temporary", 123)

    removed = memory.remove("temporary")

    assert removed is not None
    assert removed.value == 123
    assert memory.contains("temporary") is False
    assert len(memory) == 0


def test_agent_memory_lists_entries() -> None:
    """AgentMemory should list entries in insertion order."""
    memory = AgentMemory()
    memory.set("first", 1)
    memory.set("second", 2)

    entries = memory.list_entries()

    assert [entry.key for entry in entries] == ["first", "second"]


def test_agent_memory_clears_entries() -> None:
    """AgentMemory should clear all stored entries."""
    memory = AgentMemory()
    memory.set("first", 1)
    memory.set("second", 2)

    memory.clear()

    assert len(memory) == 0
    assert memory.list_entries() == []


def test_agent_memory_rejects_empty_key() -> None:
    """AgentMemory should reject an empty key."""
    memory = AgentMemory()

    with pytest.raises(
        ValueError,
        match="Memory key cannot be empty",
    ):
        memory.set("", "value")

## Run

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## Step 10 — Build the Shared RAG Package:

## Step 10.1 — Create the RAG Package Structure

## Create the RAG package directory:
New-Item `
    -ItemType Directory `
    -Force `
    src\full_stack_ai_shared\rag |
    Out-Null

## Create the initial Python files:

$ragFiles = @(
    "__init__.py",
    "models.py",
    "chunking.py",
    "embeddings.py",
    "vector_store.py",
    "retriever.py",
    "pipeline.py"
)

foreach ($file in $ragFiles) {
    New-Item `
        -ItemType File `
        -Force `
        "src\full_stack_ai_shared\rag\$file" |
        Out-Null
}

## Create test file:

New-Item `
    -ItemType File `
    -Force `
    tests\test_rag.py |
    Out-Null

## Verify the package structure:

Get-ChildItem `
    src\full_stack_ai_shared\rag `
    -Recurse

## Verify test file

Test-Path tests\test_rag.py
True

## Open the new package in VS Code:

## code src\full_stack_ai_shared\rag

## Run the existing test suite before adding code:  uv run pytest -v

## Step 10.2 — Build the RAG Data Models

## 1. Open models.py

## code src\full_stack_ai_shared\rag\models.py

```python
"""Core data models for retrieval-augmented generation workflows."""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class Document:
    """Represent a source document before text chunking."""

    content: str
    metadata: dict[str, Any] = field(default_factory=dict)
    document_id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        """Validate the document after initialization."""
        if not self.content.strip():
            raise ValueError("Document content must not be empty.")

        if not self.document_id.strip():
            raise ValueError("Document ID must not be empty.")


@dataclass(slots=True)
class DocumentChunk:
    """Represent a searchable chunk created from a source document."""

    document_id: str
    content: str
    chunk_index: int
    start_char: int
    end_char: int
    metadata: dict[str, Any] = field(default_factory=dict)
    chunk_id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        """Validate the document chunk after initialization."""
        if not self.document_id.strip():
            raise ValueError("Document ID must not be empty.")

        if not self.content.strip():
            raise ValueError("Document chunk content must not be empty.")

        if self.chunk_index < 0:
            raise ValueError("Chunk index must not be negative.")

        if self.start_char < 0:
            raise ValueError("Start character position must not be negative.")

        if self.end_char <= self.start_char:
            raise ValueError(
                "End character position must be greater than start character position."
            )

        if not self.chunk_id.strip():
            raise ValueError("Chunk ID must not be empty.")


@dataclass(slots=True)
class SearchResult:
    """Represent a document chunk returned by semantic retrieval."""

    chunk: DocumentChunk
    score: float

    def __post_init__(self) -> None:
        """Validate the search result after initialization."""
        if not 0.0 <= self.score <= 1.0:
            raise ValueError(
                "Search result score must be between 0.0 and 1.0."
            )
```


## 2.   Export the Models from rag/__init__.py

## code src\full_stack_ai_shared\rag\__init__.py

"""Shared retrieval-augmented generation abstractions."""

from full_stack_ai_shared.rag.models import (
    Document,
    DocumentChunk,
    SearchResult,
)

__all__ = [
    "Document",
    "DocumentChunk",
    "SearchResult",
]

## 3. Add the RAG Model Tests:  code tests\test_rag.py

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
## Run

## uv run ruff format .
## uv run ruff check .
## uv run mypy src
## uv run pytest tests\test_rag.py -v
## uv run pytest -v

## uv run python -c "from full_stack_ai_shared.rag import Document, DocumentChunk, SearchResult; print(Document.__name__, DocumentChunk.__name__, SearchResult.__name__)" ## VERIFY PUBLIC IMPORTS

## Run

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest tests\test_rag.py -v
uv run pytest -v

## Step 10.3 — Build the Text Chunking Engine

## code src\full_stack_ai_shared\rag\chunking.py

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

2. Update the RAG public API - code src\full_stack_ai_shared\rag\__init__.py

"""Shared retrieval-augmented generation abstractions."""

from full_stack_ai_shared.rag.chunking import TextChunker
from full_stack_ai_shared.rag.models import Document, DocumentChunk

__all__ = [
    "Document",
    "DocumentChunk",
    "TextChunker",
]

## 3. Add text-chunking tests

## code tests/test_rag.py

## Target public API

from full_stack_ai_shared.rag import (
    Document,
    DocumentChunk,
    TextChunker,
)

document = Document(
    content="Very long enterprise document..."
)

chunker = TextChunker(
    chunk_size=500,
    overlap=100,
)

chunks = chunker.chunk(document)

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## Step 11 — Build the Shared Vector Store Layer

## Step 11.1 — Create the Files

New-Item -ItemType File -Force `
    src\full_stack_ai_shared\rag\embeddings.py, `
    src\full_stack_ai_shared\rag\vector_store.py, `
    tests\test_vector_store.py

## Verify files

Get-ChildItem src\full_stack_ai_shared\rag
Get-ChildItem tests\test_vector_store.py

## Step 11.2 — Update models.py code src\full_stack_ai_shared\rag\models.py

"""Core data models for retrieval-augmented generation workflows."""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class Document:
    """Represent a source document before text chunking."""

    content: str
    metadata: dict[str, Any] = field(default_factory=dict)
    document_id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        """Validate the document after initialization."""
        if not self.content.strip():
            raise ValueError("Document content must not be empty.")

        if not self.document_id.strip():
            raise ValueError("Document ID must not be empty.")


@dataclass(slots=True)
class DocumentChunk:
    """Represent a searchable chunk created from a source document."""

    document_id: str
    content: str
    chunk_index: int
    start_char: int
    end_char: int
    metadata: dict[str, Any] = field(default_factory=dict)
    chunk_id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        """Validate the document chunk after initialization."""
        if not self.document_id.strip():
            raise ValueError("Document ID must not be empty.")

        if not self.content.strip():
            raise ValueError("Chunk content must not be empty.")

        if self.chunk_index < 0:
            raise ValueError("Chunk index cannot be negative.")

        if self.start_char < 0:
            raise ValueError("Start character cannot be negative.")

        if self.end_char < self.start_char:
            raise ValueError(
                "End character must be greater than or equal to start character."
            )

        if not self.chunk_id.strip():
            raise ValueError("Chunk ID must not be empty.")


@dataclass(slots=True, frozen=True)
class SearchResult:
    """Represent a vector-search result and its similarity score."""

    chunk: DocumentChunk
    score: float

    def __post_init__(self) -> None:
        """Validate the search result."""
        if not -1.0 <= self.score <= 1.0:
            raise ValueError(
                "Search result score must be between -1.0 and 1.0."
            )

## Step 11.3 — Create embeddings.py     code src\full_stack_ai_shared\rag\embeddings.py

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
            raise ValueError(
                "Embedding dimensions must be greater than zero."
            )

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

## Pasted text(432).txt
Document
Step 11.2 — Update models.py

Open:

code src\full_stack_ai_shared\rag\models.py

Replace the entire file with:

"""Core data models for retrieval-augmented generation workflows."""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class Document:
    """Represent a source document before text chunking."""

    content: str
    metadata: dict[str, Any] = field(default_factory=dict)
    document_id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        """Validate the document after initialization."""
        if not self.content.strip():
            raise ValueError("Document content must not be empty.")

        if not self.document_id.strip():
            raise ValueError("Document ID must not be empty.")


@dataclass(slots=True)
class DocumentChunk:
    """Represent a searchable chunk created from a source document."""

    document_id: str
    content: str
    chunk_index: int
    start_char: int
    end_char: int
    metadata: dict[str, Any] = field(default_factory=dict)
    chunk_id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        """Validate the document chunk after initialization."""
        if not self.document_id.strip():
            raise ValueError("Document ID must not be empty.")

        if not self.content.strip():
            raise ValueError("Chunk content must not be empty.")

        if self.chunk_index < 0:
            raise ValueError("Chunk index cannot be negative.")

        if self.start_char < 0:
            raise ValueError("Start character cannot be negative.")

        if self.end_char < self.start_char:
            raise ValueError(
                "End character must be greater than or equal to start character."
            )

        if not self.chunk_id.strip():
            raise ValueError("Chunk ID must not be empty.")


@dataclass(slots=True, frozen=True)
class SearchResult:
    """Represent a vector-search result and its similarity score."""

    chunk: DocumentChunk
    score: float

    def __post_init__(self) -> None:
        """Validate the search result."""
        if not -1.0 <= self.score <= 1.0:
            raise ValueError(
                "Search result score must be between -1.0 and 1.0."
            )

Save the file with:

Ctrl + S

Do not run tests yet because SearchResult is not exported and the vector-store files are still empty.

Next: Step 11.3 — Create embeddings.py.

next
Step 11.3 — Create embeddings.py

Open:

code src\full_stack_ai_shared\rag\embeddings.py

Replace the entire file with:

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
            raise ValueError(
                "Embedding dimensions must be greater than zero."
            )

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

Step 11.4 — Create vector_store.py      code src\full_stack_ai_shared\rag\vector_store.py

"""Vector-store abstractions and in-memory implementation."""

from abc import ABC, abstractmethod
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from math import sqrt
from typing import Any

from full_stack_ai_shared.rag.embeddings import EmbeddingProvider
from full_stack_ai_shared.rag.models import DocumentChunk, SearchResult


class VectorStore(ABC):
    """Define the interface implemented by vector stores."""

    @abstractmethod
    def add(self, chunks: Sequence[DocumentChunk]) -> None:
        """Add document chunks to the vector store."""

    @abstractmethod
    def search(
        self,
        query: str,
        *,
        top_k: int = 5,
        metadata_filter: Mapping[str, Any] | None = None,
    ) -> list[SearchResult]:
        """Search for chunks similar to a query."""

    @abstractmethod
    def delete(self, chunk_ids: Sequence[str]) -> int:
        """Delete chunks and return the number removed."""

    @abstractmethod
    def clear(self) -> None:
        """Remove all stored chunks."""

    @abstractmethod
    def count(self) -> int:
        """Return the number of stored chunks."""


@dataclass(slots=True)
class _StoredVector:
    """Store a document chunk and its embedding."""

    chunk: DocumentChunk
    embedding: list[float]


class InMemoryVectorStore(VectorStore):
    """Store embeddings in memory and perform cosine-similarity search."""

    def __init__(self, embedding_provider: EmbeddingProvider) -> None:
        """Initialize the in-memory vector store."""
        self._embedding_provider = embedding_provider
        self._vectors: dict[str, _StoredVector] = {}

    def add(self, chunks: Sequence[DocumentChunk]) -> None:
        """Add or replace document chunks in the vector store."""
        if not chunks:
            return

        embeddings = self._embedding_provider.embed_texts(
            [chunk.content for chunk in chunks]
        )

        for chunk, embedding in zip(chunks, embeddings, strict=True):
            self._validate_embedding(embedding)

            self._vectors[chunk.chunk_id] = _StoredVector(
                chunk=chunk,
                embedding=embedding,
            )

    def search(
        self,
        query: str,
        *,
        top_k: int = 5,
        metadata_filter: Mapping[str, Any] | None = None,
    ) -> list[SearchResult]:
        """Search stored chunks using cosine similarity."""
        if not query.strip():
            raise ValueError("Search query must not be empty.")

        if top_k <= 0:
            raise ValueError("top_k must be greater than zero.")

        query_embedding = self._embedding_provider.embed_text(query)
        self._validate_embedding(query_embedding)

        results: list[SearchResult] = []

        for stored_vector in self._vectors.values():
            if not self._matches_metadata(
                stored_vector.chunk,
                metadata_filter,
            ):
                continue

            score = self._cosine_similarity(
                query_embedding,
                stored_vector.embedding,
            )

            results.append(
                SearchResult(
                    chunk=stored_vector.chunk,
                    score=score,
                )
            )

        results.sort(
            key=lambda result: result.score,
            reverse=True,
        )

        return results[:top_k]

    def delete(self, chunk_ids: Sequence[str]) -> int:
        """Delete chunks and return the number removed."""
        deleted_count = 0

        for chunk_id in set(chunk_ids):
            if self._vectors.pop(chunk_id, None) is not None:
                deleted_count += 1

        return deleted_count

    def clear(self) -> None:
        """Remove all stored vectors."""
        self._vectors.clear()

    def count(self) -> int:
        """Return the number of stored vectors."""
        return len(self._vectors)

    def get(self, chunk_id: str) -> DocumentChunk | None:
        """Return a stored chunk by its identifier."""
        stored_vector = self._vectors.get(chunk_id)

        if stored_vector is None:
            return None

        return stored_vector.chunk

    def _validate_embedding(
        self,
        embedding: Sequence[float],
    ) -> None:
        """Validate that an embedding matches provider dimensions."""
        if len(embedding) != self._embedding_provider.dimensions:
            raise ValueError(
                "Embedding dimensions do not match the configured provider."
            )

    @staticmethod
    def _matches_metadata(
        chunk: DocumentChunk,
        metadata_filter: Mapping[str, Any] | None,
    ) -> bool:
        """Return whether a chunk matches requested metadata."""
        if metadata_filter is None:
            return True

        return all(
            chunk.metadata.get(key) == expected_value
            for key, expected_value in metadata_filter.items()
        )

    @staticmethod
    def _cosine_similarity(
        first: Sequence[float],
        second: Sequence[float],
    ) -> float:
        """Calculate cosine similarity between two vectors."""
        if len(first) != len(second):
            raise ValueError("Vectors must have matching dimensions.")

        dot_product = sum(
            first_value * second_value
            for first_value, second_value in zip(
                first,
                second,
                strict=True,
            )
        )
        first_magnitude = sqrt(
            sum(value * value for value in first)
        )
        second_magnitude = sqrt(
            sum(value * value for value in second)
        )

        if first_magnitude == 0 or second_magnitude == 0:
            return 0.0

        score = dot_product / (
            first_magnitude * second_magnitude
        )

        return max(-1.0, min(1.0, score))

## Step 11.5 — Update the Public RAG API    code src\full_stack_ai_shared\rag\__init__.py

"""Shared retrieval-augmented generation abstractions."""

from full_stack_ai_shared.rag.chunking import TextChunker
from full_stack_ai_shared.rag.embeddings import (
    EmbeddingProvider,
    HashEmbeddingProvider,
)
from full_stack_ai_shared.rag.models import (
    Document,
    DocumentChunk,
    SearchResult,
)
from full_stack_ai_shared.rag.vector_store import (
    InMemoryVectorStore,
    VectorStore,
)

__all__ = [
    "Document",
    "DocumentChunk",
    "EmbeddingProvider",
    "HashEmbeddingProvider",
    "InMemoryVectorStore",
    "SearchResult",
    "TextChunker",
    "VectorStore",
]

## Run import check
uv run python -c "from full_stack_ai_shared.rag import HashEmbeddingProvider, InMemoryVectorStore, SearchResult; print('RAG vector API imports passed')"
RAG vector API imports passed

## Step 11.6 — Add test_vector_store.py     code tests\test_vector_store.py

"""Tests for shared embedding and vector-store components."""

import pytest

from full_stack_ai_shared.rag import (
    DocumentChunk,
    HashEmbeddingProvider,
    InMemoryVectorStore,
)


def create_chunk(
    content: str,
    chunk_index: int,
    *,
    metadata: dict[str, str] | None = None,
    chunk_id: str | None = None,
) -> DocumentChunk:
    """Create a document chunk for vector-store tests."""
    if chunk_id is None:
        return DocumentChunk(
            document_id="document-123",
            content=content,
            chunk_index=chunk_index,
            start_char=0,
            end_char=len(content),
            metadata=metadata or {},
        )

    return DocumentChunk(
        document_id="document-123",
        content=content,
        chunk_index=chunk_index,
        start_char=0,
        end_char=len(content),
        metadata=metadata or {},
        chunk_id=chunk_id,
    )


def test_hash_embedding_provider_returns_expected_dimensions() -> None:
    """Embedding provider should return the configured vector size."""
    provider = HashEmbeddingProvider(dimensions=32)

    embedding = provider.embed_text("Predictive maintenance analysis")

    assert len(embedding) == 32


def test_hash_embedding_provider_is_deterministic() -> None:
    """Identical text should produce identical vectors."""
    provider = HashEmbeddingProvider(dimensions=32)

    first_embedding = provider.embed_text("Equipment vibration")
    second_embedding = provider.embed_text("Equipment vibration")

    assert first_embedding == second_embedding


def test_hash_embedding_provider_rejects_invalid_dimensions() -> None:
    """Embedding dimensions must be greater than zero."""
    with pytest.raises(
        ValueError,
        match="Embedding dimensions must be greater than zero.",
    ):
        HashEmbeddingProvider(dimensions=0)


def test_hash_embedding_provider_rejects_empty_text() -> None:
    """Empty text should not be embedded."""
    provider = HashEmbeddingProvider()

    with pytest.raises(
        ValueError,
        match="Text to embed must not be empty.",
    ):
        provider.embed_text("   ")


def test_vector_store_adds_chunks() -> None:
    """Vector store should add document chunks."""
    store = InMemoryVectorStore(HashEmbeddingProvider())

    chunks = [
        create_chunk("Pump vibration is elevated.", 0),
        create_chunk("Motor temperature is normal.", 1),
    ]

    store.add(chunks)

    assert store.count() == 2


def test_vector_store_returns_chunk_by_id() -> None:
    """Vector store should retrieve a chunk by identifier."""
    store = InMemoryVectorStore(HashEmbeddingProvider())
    chunk = create_chunk(
        "Bearing inspection is required.",
        0,
        chunk_id="chunk-123",
    )

    store.add([chunk])

    stored_chunk = store.get("chunk-123")

    assert stored_chunk == chunk


def test_vector_store_search_returns_ranked_results() -> None:
    """Search should return results ordered by similarity."""
    store = InMemoryVectorStore(HashEmbeddingProvider(dimensions=64))

    vibration_chunk = create_chunk(
        "Pump vibration indicates bearing wear.",
        0,
    )
    finance_chunk = create_chunk(
        "Quarterly finance report and revenue forecast.",
        1,
    )

    store.add([vibration_chunk, finance_chunk])

    results = store.search(
        "pump vibration bearing",
        top_k=2,
    )

    assert len(results) == 2
    assert results[0].score >= results[1].score
    assert results[0].chunk == vibration_chunk


def test_vector_store_limits_search_results() -> None:
    """Search should honor the requested top-k limit."""
    store = InMemoryVectorStore(HashEmbeddingProvider())

    store.add(
        [
            create_chunk("Pump maintenance record.", 0),
            create_chunk("Motor maintenance record.", 1),
            create_chunk("Compressor maintenance record.", 2),
        ]
    )

    results = store.search("maintenance", top_k=2)

    assert len(results) == 2


def test_vector_store_filters_by_metadata() -> None:
    """Search should filter chunks using metadata values."""
    store = InMemoryVectorStore(HashEmbeddingProvider())

    pump_chunk = create_chunk(
        "Pump vibration maintenance record.",
        0,
        metadata={
            "asset_type": "pump",
            "site": "los-angeles",
        },
    )
    motor_chunk = create_chunk(
        "Motor vibration maintenance record.",
        1,
        metadata={
            "asset_type": "motor",
            "site": "los-angeles",
        },
    )

    store.add([pump_chunk, motor_chunk])

    results = store.search(
        "vibration maintenance",
        metadata_filter={"asset_type": "pump"},
    )

    assert len(results) == 1
    assert results[0].chunk == pump_chunk


def test_vector_store_replaces_existing_chunk() -> None:
    """Adding the same chunk ID should replace its stored value."""
    store = InMemoryVectorStore(HashEmbeddingProvider())

    original_chunk = create_chunk(
        "Original maintenance content.",
        0,
        chunk_id="shared-chunk-id",
    )
    updated_chunk = create_chunk(
        "Updated maintenance content.",
        0,
        chunk_id="shared-chunk-id",
    )

    store.add([original_chunk])
    store.add([updated_chunk])

    assert store.count() == 1
    assert store.get("shared-chunk-id") == updated_chunk


def test_vector_store_deletes_chunks() -> None:
    """Vector store should delete chunks by identifier."""
    store = InMemoryVectorStore(HashEmbeddingProvider())

    first_chunk = create_chunk(
        "First chunk.",
        0,
        chunk_id="chunk-1",
    )
    second_chunk = create_chunk(
        "Second chunk.",
        1,
        chunk_id="chunk-2",
    )

    store.add([first_chunk, second_chunk])

    deleted_count = store.delete(["chunk-1"])

    assert deleted_count == 1
    assert store.count() == 1
    assert store.get("chunk-1") is None
    assert store.get("chunk-2") == second_chunk


def test_vector_store_clears_all_chunks() -> None:
    """Vector store should remove every stored chunk."""
    store = InMemoryVectorStore(HashEmbeddingProvider())

    store.add(
        [
            create_chunk("First chunk.", 0),
            create_chunk("Second chunk.", 1),
        ]
    )

    store.clear()

    assert store.count() == 0


@pytest.mark.parametrize(
    ("query", "top_k", "expected_message"),
    [
        ("", 5, "Search query must not be empty."),
        ("   ", 5, "Search query must not be empty."),
        ("maintenance", 0, "top_k must be greater than zero."),
        ("maintenance", -1, "top_k must be greater than zero."),
    ],
)
def test_vector_store_rejects_invalid_search_parameters(
    query: str,
    top_k: int,
    expected_message: str,
) -> None:
    """Search should reject invalid query parameters."""
    store = InMemoryVectorStore(HashEmbeddingProvider())

    with pytest.raises(ValueError, match=expected_message):
        store.search(query, top_k=top_k)

## Run 

uv run pytest tests\test_vector_store.py -v

## uv run ruff format .
## uv run ruff check .
## uv run mypy src
## uv run pytest -v

Project Progress

You have completed:

✅ Step 1–9: Core shared infrastructure
✅ Step 10: Shared RAG Package
✅ Step 10.3: Text Chunking Engine
✅ Step 11: Shared Vector Store Layer

Total test suite: 98 passing tests.

## Step 12 — Build the Shared RAG Retrieval Service

## This layer will combine everything built into a single reusable service:

## Create the new service and test files:

New-Item -ItemType File -Force `
    src\full_stack_ai_shared\rag\service.py, `
    tests\test_rag_service.py

Files that will be created or updated:

## code src\full_stack_ai_shared\rag\service.py

"""High-level retrieval-augmented generation service."""

from collections.abc import Mapping
from typing import Any

from full_stack_ai_shared.rag.chunking import TextChunker
from full_stack_ai_shared.rag.models import (
    Document,
    DocumentChunk,
    SearchResult,
)
from full_stack_ai_shared.rag.vector_store import InMemoryVectorStore


class RAGService:
    """Coordinate document chunking, storage, and semantic retrieval."""

    def __init__(
        self,
        *,
        chunker: TextChunker,
        vector_store: InMemoryVectorStore,
    ) -> None:
        """Initialize the retrieval service."""
        self._chunker = chunker
        self._vector_store = vector_store
        self._document_chunks: dict[str, set[str]] = {}

    @property
    def chunker(self) -> TextChunker:
        """Return the configured text chunker."""
        return self._chunker

    @property
    def vector_store(self) -> InMemoryVectorStore:
        """Return the configured vector store."""
        return self._vector_store

    def ingest(self, document: Document) -> list[DocumentChunk]:
        """Chunk and index a document."""
        chunks = self._chunker.chunk(document)
        self._vector_store.add(chunks)

        previous_chunk_ids = self._document_chunks.get(document.document_id, set())
        current_chunk_ids = {chunk.chunk_id for chunk in chunks}

        stale_chunk_ids = previous_chunk_ids - current_chunk_ids
        if stale_chunk_ids:
            self._vector_store.delete(list(stale_chunk_ids))

        self._document_chunks[document.document_id] = current_chunk_ids

        return chunks

    def retrieve(
        self,
        query: str,
        *,
        top_k: int = 5,
        metadata_filter: Mapping[str, Any] | None = None,
    ) -> list[SearchResult]:
        """Retrieve document chunks that are most relevant to a query."""
        if not query.strip():
            raise ValueError("Search query must not be empty.")

        if top_k <= 0:
            raise ValueError("top_k must be greater than zero.")

        return self._vector_store.search(
            query,
            top_k=top_k,
            metadata_filter=metadata_filter,
        )

    def get_chunk(self, chunk_id: str) -> DocumentChunk | None:
        """Return a stored document chunk by its identifier."""
        if not chunk_id.strip():
            raise ValueError("Chunk ID must not be empty.")

        return self._vector_store.get(chunk_id)

    def delete_document(self, document_id: str) -> int:
        """Delete all chunks associated with a source document."""
        if not document_id.strip():
            raise ValueError("Document ID must not be empty.")

        chunk_ids = self._document_chunks.pop(document_id, set())

        if not chunk_ids:
            return 0

        self._vector_store.delete(list(chunk_ids))

        return len(chunk_ids)

    def clear(self) -> None:
        """Remove every indexed chunk from the service."""
        self._vector_store.clear()
        self._document_chunks.clear()

## Update public API:

## code src\full_stack_ai_shared\rag\__init__.py

"""Shared retrieval-augmented generation abstractions."""

from full_stack_ai_shared.rag.chunking import TextChunker
from full_stack_ai_shared.rag.embeddings import (
    EmbeddingProvider,
    HashEmbeddingProvider,
)
from full_stack_ai_shared.rag.models import (
    Document,
    DocumentChunk,
    SearchResult,
)
from full_stack_ai_shared.rag.service import RAGService
from full_stack_ai_shared.rag.vector_store import InMemoryVectorStore

__all__ = [
    "Document",
    "DocumentChunk",
    "EmbeddingProvider",
    "HashEmbeddingProvider",
    "InMemoryVectorStore",
    "RAGService",
    "SearchResult",
    "TextChunker",
]

## code tests\test_rag_service.py

"""Tests for the high-level RAG retrieval service."""

import pytest

from full_stack_ai_shared.rag import (
    Document,
    HashEmbeddingProvider,
    InMemoryVectorStore,
    RAGService,
    TextChunker,
)


def create_rag_service(
    *,
    chunk_size: int = 100,
    overlap: int = 20,
) -> RAGService:
    """Create a RAG service configured for testing."""
    embedding_provider = HashEmbeddingProvider(dimensions=32)

    vector_store = InMemoryVectorStore(
        embedding_provider=embedding_provider,
    )

    chunker = TextChunker(
        chunk_size=chunk_size,
        overlap=overlap,
    )

    return RAGService(
        chunker=chunker,
        vector_store=vector_store,
    )


def test_rag_service_exposes_configured_components() -> None:
    """RAGService should expose its chunker and vector store."""
    chunker = TextChunker(
        chunk_size=100,
        overlap=20,
    )

    vector_store = InMemoryVectorStore(
        embedding_provider=HashEmbeddingProvider(dimensions=32),
    )

    service = RAGService(
        chunker=chunker,
        vector_store=vector_store,
    )

    assert service.chunker is chunker
    assert service.vector_store is vector_store


def test_rag_service_ingests_document() -> None:
    """Ingesting a document should chunk and index its content."""
    service = create_rag_service()

    document = Document(
        content="Compressor maintenance requires regular vibration monitoring.",
        metadata={
            "asset_type": "compressor",
            "department": "maintenance",
        },
    )

    chunks = service.ingest(document)

    assert len(chunks) == 1
    assert chunks[0].document_id == document.document_id
    assert chunks[0].content == document.content
    assert chunks[0].metadata["asset_type"] == "compressor"
    assert chunks[0].metadata["department"] == "maintenance"
    assert chunks[0].metadata["chunk_index"] == 0
    assert chunks[0].metadata["start_char"] == 0
    assert chunks[0].metadata["end_char"] == len(document.content)

    stored_chunk = service.get_chunk(chunks[0].chunk_id)

    assert stored_chunk == chunks[0]


def test_rag_service_ingests_multiple_chunks() -> None:
    """Long documents should be split and indexed as multiple chunks."""
    service = create_rag_service(
        chunk_size=40,
        overlap=10,
    )

    document = Document(
        content=(
            "Industrial compressors require vibration monitoring, "
            "temperature analysis, pressure inspection, and scheduled "
            "preventive maintenance."
        ),
    )

    chunks = service.ingest(document)

    assert len(chunks) > 1

    for chunk in chunks:
        assert service.get_chunk(chunk.chunk_id) == chunk


def test_rag_service_retrieves_relevant_chunks() -> None:
    """The service should return chunks relevant to a search query."""
    service = create_rag_service()

    compressor_document = Document(
        content=(
            "Compressor maintenance includes vibration analysis "
            "and bearing inspection."
        ),
        metadata={"asset_type": "compressor"},
    )

    pump_document = Document(
        content=(
            "Centrifugal pump maintenance includes seal replacement "
            "and flow inspection."
        ),
        metadata={"asset_type": "pump"},
    )

    service.ingest(compressor_document)
    service.ingest(pump_document)

    results = service.retrieve(
        "compressor vibration maintenance",
        top_k=1,
    )

    assert len(results) == 1
    assert results[0].chunk.document_id == compressor_document.document_id
    assert results[0].chunk.metadata["asset_type"] == "compressor"


def test_rag_service_limits_retrieval_results() -> None:
    """Retrieval should respect the requested result limit."""
    service = create_rag_service()

    documents = [
        Document(content="Compressor maintenance and vibration monitoring."),
        Document(content="Pump maintenance and seal inspection."),
        Document(content="Motor maintenance and temperature monitoring."),
    ]

    for document in documents:
        service.ingest(document)

    results = service.retrieve(
        "maintenance monitoring",
        top_k=2,
    )

    assert len(results) == 2


def test_rag_service_filters_retrieval_by_metadata() -> None:
    """Retrieval should support metadata filtering."""
    service = create_rag_service()

    compressor_document = Document(
        content="Inspect compressor vibration and bearing temperature.",
        metadata={
            "asset_type": "compressor",
            "site": "los-angeles",
        },
    )

    pump_document = Document(
        content="Inspect pump vibration and bearing temperature.",
        metadata={
            "asset_type": "pump",
            "site": "los-angeles",
        },
    )

    service.ingest(compressor_document)
    service.ingest(pump_document)

    results = service.retrieve(
        "bearing vibration inspection",
        top_k=5,
        metadata_filter={"asset_type": "pump"},
    )

    assert len(results) == 1
    assert results[0].chunk.document_id == pump_document.document_id
    assert results[0].chunk.metadata["asset_type"] == "pump"


def test_rag_service_returns_chunk_by_id() -> None:
    """A stored chunk should be retrievable by its identifier."""
    service = create_rag_service()

    document = Document(
        content="Enterprise asset-health documentation.",
    )

    chunks = service.ingest(document)

    stored_chunk = service.get_chunk(chunks[0].chunk_id)

    assert stored_chunk == chunks[0]


def test_rag_service_returns_none_for_unknown_chunk() -> None:
    """An unknown chunk identifier should return None."""
    service = create_rag_service()

    assert service.get_chunk("unknown-chunk-id") is None


def test_rag_service_deletes_document_chunks() -> None:
    """Deleting a document should remove all of its stored chunks."""
    service = create_rag_service(
        chunk_size=40,
        overlap=10,
    )

    document = Document(
        content=(
            "Compressor vibration monitoring identifies bearing wear. "
            "Temperature monitoring identifies lubrication problems."
        ),
    )

    chunks = service.ingest(document)

    deleted_count = service.delete_document(document.document_id)

    assert deleted_count == len(chunks)

    for chunk in chunks:
        assert service.get_chunk(chunk.chunk_id) is None


def test_rag_service_delete_document_preserves_other_documents() -> None:
    """Deleting one document should not remove unrelated chunks."""
    service = create_rag_service()

    first_document = Document(
        content="Compressor vibration monitoring procedures.",
    )

    second_document = Document(
        content="Pump seal inspection procedures.",
    )

    first_chunks = service.ingest(first_document)
    second_chunks = service.ingest(second_document)

    deleted_count = service.delete_document(first_document.document_id)

    assert deleted_count == len(first_chunks)
    assert service.get_chunk(first_chunks[0].chunk_id) is None
    assert service.get_chunk(second_chunks[0].chunk_id) == second_chunks[0]


def test_rag_service_delete_unknown_document_returns_zero() -> None:
    """Deleting an unknown document should report no deleted chunks."""
    service = create_rag_service()

    deleted_count = service.delete_document("unknown-document-id")

    assert deleted_count == 0


def test_rag_service_reingests_existing_document() -> None:
    """Reingesting a document should replace its previous chunks."""
    service = create_rag_service(
        chunk_size=50,
        overlap=10,
    )

    original_document = Document(
        document_id="maintenance-document",
        content=(
            "Original compressor maintenance instructions "
            "for vibration inspection."
        ),
    )

    original_chunks = service.ingest(original_document)

    updated_document = Document(
        document_id="maintenance-document",
        content=(
            "Updated compressor maintenance instructions "
            "for temperature monitoring."
        ),
    )

    updated_chunks = service.ingest(updated_document)

    for chunk in original_chunks:
        assert service.get_chunk(chunk.chunk_id) is None

    for chunk in updated_chunks:
        assert service.get_chunk(chunk.chunk_id) == chunk


def test_rag_service_clear_removes_all_chunks() -> None:
    """Clearing the service should remove every indexed chunk."""
    service = create_rag_service()

    first_chunks = service.ingest(
        Document(content="Compressor maintenance documentation.")
    )

    second_chunks = service.ingest(
        Document(content="Pump maintenance documentation.")
    )

    service.clear()

    for chunk in first_chunks + second_chunks:
        assert service.get_chunk(chunk.chunk_id) is None


@pytest.mark.parametrize(
    ("query", "error_message"),
    [
        ("", "Search query must not be empty."),
        ("   ", "Search query must not be empty."),
    ],
)
def test_rag_service_rejects_empty_query(
    query: str,
    error_message: str,
) -> None:
    """Retrieval should reject empty search queries."""
    service = create_rag_service()

    with pytest.raises(ValueError, match=error_message):
        service.retrieve(query)


@pytest.mark.parametrize("top_k", [0, -1])
def test_rag_service_rejects_invalid_top_k(top_k: int) -> None:
    """Retrieval should reject non-positive result limits."""
    service = create_rag_service()

    with pytest.raises(
        ValueError,
        match="top_k must be greater than zero.",
    ):
        service.retrieve(
            "compressor maintenance",
            top_k=top_k,
        )


@pytest.mark.parametrize(
    ("chunk_id", "error_message"),
    [
        ("", "Chunk ID must not be empty."),
        ("   ", "Chunk ID must not be empty."),
    ],
)
def test_rag_service_rejects_empty_chunk_id(
    chunk_id: str,
    error_message: str,
) -> None:
    """Chunk lookup should reject empty identifiers."""
    service = create_rag_service()

    with pytest.raises(ValueError, match=error_message):
        service.get_chunk(chunk_id)


@pytest.mark.parametrize(
    ("document_id", "error_message"),
    [
        ("", "Document ID must not be empty."),
        ("   ", "Document ID must not be empty."),
    ],
)
def test_rag_service_rejects_empty_document_id(
    document_id: str,
    error_message: str,
) -> None:
    """Document deletion should reject empty identifiers."""
    service = create_rag_service()

    with pytest.raises(ValueError, match=error_message):
        service.delete_document(document_id)


## rUN

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest tests\test_rag_service.py -v


## RAG package:

src/full_stack_ai_shared/rag/
├── __init__.py
├── chunking.py
├── embeddings.py
├── models.py
├── service.py
└── vector_store.py

## Tests:

tests/
├── test_rag.py
├── test_rag_service.py
└── test_vector_store.py

## Step 12.4 — Validate the Complete Shared RAG Package

## Run the complete RAG test suite:

## uv run pytest tests\test_rag.py tests\test_vector_store.py tests\test_ra

## Run

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## Step 13 — Shared RAG Generation Pipeline:

## Create these files

New-Item -ItemType File -Force `
    src\full_stack_ai_shared\rag\generation.py, `
    tests\test_rag_generation.py

## Step 13.2 — Implement generation.py

## 
"""Shared retrieval-augmented generation service."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

from full_stack_ai_shared.rag.models import SearchResult
from full_stack_ai_shared.rag.service import RAGService


@dataclass(slots=True)
class RAGRequest:
    """Represent a retrieval-augmented generation request."""

    query: str
    top_k: int = 5
    metadata_filter: Mapping[str, Any] | None = None

    def __post_init__(self) -> None:
        """Validate the request."""
        if not self.query.strip():
            raise ValueError("Query must not be empty.")

        if self.top_k <= 0:
            raise ValueError("top_k must be greater than zero.")


@dataclass(slots=True)
class RAGResponse:
    """Represent the response returned by the RAG generation service."""

    answer: str
    search_results: list[SearchResult] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


class RAGGenerationService:
    """Generate answers from retrieved document context."""

    def __init__(self, rag_service: RAGService) -> None:
        """Initialize the generation service."""
        self._rag_service = rag_service

    @property
    def rag_service(self) -> RAGService:
        """Return the configured retrieval service."""
        return self._rag_service

    def generate(self, request: RAGRequest) -> RAGResponse:
        """Generate an answer using retrieved document chunks."""
        search_results = self._rag_service.retrieve(
            request.query,
            top_k=request.top_k,
            metadata_filter=request.metadata_filter,
        )

        if not search_results:
            return RAGResponse(
                answer="No relevant information found.",
                search_results=[],
                sources=[],
            )

        context = "\n\n".join(
            result.chunk.content for result in search_results
        )

        answer = (
            "Generated answer based on retrieved context:\n\n"
            f"{context}"
        )

        sources = list(
            {
                result.chunk.document_id
                for result in search_results
            }
        )

        return RAGResponse(
            answer=answer,
            search_results=search_results,
            sources=sources,
            metadata={
                "retrieved_chunks": len(search_results),
            },
        
## code src\full_stack_ai_shared\rag\__init__.py

"""Shared retrieval-augmented generation abstractions."""

from full_stack_ai_shared.rag.chunking import TextChunker
from full_stack_ai_shared.rag.embeddings import (
    EmbeddingProvider,
    HashEmbeddingProvider,
)
from full_stack_ai_shared.rag.generation import (
    RAGGenerationService,
    RAGRequest,
    RAGResponse,
)
from full_stack_ai_shared.rag.models import (
    Document,
    DocumentChunk,
    SearchResult,
)
from full_stack_ai_shared.rag.service import RAGService
from full_stack_ai_shared.rag.vector_store import InMemoryVectorStore

__all__ = [
    "Document",
    "DocumentChunk",
    "EmbeddingProvider",
    "HashEmbeddingProvider",
    "InMemoryVectorStore",
    "RAGGenerationService",
    "RAGRequest",
    "RAGResponse",
    "RAGService",
    "SearchResult",
    "TextChunker",
]

## code tests\test_rag_generation.py

"""Tests for the shared RAG generation service."""

import pytest

from full_stack_ai_shared.rag import (
    Document,
    HashEmbeddingProvider,
    InMemoryVectorStore,
    RAGGenerationService,
    RAGRequest,
    RAGResponse,
    RAGService,
    TextChunker,
)


def create_generation_service() -> RAGGenerationService:
    """Create a RAG generation service configured for testing."""
    embedding_provider = HashEmbeddingProvider(dimensions=32)

    vector_store = InMemoryVectorStore(
        embedding_provider=embedding_provider,
    )

    rag_service = RAGService(
        chunker=TextChunker(
            chunk_size=100,
            overlap=20,
        ),
        vector_store=vector_store,
    )

    return RAGGenerationService(rag_service=rag_service)


def test_rag_request_defaults() -> None:
    """RAGRequest should provide default retrieval settings."""
    request = RAGRequest(
        query="How should compressor bearings be maintained?"
    )

    assert request.query == "How should compressor bearings be maintained?"
    assert request.top_k == 5
    assert request.metadata_filter is None


def test_rag_request_accepts_custom_values() -> None:
    """RAGRequest should accept custom retrieval settings."""
    request = RAGRequest(
        query="How should pump seals be inspected?",
        top_k=3,
        metadata_filter={"asset_type": "pump"},
    )

    assert request.query == "How should pump seals be inspected?"
    assert request.top_k == 3
    assert request.metadata_filter == {"asset_type": "pump"}


@pytest.mark.parametrize("query", ["", "   "])
def test_rag_request_rejects_empty_query(query: str) -> None:
    """RAGRequest should reject empty queries."""
    with pytest.raises(
        ValueError,
        match="Query must not be empty.",
    ):
        RAGRequest(query=query)


@pytest.mark.parametrize("top_k", [0, -1])
def test_rag_request_rejects_invalid_top_k(top_k: int) -> None:
    """RAGRequest should reject non-positive result limits."""
    with pytest.raises(
        ValueError,
        match="top_k must be greater than zero.",
    ):
        RAGRequest(
            query="Compressor maintenance",
            top_k=top_k,
        )


def test_rag_response_defaults() -> None:
    """RAGResponse should provide empty result collections by default."""
    response = RAGResponse(
        answer="Generated maintenance answer.",
    )

    assert response.answer == "Generated maintenance answer."
    assert response.search_results == []
    assert response.sources == []
    assert response.metadata == {}


def test_generation_service_exposes_rag_service() -> None:
    """The generation service should expose its retrieval service."""
    generation_service = create_generation_service()

    assert isinstance(generation_service.rag_service, RAGService)


def test_generation_service_returns_no_information_response() -> None:
    """Generation should return a fallback when no chunks are available."""
    generation_service = create_generation_service()

    response = generation_service.generate(
        RAGRequest(
            query="How should compressor bearings be maintained?",
        )
    )

    assert response.answer == "No relevant information found."
    assert response.search_results == []
    assert response.sources == []
    assert response.metadata == {}


def test_generation_service_generates_answer_from_retrieved_context() -> None:
    """Generation should build an answer from retrieved chunks."""
    generation_service = create_generation_service()

    document = Document(
        content=(
            "Compressor bearings should be inspected for vibration, "
            "temperature, and lubrication condition."
        ),
        metadata={
            "asset_type": "compressor",
            "source": "maintenance-manual",
        },
    )

    generation_service.rag_service.ingest(document)

    response = generation_service.generate(
        RAGRequest(
            query="How should compressor bearings be maintained?",
            top_k=1,
        )
    )

    assert isinstance(response, RAGResponse)
    assert response.answer.startswith(
        "Generated answer based on retrieved context:"
    )
    assert document.content in response.answer
    assert len(response.search_results) == 1
    assert response.search_results[0].chunk.document_id == document.document_id
    assert response.sources == [document.document_id]
    assert response.metadata == {"retrieved_chunks": 1}


def test_generation_service_returns_unique_sources() -> None:
    """Generation should return each source document only once."""
    generation_service = create_generation_service()

    document = Document(
        content=(
            "Compressor vibration should be monitored regularly. "
            "Bearing temperature should also be checked frequently. "
            "Lubrication condition should be inspected during maintenance."
        ),
    )

    generation_service.rag_service.ingest(document)

    response = generation_service.generate(
        RAGRequest(
            query="compressor bearing maintenance",
            top_k=5,
        )
    )

    assert response.sources == [document.document_id]


def test_generation_service_filters_context_by_metadata() -> None:
    """Generation should pass metadata filters to retrieval."""
    generation_service = create_generation_service()

    compressor_document = Document(
        content="Inspect compressor bearings and vibration levels.",
        metadata={"asset_type": "compressor"},
    )

    pump_document = Document(
        content="Inspect pump seals and flow conditions.",
        metadata={"asset_type": "pump"},
    )

    generation_service.rag_service.ingest(compressor_document)
    generation_service.rag_service.ingest(pump_document)

    response = generation_service.generate(
        RAGRequest(
            query="inspection procedures",
            top_k=5,
            metadata_filter={"asset_type": "pump"},
        )
    )

    assert len(response.search_results) == 1
    assert response.search_results[0].chunk.document_id == (
        pump_document.document_id
    )
    assert response.sources == [pump_document.document_id]
    assert pump_document.content in response.answer
    assert compressor_document.content not in response.answer


def test_generation_service_respects_top_k() -> None:
    """Generation should limit the number of retrieved chunks."""
    generation_service = create_generation_service()

    documents = [
        Document(content="Compressor maintenance documentation."),
        Document(content="Pump maintenance documentation."),
        Document(content="Motor maintenance documentation."),
    ]

    for document in documents:
        generation_service.rag_service.ingest(document)

    response = generation_service.generate(
        RAGRequest(
            query="maintenance documentation",
            top_k=2,
        )
    )

    assert len(response.search_results) == 2
    assert response.metadata["retrieved_chunks"] == 2

## Run

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest tests\test_rag_generation.py -v
uv run pytest tests\test_rag.py tests\test_vector_store.py tests\test_rag_service.py tests\test_rag_generation.py -v

# Built reusable infrastructure:

✅ AI Agents
✅ Authentication & Authorization
✅ Configuration
✅ Database
✅ Logging
✅ LLM abstraction
✅ Complete RAG pipeline (retrieval + generation)

## Step 14 — Shared AI Tool Framework:

## Step 14.1 — Create the Tool Package Structure

## Package folder

New-Item -ItemType Directory -Force `
    src\full_stack_ai_shared\tools | Out-Null

## create source files

$toolFiles = @(
    "src\full_stack_ai_shared\tools\__init__.py",
    "src\full_stack_ai_shared\tools\base.py",
    "src\full_stack_ai_shared\tools\context.py",
    "src\full_stack_ai_shared\tools\exceptions.py",
    "src\full_stack_ai_shared\tools\function.py",
    "src\full_stack_ai_shared\tools\models.py",
    "src\full_stack_ai_shared\tools\registry.py"
)

foreach ($file in $toolFiles) {
    New-Item -ItemType File -Force $file | Out-Null
}

## Create Test files

$testFiles = @(
    "tests\test_tool_models.py",
    "tests\test_function_tool.py",
    "tests\test_tool_registry.py"
)

foreach ($file in $testFiles) {
    New-Item -ItemType File -Force $file | Out-Null
}

## Verify Structure

Get-ChildItem src\full_stack_ai_shared\tools
Get-ChildItem tests\test_tool*

## Step 14.2 — Build the Tool Data Models

## code src\full_stack_ai_shared\tools\models.py

"""Data models for shared AI tool execution."""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class ToolDefinition:
    """Describe a tool exposed to an AI agent."""

    name: str
    description: str
    input_schema: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate the tool definition."""
        if not self.name.strip():
            raise ValueError("Tool name must not be empty.")

        if not self.description.strip():
            raise ValueError("Tool description must not be empty.")


@dataclass(slots=True)
class ToolRequest:
    """Represent a request to execute a registered tool."""

    tool_name: str
    arguments: dict[str, Any] = field(default_factory=dict)
    request_id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        """Validate the tool request."""
        if not self.tool_name.strip():
            raise ValueError("Tool name must not be empty.")

        if not self.request_id.strip():
            raise ValueError("Request ID must not be empty.")


@dataclass(slots=True)
class ToolResult:
    """Represent the result of a tool execution."""

    tool_name: str
    success: bool
    output: Any = None
    error: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    request_id: str | None = None

    def __post_init__(self) -> None:
        """Validate the tool result."""
        if not self.tool_name.strip():
            raise ValueError("Tool name must not be empty.")

        if self.success and self.error is not None:
            raise ValueError(
                "Successful tool results must not contain an error."
            )

        if not self.success and not self.error:
            raise ValueError(
                "Failed tool results must contain an error message."
            )

## code tests\test_tool_models.py

"""Tests for shared AI tool data models."""

import pytest

from full_stack_ai_shared.tools.models import (
    ToolDefinition,
    ToolRequest,
    ToolResult,
)


def test_tool_definition_defaults() -> None:
    """ToolDefinition should provide an empty input schema."""
    definition = ToolDefinition(
        name="asset_lookup",
        description="Look up an industrial asset.",
    )

    assert definition.name == "asset_lookup"
    assert definition.description == "Look up an industrial asset."
    assert definition.input_schema == {}


def test_tool_definition_rejects_empty_name() -> None:
    """ToolDefinition should reject an empty name."""
    with pytest.raises(ValueError, match="Tool name must not be empty"):
        ToolDefinition(
            name=" ",
            description="Valid description.",
        )


def test_tool_definition_rejects_empty_description() -> None:
    """ToolDefinition should reject an empty description."""
    with pytest.raises(
        ValueError,
        match="Tool description must not be empty",
    ):
        ToolDefinition(
            name="asset_lookup",
            description=" ",
        )


def test_tool_request_defaults() -> None:
    """ToolRequest should generate an identifier and empty arguments."""
    request = ToolRequest(tool_name="asset_lookup")

    assert request.tool_name == "asset_lookup"
    assert request.arguments == {}
    assert request.request_id


def test_tool_request_accepts_arguments() -> None:
    """ToolRequest should store tool arguments."""
    request = ToolRequest(
        tool_name="asset_lookup",
        arguments={"asset_id": "PUMP-101"},
    )

    assert request.arguments == {"asset_id": "PUMP-101"}


def test_tool_request_rejects_empty_tool_name() -> None:
    """ToolRequest should reject an empty tool name."""
    with pytest.raises(ValueError, match="Tool name must not be empty"):
        ToolRequest(tool_name=" ")


def test_successful_tool_result() -> None:
    """ToolResult should store successful tool output."""
    result = ToolResult(
        tool_name="asset_lookup",
        success=True,
        output={"asset_id": "PUMP-101"},
    )

    assert result.tool_name == "asset_lookup"
    assert result.success is True
    assert result.output == {"asset_id": "PUMP-101"}
    assert result.error is None
    assert result.metadata == {}


def test_failed_tool_result() -> None:
    """ToolResult should store failure details."""
    result = ToolResult(
        tool_name="asset_lookup",
        success=False,
        error="Asset was not found.",
    )

    assert result.success is False
    assert result.output is None
    assert result.error == "Asset was not found."


def test_successful_result_rejects_error() -> None:
    """Successful results should not contain errors."""
    with pytest.raises(
        ValueError,
        match="Successful tool results must not contain an error",
    ):
        ToolResult(
            tool_name="asset_lookup",
            success=True,
            error="Unexpected error.",
        )


def test_failed_result_requires_error() -> None:
    """Failed results should require an error message."""
    with pytest.raises(
        ValueError,
        match="Failed tool results must contain an error message",
    ):
        ToolResult(
            tool_name="asset_lookup",
            success=False,
        )

## Run

uv run ruff format src\full_stack_ai_shared\tools\models.py tests\test_tool_models.py
uv run ruff check src\full_stack_ai_shared\tools\models.py tests\test_tool_models.py
uv run mypy src
uv run pytest tests\test_tool_models.py -v

## Step 14.3 — Create Tool Exceptions

code src\full_stack_ai_shared\tools\exceptions.py

"""Exceptions raised by the shared AI tool framework."""


class ToolError(Exception):
    """Base exception for all shared tool framework errors."""


class ToolNotFoundError(ToolError):
    """Raised when a requested tool is not registered."""

    def __init__(self, tool_name: str) -> None:
        """Initialize the missing-tool error."""
        super().__init__(f"Tool '{tool_name}' is not registered.")
        self.tool_name = tool_name


class ToolAlreadyRegisteredError(ToolError):
    """Raised when a tool name is registered more than once."""

    def __init__(self, tool_name: str) -> None:
        """Initialize the duplicate-registration error."""
        super().__init__(f"Tool '{tool_name}' is already registered.")
        self.tool_name = tool_name


class ToolExecutionError(ToolError):
    """Raised when a tool fails during execution."""

    def __init__(
        self,
        tool_name: str,
        message: str,
    ) -> None:
        """Initialize the tool execution error."""
        super().__init__(f"Tool '{tool_name}' execution failed: {message}")
        self.tool_name = tool_name
        self.message = message

## code tests\test_tool_exceptions.py

"""Tests for shared AI tool exceptions."""

from full_stack_ai_shared.tools.exceptions import (
    ToolAlreadyRegisteredError,
    ToolError,
    ToolExecutionError,
    ToolNotFoundError,
)


def test_tool_not_found_error() -> None:
    """ToolNotFoundError should include the missing tool name."""
    error = ToolNotFoundError("asset_lookup")

    assert isinstance(error, ToolError)
    assert error.tool_name == "asset_lookup"
    assert str(error) == "Tool 'asset_lookup' is not registered."


def test_tool_already_registered_error() -> None:
    """ToolAlreadyRegisteredError should include the duplicate tool name."""
    error = ToolAlreadyRegisteredError("asset_lookup")

    assert isinstance(error, ToolError)
    assert error.tool_name == "asset_lookup"
    assert str(error) == "Tool 'asset_lookup' is already registered."


def test_tool_execution_error() -> None:
    """ToolExecutionError should preserve execution failure details."""
    error = ToolExecutionError(
        tool_name="asset_lookup",
        message="Database connection failed.",
    )

    assert isinstance(error, ToolError)
    assert error.tool_name == "asset_lookup"
    assert error.message == "Database connection failed."
    assert (
        str(error)
        == "Tool 'asset_lookup' execution failed: Database connection failed."
    )

## Run

uv run ruff format `
    src\full_stack_ai_shared\tools\exceptions.py `
    tests\test_tool_exceptions.py

uv run ruff check `
    src\full_stack_ai_shared\tools\exceptions.py `
    tests\test_tool_exceptions.py

uv run mypy src
uv run pytest tests\test_tool_exceptions.py -v

## Step 14.4 — Build the Tool Execution Context

"""Execution context for shared AI tools."""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class ToolContext:
    """Provide shared execution data to an AI tool."""

    execution_id: str = field(default_factory=lambda: str(uuid4()))
    agent_name: str | None = None
    user_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate the tool execution context."""
        if not self.execution_id.strip():
            raise ValueError("Execution ID must not be empty.")

        if self.agent_name is not None and not self.agent_name.strip():
            raise ValueError("Agent name must not be empty.")

        if self.user_id is not None and not self.user_id.strip():
            raise ValueError("User ID must not be empty.")

    def get_metadata(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """Return a metadata value or the provided default."""
        return self.metadata.get(key, default)

    def set_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """Add or update a metadata value."""
        if not key.strip():
            raise ValueError("Metadata key must not be empty.")

        self.metadata[key] = value

## code tests\test_tool_context.py

"""Tests for shared AI tool execution context."""

import pytest

from full_stack_ai_shared.tools.context import ToolContext


def test_tool_context_defaults() -> None:
    """ToolContext should provide generated and empty default values."""
    context = ToolContext()

    assert context.execution_id
    assert context.agent_name is None
    assert context.user_id is None
    assert context.metadata == {}


def test_tool_context_accepts_execution_details() -> None:
    """ToolContext should store agent, user, and metadata values."""
    context = ToolContext(
        execution_id="execution-123",
        agent_name="maintenance-agent",
        user_id="user-456",
        metadata={"environment": "test"},
    )

    assert context.execution_id == "execution-123"
    assert context.agent_name == "maintenance-agent"
    assert context.user_id == "user-456"
    assert context.metadata == {"environment": "test"}


def test_tool_context_gets_metadata_value() -> None:
    """ToolContext should return stored metadata."""
    context = ToolContext(
        metadata={"asset_id": "PUMP-101"},
    )

    assert context.get_metadata("asset_id") == "PUMP-101"


def test_tool_context_returns_metadata_default() -> None:
    """ToolContext should return a default for missing metadata."""
    context = ToolContext()

    assert context.get_metadata("asset_id", "UNKNOWN") == "UNKNOWN"


def test_tool_context_sets_metadata_value() -> None:
    """ToolContext should add and update metadata."""
    context = ToolContext()

    context.set_metadata("region", "west")
    assert context.metadata == {"region": "west"}

    context.set_metadata("region", "central")
    assert context.metadata == {"region": "central"}


def test_tool_context_rejects_empty_execution_id() -> None:
    """ToolContext should reject an empty execution identifier."""
    with pytest.raises(
        ValueError,
        match="Execution ID must not be empty",
    ):
        ToolContext(execution_id=" ")


def test_tool_context_rejects_empty_agent_name() -> None:
    """ToolContext should reject an empty provided agent name."""
    with pytest.raises(
        ValueError,
        match="Agent name must not be empty",
    ):
        ToolContext(agent_name=" ")


def test_tool_context_rejects_empty_user_id() -> None:
    """ToolContext should reject an empty provided user identifier."""
    with pytest.raises(
        ValueError,
        match="User ID must not be empty",
    ):
        ToolContext(user_id=" ")


def test_tool_context_rejects_empty_metadata_key() -> None:
    """ToolContext should reject an empty metadata key."""
    context = ToolContext()

    with pytest.raises(
        ValueError,
        match="Metadata key must not be empty",
    ):
        context.set_metadata(" ", "value")

## New-Item -ItemType File -Force tests\test_tool_context.py | Out-Null
code tests\test_tool_context.py

"""Tests for shared AI tool execution context."""

import pytest

from full_stack_ai_shared.tools.context import ToolContext


def test_tool_context_defaults() -> None:
    """ToolContext should provide generated and empty default values."""
    context = ToolContext()

    assert context.execution_id
    assert context.agent_name is None
    assert context.user_id is None
    assert context.metadata == {}


def test_tool_context_accepts_execution_details() -> None:
    """ToolContext should store agent, user, and metadata values."""
    context = ToolContext(
        execution_id="execution-123",
        agent_name="maintenance-agent",
        user_id="user-456",
        metadata={"environment": "test"},
    )

    assert context.execution_id == "execution-123"
    assert context.agent_name == "maintenance-agent"
    assert context.user_id == "user-456"
    assert context.metadata == {"environment": "test"}


def test_tool_context_gets_metadata_value() -> None:
    """ToolContext should return stored metadata."""
    context = ToolContext(
        metadata={"asset_id": "PUMP-101"},
    )

    assert context.get_metadata("asset_id") == "PUMP-101"


def test_tool_context_returns_metadata_default() -> None:
    """ToolContext should return a default for missing metadata."""
    context = ToolContext()

    assert context.get_metadata("asset_id", "UNKNOWN") == "UNKNOWN"


def test_tool_context_sets_metadata_value() -> None:
    """ToolContext should add and update metadata."""
    context = ToolContext()

    context.set_metadata("region", "west")
    assert context.metadata == {"region": "west"}

    context.set_metadata("region", "central")
    assert context.metadata == {"region": "central"}


def test_tool_context_rejects_empty_execution_id() -> None:
    """ToolContext should reject an empty execution identifier."""
    with pytest.raises(
        ValueError,
        match="Execution ID must not be empty",
    ):
        ToolContext(execution_id=" ")


def test_tool_context_rejects_empty_agent_name() -> None:
    """ToolContext should reject an empty provided agent name."""
    with pytest.raises(
        ValueError,
        match="Agent name must not be empty",
    ):
        ToolContext(agent_name=" ")


def test_tool_context_rejects_empty_user_id() -> None:
    """ToolContext should reject an empty provided user identifier."""
    with pytest.raises(
        ValueError,
        match="User ID must not be empty",
    ):
        ToolContext(user_id=" ")


def test_tool_context_rejects_empty_metadata_key() -> None:
    """ToolContext should reject an empty metadata key."""
    context = ToolContext()

    with pytest.raises(
        ValueError,
        match="Metadata key must not be empty",
    ):
        context.set_metadata(" ", "value")

## Run

uv run ruff format `
    src\full_stack_ai_shared\tools\context.py `
    tests\test_tool_context.py

uv run ruff check `
    src\full_stack_ai_shared\tools\context.py `
    tests\test_tool_context.py

uv run mypy src
uv run pytest tests\test_tool_context.py -v

## Step 14.5 — Create the Abstract BaseTool

## code src\full_stack_ai_shared\tools\base.py

"""Abstract base classes for shared AI tools."""

from abc import ABC, abstractmethod
from typing import Any

from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.models import ToolDefinition, ToolResult


class BaseTool(ABC):
    """Define the common interface implemented by all AI tools."""

    def __init__(
        self,
        name: str,
        description: str,
        input_schema: dict[str, Any] | None = None,
    ) -> None:
        """Initialize the tool definition."""
        self._definition = ToolDefinition(
            name=name,
            description=description,
            input_schema=input_schema or {},
        )

    @property
    def name(self) -> str:
        """Return the tool name."""
        return self._definition.name

    @property
    def description(self) -> str:
        """Return the tool description."""
        return self._definition.description

    @property
    def input_schema(self) -> dict[str, Any]:
        """Return a copy of the tool input schema."""
        return dict(self._definition.input_schema)

    @property
    def definition(self) -> ToolDefinition:
        """Return the tool definition."""
        return ToolDefinition(
            name=self._definition.name,
            description=self._definition.description,
            input_schema=dict(self._definition.input_schema),
        )

    @abstractmethod
    async def execute(
        self,
        arguments: dict[str, Any],
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Execute the tool with validated arguments."""

## New-Item -ItemType File -Force tests\test_base_tool.py | Out-Null
code tests\test_base_tool.py

"""Tests for the shared AI tool base class."""

from typing import Any

import pytest

from full_stack_ai_shared.tools.base import BaseTool
from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.models import ToolResult


class EchoTool(BaseTool):
    """Simple tool implementation used for testing."""

    async def execute(
        self,
        arguments: dict[str, Any],
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Return the supplied arguments."""
        return ToolResult(
            tool_name=self.name,
            success=True,
            output=arguments,
            metadata={
                "execution_id": (
                    context.execution_id if context is not None else None
                ),
            },
        )


def test_base_tool_properties() -> None:
    """BaseTool should expose its configured definition."""
    tool = EchoTool(
        name="echo",
        description="Return the supplied arguments.",
        input_schema={
            "type": "object",
            "properties": {
                "message": {"type": "string"},
            },
        },
    )

    assert tool.name == "echo"
    assert tool.description == "Return the supplied arguments."
    assert tool.input_schema == {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
        },
    }


def test_base_tool_definition() -> None:
    """BaseTool should return a complete tool definition."""
    tool = EchoTool(
        name="echo",
        description="Return the supplied arguments.",
    )

    definition = tool.definition

    assert definition.name == "echo"
    assert definition.description == "Return the supplied arguments."
    assert definition.input_schema == {}


def test_base_tool_returns_schema_copy() -> None:
    """Changing a returned schema should not change the tool."""
    tool = EchoTool(
        name="echo",
        description="Return the supplied arguments.",
        input_schema={"type": "object"},
    )

    schema = tool.input_schema
    schema["type"] = "array"

    assert tool.input_schema == {"type": "object"}


@pytest.mark.asyncio
async def test_base_tool_execution() -> None:
    """Concrete tools should implement asynchronous execution."""
    tool = EchoTool(
        name="echo",
        description="Return the supplied arguments.",
    )
    context = ToolContext(execution_id="execution-123")

    result = await tool.execute(
        arguments={"message": "hello"},
        context=context,
    )

    assert result.success is True
    assert result.tool_name == "echo"
    assert result.output == {"message": "hello"}
    assert result.metadata == {"execution_id": "execution-123"}


def test_base_tool_cannot_be_instantiated() -> None:
    """BaseTool should remain abstract."""
    with pytest.raises(TypeError):
        BaseTool(  # type: ignore[abstract]
            name="invalid",
            description="Invalid direct construction.",
        )

## Run

uv run ruff format `
    src\full_stack_ai_shared\tools\base.py `
    tests\test_base_tool.py

uv run ruff check `
    src\full_stack_ai_shared\tools\base.py `
    tests\test_base_tool.py

uv run mypy src

uv run pytest tests\test_base_tool.py -v

## Step 14.6 — Build FunctionTool

## code src\full_stack_ai_shared\tools\function.py

"""Function-backed implementation of the shared AI tool interface."""

import inspect
from collections.abc import Awaitable, Callable
from typing import Any

from full_stack_ai_shared.tools.base import BaseTool
from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.models import ToolResult

ToolFunction = Callable[..., Any]
AsyncToolFunction = Callable[..., Awaitable[Any]]


class FunctionTool(BaseTool):
    """Expose a synchronous or asynchronous Python function as an AI tool."""

    def __init__(
        self,
        name: str,
        description: str,
        function: ToolFunction | AsyncToolFunction,
        input_schema: dict[str, Any] | None = None,
    ) -> None:
        """Initialize the function-backed tool."""
        if not callable(function):
            raise TypeError("Tool function must be callable.")

        super().__init__(
            name=name,
            description=description,
            input_schema=input_schema,
        )
        self._function = function

    async def execute(
        self,
        arguments: dict[str, Any],
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Execute the wrapped function and return a standardized result."""
        try:
            output = self._function(**arguments)

            if inspect.isawaitable(output):
                output = await output

            metadata: dict[str, Any] = {}

            if context is not None:
                metadata["execution_id"] = context.execution_id

                if context.agent_name is not None:
                    metadata["agent_name"] = context.agent_name

                if context.user_id is not None:
                    metadata["user_id"] = context.user_id

            return ToolResult(
                tool_name=self.name,
                success=True,
                output=output,
                metadata=metadata,
            )
        except Exception as error:
            return ToolResult(
                tool_name=self.name,
                success=False,
                error=str(error),
                metadata={
                    "error_type": type(error).__name__,
                },
            )
      

## code tests\test_function_tool.py

"""Tests for function-backed shared AI tools."""

from typing import Any

import pytest

from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.function import FunctionTool


def add_numbers(first: int, second: int) -> int:
    """Add two integers."""
    return first + second


async def multiply_numbers(first: int, second: int) -> int:
    """Multiply two integers asynchronously."""
    return first * second


def raise_tool_error() -> None:
    """Raise a predictable function error."""
    raise RuntimeError("Simulated tool failure.")


def return_asset(asset_id: str) -> dict[str, Any]:
    """Return an industrial asset record."""
    return {
        "asset_id": asset_id,
        "status": "operational",
    }


def test_function_tool_properties() -> None:
    """FunctionTool should expose its configured tool details."""
    tool = FunctionTool(
        name="add_numbers",
        description="Add two integer values.",
        function=add_numbers,
        input_schema={
            "type": "object",
            "properties": {
                "first": {"type": "integer"},
                "second": {"type": "integer"},
            },
            "required": ["first", "second"],
        },
    )

    assert tool.name == "add_numbers"
    assert tool.description == "Add two integer values."
    assert tool.input_schema["type"] == "object"


def test_function_tool_rejects_non_callable() -> None:
    """FunctionTool should reject a non-callable function value."""
    with pytest.raises(
        TypeError,
        match="Tool function must be callable",
    ):
        FunctionTool(
            name="invalid",
            description="Invalid tool.",
            function="not-callable",  # type: ignore[arg-type]
        )


@pytest.mark.asyncio
async def test_function_tool_executes_sync_function() -> None:
    """FunctionTool should execute synchronous Python functions."""
    tool = FunctionTool(
        name="add_numbers",
        description="Add two integer values.",
        function=add_numbers,
    )

    result = await tool.execute(
        {
            "first": 10,
            "second": 15,
        },
    )

    assert result.success is True
    assert result.tool_name == "add_numbers"
    assert result.output == 25
    assert result.error is None


@pytest.mark.asyncio
async def test_function_tool_executes_async_function() -> None:
    """FunctionTool should await asynchronous Python functions."""
    tool = FunctionTool(
        name="multiply_numbers",
        description="Multiply two integer values.",
        function=multiply_numbers,
    )

    result = await tool.execute(
        {
            "first": 6,
            "second": 7,
        },
    )

    assert result.success is True
    assert result.output == 42


@pytest.mark.asyncio
async def test_function_tool_returns_complex_output() -> None:
    """FunctionTool should preserve structured function output."""
    tool = FunctionTool(
        name="return_asset",
        description="Return an industrial asset.",
        function=return_asset,
    )

    result = await tool.execute(
        {
            "asset_id": "PUMP-101",
        },
    )

    assert result.success is True
    assert result.output == {
        "asset_id": "PUMP-101",
        "status": "operational",
    }


@pytest.mark.asyncio
async def test_function_tool_adds_context_metadata() -> None:
    """FunctionTool should include relevant execution context metadata."""
    tool = FunctionTool(
        name="add_numbers",
        description="Add two integer values.",
        function=add_numbers,
    )
    context = ToolContext(
        execution_id="execution-123",
        agent_name="calculation-agent",
        user_id="user-456",
    )

    result = await tool.execute(
        {
            "first": 2,
            "second": 3,
        },
        context=context,
    )

    assert result.success is True
    assert result.metadata == {
        "execution_id": "execution-123",
        "agent_name": "calculation-agent",
        "user_id": "user-456",
    }


@pytest.mark.asyncio
async def test_function_tool_handles_function_failure() -> None:
    """FunctionTool should return a failed result for function errors."""
    tool = FunctionTool(
        name="raise_tool_error",
        description="Raise a predictable error.",
        function=raise_tool_error,
    )

    result = await tool.execute({})

    assert result.success is False
    assert result.output is None
    assert result.error == "Simulated tool failure."
    assert result.metadata == {
        "error_type": "RuntimeError",
    }


@pytest.mark.asyncio
async def test_function_tool_handles_missing_argument() -> None:
    """FunctionTool should return failure when arguments are missing."""
    tool = FunctionTool(
        name="add_numbers",
        description="Add two integer values.",
        function=add_numbers,
    )

    result = await tool.execute(
        {
            "first": 10,
        },
    )

    assert result.success is False
    assert result.error is not None
    assert result.metadata["error_type"] == "TypeError"


## Run

uv run ruff format `
    src\full_stack_ai_shared\tools\function.py `
    tests\test_function_tool.py

uv run ruff check `
    src\full_stack_ai_shared\tools\function.py `
    tests\test_function_tool.py

uv run mypy src

uv run pytest tests\test_function_tool.py -v

## Step 14.7 — Build the ToolRegistry

## code src\full_stack_ai_shared\tools\registry.py

"""Registry for discovering and executing shared AI tools."""

from typing import Any

from full_stack_ai_shared.tools.base import BaseTool
from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.exceptions import (
    ToolAlreadyRegisteredError,
    ToolNotFoundError,
)
from full_stack_ai_shared.tools.models import ToolDefinition, ToolResult


class ToolRegistry:
    """Store, discover, and execute registered AI tools."""

    def __init__(self) -> None:
        """Initialize an empty tool registry."""
        self._tools: dict[str, BaseTool] = {}

    def register(
        self,
        tool: BaseTool,
        *,
        replace: bool = False,
    ) -> None:
        """Register a tool by its unique name."""
        if tool.name in self._tools and not replace:
            raise ToolAlreadyRegisteredError(tool.name)

        self._tools[tool.name] = tool

    def unregister(self, tool_name: str) -> BaseTool:
        """Remove and return a registered tool."""
        try:
            return self._tools.pop(tool_name)
        except KeyError as error:
            raise ToolNotFoundError(tool_name) from error

    def get(self, tool_name: str) -> BaseTool:
        """Return a registered tool by name."""
        try:
            return self._tools[tool_name]
        except KeyError as error:
            raise ToolNotFoundError(tool_name) from error

    def contains(self, tool_name: str) -> bool:
        """Return whether a tool is registered."""
        return tool_name in self._tools

    def list_tools(self) -> list[ToolDefinition]:
        """Return definitions for all registered tools."""
        return [
            self._tools[name].definition
            for name in sorted(self._tools)
        ]

    async def execute(
        self,
        tool_name: str,
        arguments: dict[str, Any] | None = None,
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Execute a registered tool."""
        tool = self.get(tool_name)

        return await tool.execute(
            arguments=arguments or {},
            context=context,
        )

    def clear(self) -> None:
        """Remove all registered tools."""
        self._tools.clear()

    def __len__(self) -> int:
        """Return the number of registered tools."""
        return len(self._tools)

    def __contains__(self, tool_name: object) -> bool:
        """Support membership checks using the `in` operator."""
        if not isinstance(tool_name, str):
            return False

        return self.contains(tool_name)

## code tests\test_tool_registry.py

"""Tests for the shared AI tool registry."""

import pytest

from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.exceptions import (
    ToolAlreadyRegisteredError,
    ToolNotFoundError,
)
from full_stack_ai_shared.tools.function import FunctionTool
from full_stack_ai_shared.tools.registry import ToolRegistry


def add_numbers(first: int, second: int) -> int:
    """Add two integers."""
    return first + second


def subtract_numbers(first: int, second: int) -> int:
    """Subtract the second integer from the first."""
    return first - second


def create_add_tool() -> FunctionTool:
    """Create a reusable addition tool."""
    return FunctionTool(
        name="add_numbers",
        description="Add two integer values.",
        function=add_numbers,
        input_schema={
            "type": "object",
            "properties": {
                "first": {"type": "integer"},
                "second": {"type": "integer"},
            },
            "required": ["first", "second"],
        },
    )


def test_tool_registry_defaults() -> None:
    """ToolRegistry should start empty."""
    registry = ToolRegistry()

    assert len(registry) == 0
    assert registry.list_tools() == []


def test_tool_registry_registers_tool() -> None:
    """ToolRegistry should register a tool by name."""
    registry = ToolRegistry()
    tool = create_add_tool()

    registry.register(tool)

    assert len(registry) == 1
    assert registry.contains("add_numbers") is True
    assert "add_numbers" in registry
    assert registry.get("add_numbers") is tool


def test_tool_registry_rejects_duplicate_tool() -> None:
    """ToolRegistry should reject duplicate names by default."""
    registry = ToolRegistry()
    registry.register(create_add_tool())

    with pytest.raises(
        ToolAlreadyRegisteredError,
        match="Tool 'add_numbers' is already registered",
    ):
        registry.register(create_add_tool())


def test_tool_registry_replaces_existing_tool() -> None:
    """ToolRegistry should replace a tool when explicitly requested."""
    registry = ToolRegistry()
    original = create_add_tool()
    replacement = FunctionTool(
        name="add_numbers",
        description="Subtract two integer values.",
        function=subtract_numbers,
    )

    registry.register(original)
    registry.register(replacement, replace=True)

    assert len(registry) == 1
    assert registry.get("add_numbers") is replacement


def test_tool_registry_gets_missing_tool() -> None:
    """ToolRegistry should raise when a requested tool is absent."""
    registry = ToolRegistry()

    with pytest.raises(
        ToolNotFoundError,
        match="Tool 'missing_tool' is not registered",
    ):
        registry.get("missing_tool")


def test_tool_registry_unregisters_tool() -> None:
    """ToolRegistry should remove and return a registered tool."""
    registry = ToolRegistry()
    tool = create_add_tool()
    registry.register(tool)

    removed_tool = registry.unregister("add_numbers")

    assert removed_tool is tool
    assert len(registry) == 0
    assert "add_numbers" not in registry


def test_tool_registry_unregisters_missing_tool() -> None:
    """ToolRegistry should raise when removing an absent tool."""
    registry = ToolRegistry()

    with pytest.raises(
        ToolNotFoundError,
        match="Tool 'missing_tool' is not registered",
    ):
        registry.unregister("missing_tool")


def test_tool_registry_lists_sorted_definitions() -> None:
    """ToolRegistry should return sorted tool definitions."""
    registry = ToolRegistry()
    registry.register(
        FunctionTool(
            name="subtract_numbers",
            description="Subtract two integer values.",
            function=subtract_numbers,
        ),
    )
    registry.register(create_add_tool())

    definitions = registry.list_tools()

    assert [definition.name for definition in definitions] == [
        "add_numbers",
        "subtract_numbers",
    ]
    assert definitions[0].description == "Add two integer values."
    assert definitions[0].input_schema["type"] == "object"


@pytest.mark.asyncio
async def test_tool_registry_executes_tool() -> None:
    """ToolRegistry should execute a registered tool."""
    registry = ToolRegistry()
    registry.register(create_add_tool())

    result = await registry.execute(
        "add_numbers",
        {
            "first": 20,
            "second": 22,
        },
    )

    assert result.success is True
    assert result.tool_name == "add_numbers"
    assert result.output == 42


@pytest.mark.asyncio
async def test_tool_registry_executes_with_context() -> None:
    """ToolRegistry should pass execution context to the tool."""
    registry = ToolRegistry()
    registry.register(create_add_tool())
    context = ToolContext(
        execution_id="execution-123",
        agent_name="math-agent",
    )

    result = await registry.execute(
        "add_numbers",
        {
            "first": 2,
            "second": 3,
        },
        context=context,
    )

    assert result.success is True
    assert result.output == 5
    assert result.metadata == {
        "execution_id": "execution-123",
        "agent_name": "math-agent",
    }


@pytest.mark.asyncio
async def test_tool_registry_executes_with_default_arguments() -> None:
    """ToolRegistry should use empty arguments when none are supplied."""

    def return_status() -> str:
        return "operational"

    registry = ToolRegistry()
    registry.register(
        FunctionTool(
            name="return_status",
            description="Return the current status.",
            function=return_status,
        ),
    )

    result = await registry.execute("return_status")

    assert result.success is True
    assert result.output == "operational"


@pytest.mark.asyncio
async def test_tool_registry_executes_missing_tool() -> None:
    """ToolRegistry should raise when executing an absent tool."""
    registry = ToolRegistry()

    with pytest.raises(
        ToolNotFoundError,
        match="Tool 'missing_tool' is not registered",
    ):
        await registry.execute("missing_tool")


def test_tool_registry_clears_tools() -> None:
    """ToolRegistry should remove all registered tools."""
    registry = ToolRegistry()
    registry.register(create_add_tool())
    registry.register(
        FunctionTool(
            name="subtract_numbers",
            description="Subtract two integer values.",
            function=subtract_numbers,
        ),
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list_tools() == []

## Run

uv run ruff format `
    src\full_stack_ai_shared\tools\registry.py `
    tests\test_tool_registry.py

uv run ruff check `
    src\full_stack_ai_shared\tools\registry.py `
    tests\test_tool_registry.py

uv run mypy src

uv run pytest tests\test_tool_registry.py -v

## Step 14.8 — Export the Complete Public API

## code src\full_stack_ai_shared\tools\__init__.py

"""Shared AI tool framework abstractions."""

from full_stack_ai_shared.tools.base import BaseTool
from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.exceptions import (
    ToolAlreadyRegisteredError,
    ToolError,
    ToolExecutionError,
    ToolNotFoundError,
)
from full_stack_ai_shared.tools.function import FunctionTool
from full_stack_ai_shared.tools.models import (
    ToolDefinition,
    ToolRequest,
    ToolResult,
)
from full_stack_ai_shared.tools.registry import ToolRegistry

__all__ = [
    "BaseTool",
    "FunctionTool",
    "ToolAlreadyRegisteredError",
    "ToolContext",
    "ToolDefinition",
    "ToolError",
    "ToolExecutionError",
    "ToolNotFoundError",
    "ToolRegistry",
    "ToolRequest",
    "ToolResult",
]

## New-Item -ItemType File -Force tests\test_tools_public_api.py | Out-Null
code tests\test_tools_public_api.py

"""Tests for the shared AI tool framework public API."""

from full_stack_ai_shared.tools import (
    BaseTool,
    FunctionTool,
    ToolAlreadyRegisteredError,
    ToolContext,
    ToolDefinition,
    ToolError,
    ToolExecutionError,
    ToolNotFoundError,
    ToolRegistry,
    ToolRequest,
    ToolResult,
)


def test_tools_public_api_exports_expected_types() -> None:
    """The tools package should expose the complete public API."""
    assert BaseTool.__name__ == "BaseTool"
    assert FunctionTool.__name__ == "FunctionTool"
    assert ToolAlreadyRegisteredError.__name__ == (
        "ToolAlreadyRegisteredError"
    )
    assert ToolContext.__name__ == "ToolContext"
    assert ToolDefinition.__name__ == "ToolDefinition"
    assert ToolError.__name__ == "ToolError"
    assert ToolExecutionError.__name__ == "ToolExecutionError"
    assert ToolNotFoundError.__name__ == "ToolNotFoundError"
    assert ToolRegistry.__name__ == "ToolRegistry"
    assert ToolRequest.__name__ == "ToolRequest"
    assert ToolResult.__name__ == "ToolResult"
    
## Run

uv run ruff format `
    src\full_stack_ai_shared\tools\__init__.py `
    tests\test_tools_public_api.py

uv run ruff check `
    src\full_stack_ai_shared\tools\__init__.py `
    tests\test_tools_public_api.py

uv run mypy src

uv run pytest tests\test_tools_public_api.py -v

uv run python -c "from full_stack_ai_shared.tools import BaseTool, FunctionTool, ToolContext, ToolRegistry, ToolRequest, ToolResult; print('Shared AI tool framework imports successfully.')"
Shared AI tool framework imports successfully.

## Step 14.9 — Run the Complete Tool Framework Test Suite:

uv run pytest `
    tests\test_tool_models.py `
    tests\test_tool_exceptions.py `
    tests\test_tool_context.py `
    tests\test_base_tool.py `
    tests\test_function_tool.py `
    tests\test_tool_registry.py `
    tests\test_tools_public_api.py `
    -v

## run the full project quality checks:

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## Step 14.10 — Add Request-Based Execution

## code src\full_stack_ai_shared\tools\registry.py

"""Registry for discovering and executing shared AI tools."""

from typing import Any

from full_stack_ai_shared.tools.base import BaseTool
from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.exceptions import (
    ToolAlreadyRegisteredError,
    ToolNotFoundError,
)
from full_stack_ai_shared.tools.models import (
    ToolDefinition,
    ToolRequest,
    ToolResult,
)


class ToolRegistry:
    """Store, discover, and execute registered AI tools."""

    def __init__(self) -> None:
        """Initialize an empty tool registry."""
        self._tools: dict[str, BaseTool] = {}

    def register(
        self,
        tool: BaseTool,
        *,
        replace: bool = False,
    ) -> None:
        """Register a tool by its unique name."""
        if tool.name in self._tools and not replace:
            raise ToolAlreadyRegisteredError(tool.name)

        self._tools[tool.name] = tool

    def unregister(self, tool_name: str) -> BaseTool:
        """Remove and return a registered tool."""
        try:
            return self._tools.pop(tool_name)
        except KeyError as error:
            raise ToolNotFoundError(tool_name) from error

    def get(self, tool_name: str) -> BaseTool:
        """Return a registered tool by name."""
        try:
            return self._tools[tool_name]
        except KeyError as error:
            raise ToolNotFoundError(tool_name) from error

    def contains(self, tool_name: str) -> bool:
        """Return whether a tool is registered."""
        return tool_name in self._tools

    def list_tools(self) -> list[ToolDefinition]:
        """Return definitions for all registered tools."""
        return [
            self._tools[name].definition
            for name in sorted(self._tools)
        ]

    async def execute(
        self,
        tool_name: str,
        arguments: dict[str, Any] | None = None,
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Execute a registered tool by name."""
        request = ToolRequest(
            tool_name=tool_name,
            arguments=arguments or {},
        )

        return await self.execute_request(
            request=request,
            context=context,
        )

    async def execute_request(
        self,
        request: ToolRequest,
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Execute a complete tool request."""
        tool = self.get(request.tool_name)

        result = await tool.execute(
            arguments=request.arguments,
            context=context,
        )

        result.request_id = request.request_id
        return result

    def clear(self) -> None:
        """Remove all registered tools."""
        self._tools.clear()

    def __len__(self) -> int:
        """Return the number of registered tools."""
        return len(self._tools)

    def __contains__(self, tool_name: object) -> bool:
        """Support membership checks using the `in` operator."""
        if not isinstance(tool_name, str):
            return False

        return self.contains(tool_name)

## code tests\test_tool_registry.py

from full_stack_ai_shared.tools.models import ToolRequest

@pytest.mark.asyncio
async def test_tool_registry_executes_tool_request() -> None:
    """ToolRegistry should execute a complete ToolRequest."""
    registry = ToolRegistry()
    registry.register(create_add_tool())

    request = ToolRequest(
        tool_name="add_numbers",
        arguments={
            "first": 19,
            "second": 23,
        },
        request_id="request-123",
    )

    result = await registry.execute_request(request)

    assert result.success is True
    assert result.output == 42
    assert result.request_id == "request-123"


@pytest.mark.asyncio
async def test_tool_registry_generated_request_id_is_preserved() -> None:
    """Name-based execution should preserve its generated request ID."""
    registry = ToolRegistry()
    registry.register(create_add_tool())

    result = await registry.execute(
        "add_numbers",
        {
            "first": 10,
            "second": 5,
        },
    )

    assert result.success is True
    assert result.output == 15
    assert result.request_id is not None

## Run

uv run ruff format `
    src\full_stack_ai_shared\tools\registry.py `
    tests\test_tool_registry.py

uv run ruff check `
    src\full_stack_ai_shared\tools\registry.py `
    tests\test_tool_registry.py

uv run mypy src

uv run pytest tests\test_tool_registry.py -v

## Run the full project

uv run ruff format .
uv run ruff check .
uv run mypy src
uv run pytest -v

## tep 15 — Shared AI Agent Orchestration Framework

## Step 15.1 — Create the Agent Execution Context

## Create files

New-Item -ItemType File -Force `
    src\full_stack_ai_shared\agents\context.py | Out-Null

New-Item -ItemType File -Force `
    tests\test_agent_context.py | Out-Null

## code src\full_stack_ai_shared\agents\context.py

"""Execution context for shared AI-agent orchestration."""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

from full_stack_ai_shared.agents.memory import AgentMemory
from full_stack_ai_shared.tools import ToolRegistry


@dataclass(slots=True)
class AgentExecutionContext:
    """Provide shared services and metadata during agent execution."""

    execution_id: str = field(default_factory=lambda: str(uuid4()))
    tool_registry: ToolRegistry = field(default_factory=ToolRegistry)
    memory: AgentMemory = field(default_factory=AgentMemory)
    rag_service: Any | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate the agent execution context."""
        if not self.execution_id.strip():
            raise ValueError("Execution ID must not be empty.")

    def get_metadata(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """Return a metadata value or the supplied default."""
        return self.metadata.get(key, default)

    def set_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """Add or update execution metadata."""
        if not key.strip():
            raise ValueError("Metadata key must not be empty.")

        self.metadata[key] = value

## code tests\test_agent_context.py

"""Tests for shared AI-agent execution context."""

import pytest

from full_stack_ai_shared.agents.context import AgentExecutionContext
from full_stack_ai_shared.agents.memory import AgentMemory
from full_stack_ai_shared.tools import ToolRegistry


def test_agent_execution_context_defaults() -> None:
    """Context should provide shared service defaults."""
    context = AgentExecutionContext()

    assert context.execution_id
    assert isinstance(context.tool_registry, ToolRegistry)
    assert isinstance(context.memory, AgentMemory)
    assert context.rag_service is None
    assert context.metadata == {}


def test_agent_execution_context_accepts_services() -> None:
    """Context should store supplied shared services."""
    registry = ToolRegistry()
    memory = AgentMemory()
    rag_service = object()

    context = AgentExecutionContext(
        execution_id="execution-123",
        tool_registry=registry,
        memory=memory,
        rag_service=rag_service,
        metadata={"environment": "test"},
    )

    assert context.execution_id == "execution-123"
    assert context.tool_registry is registry
    assert context.memory is memory
    assert context.rag_service is rag_service
    assert context.metadata == {"environment": "test"}


def test_agent_execution_context_gets_metadata() -> None:
    """Context should return stored metadata."""
    context = AgentExecutionContext(
        metadata={"asset_id": "PUMP-101"},
    )

    assert context.get_metadata("asset_id") == "PUMP-101"


def test_agent_execution_context_returns_metadata_default() -> None:
    """Context should return the supplied default for missing metadata."""
    context = AgentExecutionContext()

    assert context.get_metadata("region", "unknown") == "unknown"


def test_agent_execution_context_sets_metadata() -> None:
    """Context should add and update metadata."""
    context = AgentExecutionContext()

    context.set_metadata("region", "west")
    assert context.metadata == {"region": "west"}

    context.set_metadata("region", "central")
    assert context.metadata == {"region": "central"}


def test_agent_execution_context_rejects_empty_execution_id() -> None:
    """Context should reject an empty execution identifier."""
    with pytest.raises(
        ValueError,
        match="Execution ID must not be empty",
    ):
        AgentExecutionContext(execution_id=" ")


def test_agent_execution_context_rejects_empty_metadata_key() -> None:
    """Context should reject an empty metadata key."""
    context = AgentExecutionContext()

    with pytest.raises(
        ValueError,
        match="Metadata key must not be empty",
    ):
        context.set_metadata(" ", "value")

## Run

uv run ruff format `
    src\full_stack_ai_shared\agents\context.py `
    tests\test_agent_context.py

uv run ruff check `
    src\full_stack_ai_shared\agents\context.py `
    tests\test_agent_context.py

uv run mypy src

uv run pytest tests\test_agent_context.py -v

git add .
git commit -m "Add shared AI tool framework"
git push origin main
git status

## Step 16 — Shared Multi-Agent Orchestrator

## Step 16.1 — Create the new files

@(
    "src\full_stack_ai_shared\agents\registry.py",
    "src\full_stack_ai_shared\agents\exceptions.py",
    "src\full_stack_ai_shared\agents\orchestrator.py",
    "tests\test_agent_registry.py",
    "tests\test_agent_exceptions.py",
    "tests\test_orchestrator.py"
) | ForEach-Object {
    New-Item -ItemType File -Force $_ | Out-Null
}

## Step 16.1 — Build the Agent Registry

code src\full_stack_ai_shared\agents\registry.py

"""Registry for discovering and retrieving shared AI agents."""

from collections.abc import Iterator

from full_stack_ai_shared.agents.base import BaseAgent


class AgentRegistry:
    """Store and manage named AI-agent instances."""

    def __init__(self) -> None:
        """Initialize an empty agent registry."""
        self._agents: dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        """Register an agent using its unique name."""
        agent_name = agent.name.strip()

        if not agent_name:
            raise ValueError("Agent name must not be empty.")

        if agent_name in self._agents:
            raise ValueError(f"Agent '{agent_name}' is already registered.")

        self._agents[agent_name] = agent

    def get(self, agent_name: str) -> BaseAgent:
        """Return an agent registered under the supplied name."""
        normalized_name = agent_name.strip()

        if not normalized_name:
            raise ValueError("Agent name must not be empty.")

        try:
            return self._agents[normalized_name]
        except KeyError as error:
            raise KeyError(
                f"Agent '{normalized_name}' is not registered."
            ) from error

    def unregister(self, agent_name: str) -> BaseAgent:
        """Remove and return a registered agent."""
        normalized_name = agent_name.strip()

        if not normalized_name:
            raise ValueError("Agent name must not be empty.")

        try:
            return self._agents.pop(normalized_name)
        except KeyError as error:
            raise KeyError(
                f"Agent '{normalized_name}' is not registered."
            ) from error

    def contains(self, agent_name: str) -> bool:
        """Return whether an agent name exists in the registry."""
        return agent_name.strip() in self._agents

    def list_names(self) -> list[str]:
        """Return all registered agent names in insertion order."""
        return list(self._agents)

    def clear(self) -> None:
        """Remove all registered agents."""
        self._agents.clear()

    def __len__(self) -> int:
        """Return the number of registered agents."""
        return len(self._agents)

    def __iter__(self) -> Iterator[BaseAgent]:
        """Iterate over registered agents."""
        return iter(self._agents.values())

## Step 16.2 — Add - code tests\test_agent_registry.py

"""Tests for the shared AI-agent registry."""

import pytest

from full_stack_ai_shared.agents import (
    AgentRegistry,
    AgentRequest,
    AgentResult,
    BaseAgent,
)


class TestAgent(BaseAgent):
    """Simple agent implementation used for registry tests."""

    async def run(self, request: AgentRequest) -> AgentResult:
        """Return the submitted task as a successful result."""
        return AgentResult(
            agent_name=self.name,
            success=True,
            output=request.task,
        )


def test_agent_registry_starts_empty() -> None:
    """Registry should contain no agents after initialization."""
    registry = AgentRegistry()

    assert len(registry) == 0
    assert registry.list_names() == []


def test_agent_registry_registers_agent() -> None:
    """Registry should store an agent by name."""
    registry = AgentRegistry()
    agent = TestAgent(name="diagnostic-agent")

    registry.register(agent)

    assert len(registry) == 1
    assert registry.contains("diagnostic-agent")
    assert registry.get("diagnostic-agent") is agent


def test_agent_registry_rejects_duplicate_agent_name() -> None:
    """Registry should reject agents with duplicate names."""
    registry = AgentRegistry()
    first_agent = TestAgent(name="diagnostic-agent")
    second_agent = TestAgent(name="diagnostic-agent")

    registry.register(first_agent)

    with pytest.raises(
        ValueError,
        match="Agent 'diagnostic-agent' is already registered.",
    ):
        registry.register(second_agent)


def test_agent_registry_get_rejects_unknown_agent() -> None:
    """Registry should reject requests for unknown agents."""
    registry = AgentRegistry()

    with pytest.raises(
        KeyError,
        match="Agent 'missing-agent' is not registered.",
    ):
        registry.get("missing-agent")


def test_agent_registry_unregisters_agent() -> None:
    """Registry should remove and return a registered agent."""
    registry = AgentRegistry()
    agent = TestAgent(name="diagnostic-agent")
    registry.register(agent)

    removed_agent = registry.unregister("diagnostic-agent")

    assert removed_agent is agent
    assert not registry.contains("diagnostic-agent")
    assert len(registry) == 0


def test_agent_registry_unregister_rejects_unknown_agent() -> None:
    """Registry should reject removal of an unknown agent."""
    registry = AgentRegistry()

    with pytest.raises(
        KeyError,
        match="Agent 'missing-agent' is not registered.",
    ):
        registry.unregister("missing-agent")


def test_agent_registry_lists_registered_names() -> None:
    """Registry should list names in registration order."""
    registry = AgentRegistry()
    registry.register(TestAgent(name="planning-agent"))
    registry.register(TestAgent(name="retrieval-agent"))

    assert registry.list_names() == [
        "planning-agent",
        "retrieval-agent",
    ]


def test_agent_registry_iterates_over_agents() -> None:
    """Registry should iterate over registered agent instances."""
    registry = AgentRegistry()
    planning_agent = TestAgent(name="planning-agent")
    retrieval_agent = TestAgent(name="retrieval-agent")

    registry.register(planning_agent)
    registry.register(retrieval_agent)

    assert list(registry) == [
        planning_agent,
        retrieval_agent,
    ]


def test_agent_registry_clears_agents() -> None:
    """Registry should remove every registered agent."""
    registry = AgentRegistry()
    registry.register(TestAgent(name="planning-agent"))
    registry.register(TestAgent(name="retrieval-agent"))

    registry.clear()

    assert len(registry) == 0
    assert registry.list_names() == []


@pytest.mark.parametrize(
    ("operation", "agent_name"),
    [
        ("get", ""),
        ("get", "   "),
        ("unregister", ""),
        ("unregister", "   "),
    ],
)
def test_agent_registry_rejects_empty_names(
    operation: str,
    agent_name: str,
) -> None:
    """Registry operations should reject empty agent names."""
    registry = AgentRegistry()

    method = getattr(registry, operation)

    with pytest.raises(
        ValueError,
        match="Agent name must not be empty.",
    ):
        method(agent_name)

## Step 16.3 — Export AgentRegistry

## code src\full_stack_ai_shared\agents\__init__.py

"""Shared AI-agent abstractions."""

from full_stack_ai_shared.agents.base import (
    AgentRequest,
    AgentResult,
    BaseAgent,
)
from full_stack_ai_shared.agents.context import AgentExecutionContext
from full_stack_ai_shared.agents.memory import (
    AgentMemory,
    MemoryEntry,
)
from full_stack_ai_shared.agents.registry import AgentRegistry
from full_stack_ai_shared.agents.state import (
    AgentState,
    AgentStatus,
)

__all__ = [
    "AgentExecutionContext",
    "AgentMemory",
    "AgentRegistry",
    "AgentRequest",
    "AgentResult",
    "AgentState",
    "AgentStatus",
    "BaseAgent",
    "MemoryEntry",
]

## Run

uv run ruff format `
    src\full_stack_ai_shared\agents\registry.py `
    src\full_stack_ai_shared\agents\__init__.py `
    tests\test_agent_registry.py

uv run ruff check `
    src\full_stack_ai_shared\agents\registry.py `
    src\full_stack_ai_shared\agents\__init__.py `
    tests\test_agent_registry.py

uv run mypy src

## code tests\test_agent_registry.py

"""Tests for the shared AI-agent registry."""

from collections.abc import Callable
from typing import Any

import pytest

from full_stack_ai_shared.agents import (
    AgentRegistry,
    AgentRequest,
    AgentResult,
    BaseAgent,
)


class StubAgent(BaseAgent):
    """Simple agent implementation used for registry tests."""

    async def run(self, request: AgentRequest) -> AgentResult:
        """Return the submitted task as a successful result."""
        return AgentResult(
            agent_name=self.name,
            success=True,
            output=request.task,
        )


def test_agent_registry_starts_empty() -> None:
    """Registry should contain no agents after initialization."""
    registry = AgentRegistry()

    assert len(registry) == 0
    assert registry.list_names() == []


def test_agent_registry_registers_agent() -> None:
    """Registry should store an agent by name."""
    registry = AgentRegistry()
    agent = StubAgent(name="diagnostic-agent")

    registry.register(agent)

    assert len(registry) == 1
    assert registry.contains("diagnostic-agent")
    assert registry.get("diagnostic-agent") is agent


def test_agent_registry_rejects_duplicate_agent_name() -> None:
    """Registry should reject agents with duplicate names."""
    registry = AgentRegistry()
    first_agent = StubAgent(name="diagnostic-agent")
    second_agent = StubAgent(name="diagnostic-agent")

    registry.register(first_agent)

    with pytest.raises(
        ValueError,
        match="Agent 'diagnostic-agent' is already registered.",
    ):
        registry.register(second_agent)


def test_agent_registry_get_rejects_unknown_agent() -> None:
    """Registry should reject requests for unknown agents."""
    registry = AgentRegistry()

    with pytest.raises(
        KeyError,
        match="Agent 'missing-agent' is not registered.",
    ):
        registry.get("missing-agent")


def test_agent_registry_unregisters_agent() -> None:
    """Registry should remove and return a registered agent."""
    registry = AgentRegistry()
    agent = StubAgent(name="diagnostic-agent")
    registry.register(agent)

    removed_agent = registry.unregister("diagnostic-agent")

    assert removed_agent is agent
    assert not registry.contains("diagnostic-agent")
    assert len(registry) == 0


def test_agent_registry_unregister_rejects_unknown_agent() -> None:
    """Registry should reject removal of an unknown agent."""
    registry = AgentRegistry()

    with pytest.raises(
        KeyError,
        match="Agent 'missing-agent' is not registered.",
    ):
        registry.unregister("missing-agent")


def test_agent_registry_lists_registered_names() -> None:
    """Registry should list names in registration order."""
    registry = AgentRegistry()
    registry.register(StubAgent(name="planning-agent"))
    registry.register(StubAgent(name="retrieval-agent"))

    assert registry.list_names() == [
        "planning-agent",
        "retrieval-agent",
    ]


def test_agent_registry_iterates_over_agents() -> None:
    """Registry should iterate over registered agent instances."""
    registry = AgentRegistry()
    planning_agent = StubAgent(name="planning-agent")
    retrieval_agent = StubAgent(name="retrieval-agent")

    registry.register(planning_agent)
    registry.register(retrieval_agent)

    assert list(registry) == [
        planning_agent,
        retrieval_agent,
    ]


def test_agent_registry_clears_agents() -> None:
    """Registry should remove every registered agent."""
    registry = AgentRegistry()
    registry.register(StubAgent(name="planning-agent"))
    registry.register(StubAgent(name="retrieval-agent"))

    registry.clear()

    assert len(registry) == 0
    assert registry.list_names() == []


@pytest.mark.parametrize(
    ("operation", "agent_name"),
    [
        ("get", ""),
        ("get", "   "),
        ("unregister", ""),
        ("unregister", "   "),
    ],
)
def test_agent_registry_rejects_empty_names(
    operation: str,
    agent_name: str,
) -> None:
    """Registry operations should reject empty agent names."""
    registry = AgentRegistry()

    method: Callable[[str], Any] = getattr(registry, operation)

    with pytest.raises(
        ValueError,
        match="Agent name must not be empty.",
    ):
        method(agent_name)

## Run

uv run ruff format tests\test_agent_registry.py

uv run ruff check tests\test_agent_registry.py

uv run mypy src

uv run pytest tests\test_agent_registry.py -v

## Step 16.5 — Build the Agent Exception Hierarchy

## code src\full_stack_ai_shared\agents\exceptions.py

"""Exceptions raised by shared AI-agent orchestration components."""


class AgentError(Exception):
    """Base exception for all shared AI-agent errors."""


class AgentRegistrationError(AgentError):
    """Raised when an agent cannot be registered."""


class AgentNotFoundError(AgentError):
    """Raised when a requested agent is not registered."""


class AgentExecutionError(AgentError):
    """Raised when an agent fails during execution."""


class AgentOrchestrationError(AgentError):
    """Raised when an orchestration workflow cannot be completed."""

## Step 16.6 — code tests\test_agent_exceptions.py

"""Tests for shared AI-agent exceptions."""

import pytest

from full_stack_ai_shared.agents import (
    AgentError,
    AgentExecutionError,
    AgentNotFoundError,
    AgentOrchestrationError,
    AgentRegistrationError,
)


@pytest.mark.parametrize(
    "exception_type",
    [
        AgentRegistrationError,
        AgentNotFoundError,
        AgentExecutionError,
        AgentOrchestrationError,
    ],
)
def test_agent_exceptions_inherit_from_agent_error(
    exception_type: type[AgentError],
) -> None:
    """Specialized agent exceptions should inherit from AgentError."""
    error = exception_type("Agent operation failed.")

    assert isinstance(error, AgentError)
    assert isinstance(error, Exception)


@pytest.mark.parametrize(
    ("exception_type", "message"),
    [
        (
            AgentError,
            "Generic agent failure.",
        ),
        (
            AgentRegistrationError,
            "Agent registration failed.",
        ),
        (
            AgentNotFoundError,
            "Requested agent was not found.",
        ),
        (
            AgentExecutionError,
            "Agent execution failed.",
        ),
        (
            AgentOrchestrationError,
            "Agent orchestration failed.",
        ),
    ],
)
def test_agent_exceptions_preserve_messages(
    exception_type: type[AgentError],
    message: str,
) -> None:
    """Agent exceptions should preserve their supplied messages."""
    error = exception_type(message)

    assert str(error) == message


def test_agent_error_can_be_raised_and_caught() -> None:
    """AgentError should behave like a normal exception."""
    with pytest.raises(
        AgentError,
        match="Shared agent failure.",
    ):
        raise AgentError("Shared agent failure.")


def test_specialized_exception_can_be_caught_as_agent_error() -> None:
    """Specialized exceptions should be catchable as AgentError."""
    with pytest.raises(
        AgentError,
        match="Agent could not be executed.",
    ):
        raise AgentExecutionError("Agent could not be executed.")

## Step 16.7 — Export the Exceptions        code src\full_stack_ai_shared\agents\__init__.py

"""Shared AI-agent abstractions."""

from full_stack_ai_shared.agents.base import (
    AgentRequest,
    AgentResult,
    BaseAgent,
)
from full_stack_ai_shared.agents.context import AgentExecutionContext
from full_stack_ai_shared.agents.exceptions import (
    AgentError,
    AgentExecutionError,
    AgentNotFoundError,
    AgentOrchestrationError,
    AgentRegistrationError,
)
from full_stack_ai_shared.agents.memory import (
    AgentMemory,
    MemoryEntry,
)
from full_stack_ai_shared.agents.registry import AgentRegistry
from full_stack_ai_shared.agents.state import (
    AgentState,
    AgentStatus,
)

__all__ = [
    "AgentError",
    "AgentExecutionContext",
    "AgentExecutionError",
    "AgentMemory",
    "AgentNotFoundError",
    "AgentOrchestrationError",
    "AgentRegistry",
    "AgentRegistrationError",
    "AgentRequest",
    "AgentResult",
    "AgentState",
    "AgentStatus",
    "BaseAgent",
    "MemoryEntry",
]

## Run

uv run ruff format `
    src\full_stack_ai_shared\agents\exceptions.py `
    src\full_stack_ai_shared\agents\__init__.py `
    tests\test_agent_exceptions.py

uv run ruff check `
    src\full_stack_ai_shared\agents\exceptions.py `
    src\full_stack_ai_shared\agents\__init__.py `
    tests\test_agent_exceptions.py

uv run mypy src

uv run pytest tests\test_agent_exceptions.py -v

## Step 16.9 — Build Shared Agent Orchestrator  code src\full_stack_ai_shared\agents\orchestrator.py


"""Orchestration service for executing registered AI agents."""

from full_stack_ai_shared.agents.base import AgentRequest, AgentResult
from full_stack_ai_shared.agents.context import AgentExecutionContext
from full_stack_ai_shared.agents.exceptions import (
    AgentExecutionError,
    AgentNotFoundError,
)
from full_stack_ai_shared.agents.registry import AgentRegistry


class AgentOrchestrator:
    """Coordinate execution of registered AI agents."""

    def __init__(
        self,
        registry: AgentRegistry | None = None,
        context: AgentExecutionContext | None = None,
    ) -> None:
        """Initialize the orchestrator with shared agent services."""
        self.registry = registry or AgentRegistry()
        self.context = context or AgentExecutionContext()

    async def execute(
        self,
        agent_name: str,
        request: AgentRequest,
    ) -> AgentResult:
        """Execute a registered agent using the supplied request."""
        normalized_name = agent_name.strip()

        if not normalized_name:
            raise ValueError("Agent name must not be empty.")

        try:
            agent = self.registry.get(normalized_name)
        except KeyError as error:
            raise AgentNotFoundError(
                f"Agent '{normalized_name}' is not registered."
            ) from error

        try:
            result = await agent.run(request)
        except Exception as error:
            raise AgentExecutionError(
                f"Agent '{normalized_name}' execution failed."
            ) from error

        if result.agent_name != normalized_name:
            raise AgentExecutionError(
                "Agent result name does not match the executed agent: "
                f"expected '{normalized_name}', received "
                f"'{result.agent_name}'."
            )

        return result

    async def execute_task(
        self,
        agent_name: str,
        task: str,
        context: dict[str, object] | None = None,
    ) -> AgentResult:
        """Create an agent request and execute the selected agent."""
        if not task.strip():
            raise ValueError("Agent task must not be empty.")

        request = AgentRequest(
            task=task,
            context=context or {},
        )

        return await self.execute(agent_name, request)

## Step 16.10 — code tests\test_orchestrator.py

"""Tests for the shared AI-agent orchestrator."""

import pytest

from full_stack_ai_shared.agents import (
    AgentExecutionContext,
    AgentExecutionError,
    AgentNotFoundError,
    AgentOrchestrator,
    AgentRegistry,
    AgentRequest,
    AgentResult,
    BaseAgent,
)


class EchoAgent(BaseAgent):
    """Agent that returns the submitted task."""

    async def run(self, request: AgentRequest) -> AgentResult:
        """Return a successful result containing the request task."""
        return AgentResult(
            agent_name=self.name,
            success=True,
            output=f"Processed: {request.task}",
            metadata={
                "context": request.context,
            },
        )


class FailingAgent(BaseAgent):
    """Agent that raises an exception during execution."""

    async def run(self, request: AgentRequest) -> AgentResult:
        """Raise an execution failure."""
        raise RuntimeError(f"Unable to process: {request.task}")


class InvalidResultAgent(BaseAgent):
    """Agent that returns a result with an incorrect agent name."""

    async def run(self, request: AgentRequest) -> AgentResult:
        """Return a result associated with another agent."""
        return AgentResult(
            agent_name="different-agent",
            success=True,
            output=request.task,
        )


def test_agent_orchestrator_creates_default_dependencies() -> None:
    """Orchestrator should create default shared dependencies."""
    orchestrator = AgentOrchestrator()

    assert isinstance(orchestrator.registry, AgentRegistry)
    assert isinstance(orchestrator.context, AgentExecutionContext)
    assert len(orchestrator.registry) == 0


def test_agent_orchestrator_uses_supplied_dependencies() -> None:
    """Orchestrator should preserve explicitly supplied dependencies."""
    registry = AgentRegistry()
    context = AgentExecutionContext()

    orchestrator = AgentOrchestrator(
        registry=registry,
        context=context,
    )

    assert orchestrator.registry is registry
    assert orchestrator.context is context


@pytest.mark.asyncio
async def test_agent_orchestrator_executes_registered_agent() -> None:
    """Orchestrator should execute a registered agent."""
    registry = AgentRegistry()
    registry.register(EchoAgent(name="echo-agent"))
    orchestrator = AgentOrchestrator(registry=registry)
    request = AgentRequest(task="Analyze equipment health")

    result = await orchestrator.execute(
        agent_name="echo-agent",
        request=request,
    )

    assert result.agent_name == "echo-agent"
    assert result.success is True
    assert result.output == "Processed: Analyze equipment health"


@pytest.mark.asyncio
async def test_agent_orchestrator_passes_request_context() -> None:
    """Orchestrator should pass request context to the selected agent."""
    registry = AgentRegistry()
    registry.register(EchoAgent(name="echo-agent"))
    orchestrator = AgentOrchestrator(registry=registry)
    request = AgentRequest(
        task="Review maintenance history",
        context={
            "asset_id": "pump-101",
            "priority": "high",
        },
    )

    result = await orchestrator.execute(
        agent_name="echo-agent",
        request=request,
    )

    assert result.metadata["context"] == {
        "asset_id": "pump-101",
        "priority": "high",
    }


@pytest.mark.asyncio
async def test_agent_orchestrator_rejects_unknown_agent() -> None:
    """Orchestrator should raise an error for an unknown agent."""
    orchestrator = AgentOrchestrator()

    with pytest.raises(
        AgentNotFoundError,
        match="Agent 'missing-agent' is not registered.",
    ):
        await orchestrator.execute(
            agent_name="missing-agent",
            request=AgentRequest(task="Analyze asset"),
        )


@pytest.mark.asyncio
async def test_agent_orchestrator_rejects_empty_agent_name() -> None:
    """Orchestrator should reject an empty agent name."""
    orchestrator = AgentOrchestrator()

    with pytest.raises(
        ValueError,
        match="Agent name must not be empty.",
    ):
        await orchestrator.execute(
            agent_name="   ",
            request=AgentRequest(task="Analyze asset"),
        )


@pytest.mark.asyncio
async def test_agent_orchestrator_wraps_agent_failure() -> None:
    """Orchestrator should wrap exceptions raised by agents."""
    registry = AgentRegistry()
    registry.register(FailingAgent(name="failing-agent"))
    orchestrator = AgentOrchestrator(registry=registry)

    with pytest.raises(
        AgentExecutionError,
        match="Agent 'failing-agent' execution failed.",
    ) as exception_info:
        await orchestrator.execute(
            agent_name="failing-agent",
            request=AgentRequest(task="Analyze asset"),
        )

    assert isinstance(exception_info.value.__cause__, RuntimeError)


@pytest.mark.asyncio
async def test_agent_orchestrator_rejects_mismatched_result_name() -> None:
    """Orchestrator should reject results associated with another agent."""
    registry = AgentRegistry()
    registry.register(InvalidResultAgent(name="invalid-result-agent"))
    orchestrator = AgentOrchestrator(registry=registry)

    with pytest.raises(
        AgentExecutionError,
        match=(
            "Agent result name does not match the executed agent: "
            "expected 'invalid-result-agent', received "
            "'different-agent'."
        ),
    ):
        await orchestrator.execute(
            agent_name="invalid-result-agent",
            request=AgentRequest(task="Analyze asset"),
        )


@pytest.mark.asyncio
async def test_agent_orchestrator_executes_task() -> None:
    """Orchestrator should create a request from a task."""
    registry = AgentRegistry()
    registry.register(EchoAgent(name="echo-agent"))
    orchestrator = AgentOrchestrator(registry=registry)

    result = await orchestrator.execute_task(
        agent_name="echo-agent",
        task="Generate maintenance recommendation",
        context={
            "asset_id": "compressor-202",
        },
    )

    assert result.output == "Processed: Generate maintenance recommendation"
    assert result.metadata["context"] == {
        "asset_id": "compressor-202",
    }


@pytest.mark.asyncio
async def test_agent_orchestrator_execute_task_uses_empty_context() -> None:
    """Task execution should use an empty context by default."""
    registry = AgentRegistry()
    registry.register(EchoAgent(name="echo-agent"))
    orchestrator = AgentOrchestrator(registry=registry)

    result = await orchestrator.execute_task(
        agent_name="echo-agent",
        task="Inspect asset",
    )

    assert result.metadata["context"] == {}


@pytest.mark.asyncio
async def test_agent_orchestrator_rejects_empty_task() -> None:
    """Task execution should reject empty task descriptions."""
    registry = AgentRegistry()
    registry.register(EchoAgent(name="echo-agent"))
    orchestrator = AgentOrchestrator(registry=registry)

    with pytest.raises(
        ValueError,
        match="Agent task must not be empty.",
    ):
        await orchestrator.execute_task(
            agent_name="echo-agent",
            task="   ",
        )
## Step 16.11 — Export AgentOrchestrator        ## code src\full_stack_ai_shared\agents\__init__.py

"""Shared AI-agent abstractions."""

from full_stack_ai_shared.agents.base import (
    AgentRequest,
    AgentResult,
    BaseAgent,
)
from full_stack_ai_shared.agents.context import AgentExecutionContext
from full_stack_ai_shared.agents.exceptions import (
    AgentError,
    AgentExecutionError,
    AgentNotFoundError,
    AgentOrchestrationError,
    AgentRegistrationError,
)
from full_stack_ai_shared.agents.memory import (
    AgentMemory,
    MemoryEntry,
)
from full_stack_ai_shared.agents.orchestrator import AgentOrchestrator
from full_stack_ai_shared.agents.registry import AgentRegistry
from full_stack_ai_shared.agents.state import (
    AgentState,
    AgentStatus,
)

__all__ = [
    "AgentError",
    "AgentExecutionContext",
    "AgentExecutionError",
    "AgentMemory",
    "AgentNotFoundError",
    "AgentOrchestrationError",
    "AgentOrchestrator",
    "AgentRegistry",
    "AgentRegistrationError",
    "AgentRequest",
    "AgentResult",
    "AgentState",
    "AgentStatus",
    "BaseAgent",
    "MemoryEntry",
]

## Run

uv run ruff format src\full_stack_ai_shared\agents\orchestrator.py

uv run ruff check src\full_stack_ai_shared\agents\orchestrator.py

uv run mypy src

uv run pytest tests\test_orchestrator.py -v

uv run pytest `
    tests\test_agents.py `
    tests\test_agent_registry.py `
    tests\test_agent_exceptions.py `
    tests\test_orchestrator.py `
    -v


## Step 17 — Shared AI Tool Execution Framework

## Build a reusable tool framework that every future AI platform in your portfolio can use.

## Step 17.1 — Run Files

New-Item -ItemType File -Force `
src\full_stack_ai_shared\tools\context.py | Out-Null

New-Item -ItemType File -Force `
src\full_stack_ai_shared\tools\executor.py | Out-Null

New-Item -ItemType File -Force `
src\full_stack_ai_shared\tools\exceptions.py | Out-Null

New-Item -ItemType File -Force `
src\full_stack_ai_shared\tools\decorators.py | Out-Null

New-Item -ItemType File -Force `
tests\test_tool_context.py | Out-Null

New-Item -ItemType File -Force `
tests\test_tool_executor.py | Out-Null

New-Item -ItemType File -Force `
tests\test_tool_exceptions.py | Out-Null

New-Item -ItemType File -Force `
tests\test_tool_decorators.py | Out-Null

## Verify
Get-ChildItem src\full_stack_ai_shared\tools

Get-ChildItem tests\test_tool*.py

## tep 17.2 — Build Tool Exceptions

## code src\full_stack_ai_shared\tools\exceptions.py

"""Exceptions raised by shared AI-tool components."""


class ToolError(Exception):
    """Base exception for all shared AI-tool errors."""


class ToolRegistrationError(ToolError):
    """Raised when a tool cannot be registered."""


class ToolAlreadyRegisteredError(ToolRegistrationError):
    """Raised when a tool name has already been registered."""


class ToolNotFoundError(ToolError):
    """Raised when a requested tool is not registered."""


class ToolValidationError(ToolError):
    """Raised when tool input validation fails."""


class ToolExecutionError(ToolError):
    """Raised when a tool fails during execution."""

## code src\full_stack_ai_shared\tools\context.py

"""Execution context for shared AI-tool invocations."""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class ToolContext:
    """Provide metadata and identity details during tool execution."""

    execution_id: str = field(default_factory=lambda: str(uuid4()))
    agent_name: str | None = None
    user_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate context values after initialization."""
        if not self.execution_id.strip():
            raise ValueError("Tool execution ID must not be empty.")

        if self.agent_name is not None:
            normalized_agent_name = self.agent_name.strip()

            if not normalized_agent_name:
                raise ValueError("Agent name must not be empty.")

            self.agent_name = normalized_agent_name

        if self.user_id is not None:
            normalized_user_id = self.user_id.strip()

            if not normalized_user_id:
                raise ValueError("User ID must not be empty.")

            self.user_id = normalized_user_id

    def get_metadata(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """Return a metadata value or the supplied default."""
        normalized_key = key.strip()

        if not normalized_key:
            raise ValueError("Metadata key must not be empty.")

        return self.metadata.get(normalized_key, default)

    def set_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """Store a metadata value in the context."""
        normalized_key = key.strip()

        if not normalized_key:
            raise ValueError("Metadata key must not be empty.")

        self.metadata[normalized_key] = value

## code tests\test_tool_exceptions.py


"""Tests for shared AI-tool exceptions."""

import pytest

from full_stack_ai_shared.tools.exceptions import (
    ToolAlreadyRegisteredError,
    ToolError,
    ToolExecutionError,
    ToolNotFoundError,
    ToolRegistrationError,
    ToolValidationError,
)


@pytest.mark.parametrize(
    "exception_type",
    [
        ToolRegistrationError,
        ToolAlreadyRegisteredError,
        ToolNotFoundError,
        ToolValidationError,
        ToolExecutionError,
    ],
)
def test_tool_exceptions_inherit_from_tool_error(
    exception_type: type[ToolError],
) -> None:
    """Specialized tool exceptions should inherit from ToolError."""
    error = exception_type("Tool operation failed.")

    assert isinstance(error, ToolError)
    assert isinstance(error, Exception)


@pytest.mark.parametrize(
    ("exception_type", "message"),
    [
        (
            ToolError,
            "Generic tool failure.",
        ),
        (
            ToolRegistrationError,
            "Tool registration failed.",
        ),
        (
            ToolAlreadyRegisteredError,
            "Tool is already registered.",
        ),
        (
            ToolNotFoundError,
            "Requested tool was not found.",
        ),
        (
            ToolValidationError,
            "Tool input validation failed.",
        ),
        (
            ToolExecutionError,
            "Tool execution failed.",
        ),
    ],
)
def test_tool_exceptions_preserve_messages(
    exception_type: type[ToolError],
    message: str,
) -> None:
    """Tool exceptions should preserve supplied messages."""
    error = exception_type(message)

    assert str(error) == message


def test_tool_error_can_be_raised_and_caught() -> None:
    """ToolError should behave like a normal exception."""
    with pytest.raises(
        ToolError,
        match="Shared tool failure.",
    ):
        raise ToolError("Shared tool failure.")


def test_specialized_exception_can_be_caught_as_tool_error() -> None:
    """Specialized exceptions should be catchable as ToolError."""
    with pytest.raises(
        ToolError,
        match="Tool could not be executed.",
    ):
        raise ToolExecutionError("Tool could not be executed.")

## Run

uv run ruff format `
    src\full_stack_ai_shared\tools\exceptions.py `
    tests\test_tool_exceptions.py

uv run ruff check `
    src\full_stack_ai_shared\tools\exceptions.py `
    tests\test_tool_exceptions.py

uv run mypy src

uv run pytest tests\test_tool_exceptions.py -v

## Step 17.3 — Add Tool Context Tests

## code tests\test_tool_context.py

"""Tests for the shared AI-tool execution context."""

import pytest

from full_stack_ai_shared.tools import ToolContext


def test_tool_context_defaults() -> None:
    """ToolContext should provide generated defaults."""
    context = ToolContext()

    assert context.execution_id
    assert context.agent_name is None
    assert context.user_id is None
    assert context.metadata == {}


def test_tool_context_generates_unique_execution_ids() -> None:
    """ToolContext instances should receive unique execution IDs."""
    first_context = ToolContext()
    second_context = ToolContext()

    assert first_context.execution_id != second_context.execution_id


def test_tool_context_accepts_identity_values() -> None:
    """ToolContext should preserve supplied identity values."""
    context = ToolContext(
        agent_name="diagnostic-agent",
        user_id="user-101",
    )

    assert context.agent_name == "diagnostic-agent"
    assert context.user_id == "user-101"


def test_tool_context_normalizes_identity_values() -> None:
    """ToolContext should remove surrounding whitespace."""
    context = ToolContext(
        execution_id="  execution-101  ",
        agent_name="  diagnostic-agent  ",
        user_id="  user-101  ",
    )

    assert context.execution_id == "execution-101"
    assert context.agent_name == "diagnostic-agent"
    assert context.user_id == "user-101"


def test_tool_context_accepts_initial_metadata() -> None:
    """ToolContext should preserve supplied metadata."""
    context = ToolContext(
        metadata={
            "asset_id": "pump-101",
            "priority": "high",
        }
    )

    assert context.metadata == {
        "asset_id": "pump-101",
        "priority": "high",
    }


def test_tool_context_sets_metadata() -> None:
    """ToolContext should store metadata values."""
    context = ToolContext()

    context.set_metadata("asset_id", "compressor-202")

    assert context.metadata["asset_id"] == "compressor-202"


def test_tool_context_normalizes_metadata_keys() -> None:
    """Metadata operations should normalize key whitespace."""
    context = ToolContext()

    context.set_metadata("  asset_id  ", "pump-101")

    assert context.metadata == {
        "asset_id": "pump-101",
    }
    assert context.get_metadata("  asset_id  ") == "pump-101"


def test_tool_context_gets_existing_metadata() -> None:
    """ToolContext should return existing metadata values."""
    context = ToolContext(
        metadata={
            "asset_id": "pump-101",
        }
    )

    assert context.get_metadata("asset_id") == "pump-101"


def test_tool_context_gets_default_for_missing_metadata() -> None:
    """ToolContext should return a default for missing metadata."""
    context = ToolContext()

    result = context.get_metadata(
        "priority",
        "normal",
    )

    assert result == "normal"


@pytest.mark.parametrize(
    ("field_name", "field_value", "message"),
    [
        (
            "execution_id",
            "",
            "Tool execution ID must not be empty.",
        ),
        (
            "execution_id",
            "   ",
            "Tool execution ID must not be empty.",
        ),
        (
            "agent_name",
            "",
            "Agent name must not be empty.",
        ),
        (
            "agent_name",
            "   ",
            "Agent name must not be empty.",
        ),
        (
            "user_id",
            "",
            "User ID must not be empty.",
        ),
        (
            "user_id",
            "   ",
            "User ID must not be empty.",
        ),
    ],
)
def test_tool_context_rejects_empty_identity_values(
    field_name: str,
    field_value: str,
    message: str,
) -> None:
    """ToolContext should reject empty identity fields."""
    values = {
        field_name: field_value,
    }

    with pytest.raises(
        ValueError,
        match=message,
    ):
        ToolContext(**values)


@pytest.mark.parametrize(
    "metadata_key",
    [
        "",
        "   ",
    ],
)
def test_tool_context_set_metadata_rejects_empty_key(
    metadata_key: str,
) -> None:
    """set_metadata should reject empty keys."""
    context = ToolContext()

    with pytest.raises(
        ValueError,
        match="Metadata key must not be empty.",
    ):
        context.set_metadata(
            metadata_key,
            "value",
        )


@pytest.mark.parametrize(
    "metadata_key",
    [
        "",
        "   ",
    ],
)
def test_tool_context_get_metadata_rejects_empty_key(
    metadata_key: str,
) -> None:
    """get_metadata should reject empty keys."""
    context = ToolContext()

    with pytest.raises(
        ValueError,
        match="Metadata key must not be empty.",
    ):
        context.get_metadata(metadata_key)

## code src\full_stack_ai_shared\tools\context.py

"""Execution context for shared AI-tool invocations."""

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class ToolContext:
    """Provide metadata and identity details during tool execution."""

    execution_id: str = field(default_factory=lambda: str(uuid4()))
    agent_name: str | None = None
    user_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate and normalize context values."""
        normalized_execution_id = self.execution_id.strip()

        if not normalized_execution_id:
            raise ValueError("Tool execution ID must not be empty.")

        self.execution_id = normalized_execution_id

        if self.agent_name is not None:
            normalized_agent_name = self.agent_name.strip()

            if not normalized_agent_name:
                raise ValueError("Agent name must not be empty.")

            self.agent_name = normalized_agent_name

        if self.user_id is not None:
            normalized_user_id = self.user_id.strip()

            if not normalized_user_id:
                raise ValueError("User ID must not be empty.")

            self.user_id = normalized_user_id

    def get_metadata(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """Return a metadata value or the supplied default."""
        normalized_key = key.strip()

        if not normalized_key:
            raise ValueError("Metadata key must not be empty.")

        return self.metadata.get(normalized_key, default)

    def set_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """Store a metadata value in the context."""
        normalized_key = key.strip()

        if not normalized_key:
            raise ValueError("Metadata key must not be empty.")

        self.metadata[normalized_key] = value

## Run

uv run ruff format `
    src\full_stack_ai_shared\tools\context.py `
    tests\test_tool_context.py

uv run ruff check `
    src\full_stack_ai_shared\tools\context.py `
    tests\test_tool_context.py

uv run mypy src

uv run pytest tests\test_tool_context.py -v

## Add - code src\full_stack_ai_shared\tools\executor.py

"""Execution service for registered shared AI tools."""

from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.exceptions import ToolNotFoundError
from full_stack_ai_shared.tools.models import ToolRequest, ToolResult
from full_stack_ai_shared.tools.registry import ToolRegistry


class ToolExecutor:
    """Execute tool requests through a shared tool registry."""

    def __init__(self, registry: ToolRegistry) -> None:
        """Initialize the executor with a tool registry."""
        self._registry = registry

    @property
    def registry(self) -> ToolRegistry:
        """Return the tool registry used by the executor."""
        return self._registry

    async def execute(
        self,
        request: ToolRequest,
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Execute a tool request and return a normalized result."""
        execution_context = context or ToolContext(
            request_id=request.request_id,
        )

        try:
            result = await self._registry.execute_request(
                request=request,
                context=execution_context,
            )
        except ToolNotFoundError as error:
            return ToolResult(
                tool_name=request.tool_name,
                success=False,
                error=str(error),
                request_id=request.request_id,
            )
        except Exception as error:
            return ToolResult(
                tool_name=request.tool_name,
                success=False,
                error=f"Tool execution failed: {error}",
                request_id=request.request_id,
            )

        result.request_id = request.request_id
        return result

## code tests\test_tool_executor.py

"""Tests for the shared AI tool executor."""

from typing import Any

import pytest

from full_stack_ai_shared.tools import (
    BaseTool,
    ToolContext,
    ToolExecutor,
    ToolRegistry,
    ToolRequest,
    ToolResult,
)


class EchoTool(BaseTool):
    """Return the submitted message."""

    def __init__(self) -> None:
        """Initialize the echo tool."""
        super().__init__(
            name="echo",
            description="Return a submitted message.",
            input_schema={
                "type": "object",
                "properties": {
                    "message": {"type": "string"},
                },
                "required": ["message"],
            },
        )

    async def execute(
        self,
        arguments: dict[str, Any],
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Return the message supplied in the arguments."""
        return ToolResult(
            tool_name=self.name,
            success=True,
            output=arguments["message"],
            metadata={
                "request_id": context.request_id if context else None,
            },
        )


class FailingTool(BaseTool):
    """Raise an exception during execution."""

    def __init__(self) -> None:
        """Initialize the failing tool."""
        super().__init__(
            name="failing-tool",
            description="Raise an execution error.",
        )

    async def execute(
        self,
        arguments: dict[str, Any],
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Raise an intentional execution exception."""
        raise RuntimeError("Intentional tool failure.")


@pytest.mark.asyncio
async def test_executor_runs_registered_tool() -> None:
    """Executor should run a registered tool successfully."""
    registry = ToolRegistry()
    registry.register(EchoTool())

    executor = ToolExecutor(registry)
    request = ToolRequest(
        tool_name="echo",
        arguments={"message": "Hello from the executor."},
    )

    result = await executor.execute(request)

    assert result.success is True
    assert result.tool_name == "echo"
    assert result.output == "Hello from the executor."
    assert result.error is None
    assert result.request_id == request.request_id


@pytest.mark.asyncio
async def test_executor_creates_default_context() -> None:
    """Executor should create a context using the request identifier."""
    registry = ToolRegistry()
    registry.register(EchoTool())

    executor = ToolExecutor(registry)
    request = ToolRequest(
        tool_name="echo",
        arguments={"message": "Context test"},
    )

    result = await executor.execute(request)

    assert result.success is True
    assert result.metadata["request_id"] == request.request_id


@pytest.mark.asyncio
async def test_executor_uses_supplied_context() -> None:
    """Executor should pass a supplied context to the tool."""
    registry = ToolRegistry()
    registry.register(EchoTool())

    executor = ToolExecutor(registry)
    request = ToolRequest(
        tool_name="echo",
        arguments={"message": "Custom context"},
    )
    context = ToolContext(
        request_id="custom-request-id",
        metadata={"source": "test"},
    )

    result = await executor.execute(
        request=request,
        context=context,
    )

    assert result.success is True
    assert result.metadata["request_id"] == "custom-request-id"
    assert result.request_id == request.request_id


@pytest.mark.asyncio
async def test_executor_returns_failure_for_unknown_tool() -> None:
    """Executor should normalize unknown-tool errors."""
    executor = ToolExecutor(ToolRegistry())
    request = ToolRequest(tool_name="missing-tool")

    result = await executor.execute(request)

    assert result.success is False
    assert result.tool_name == "missing-tool"
    assert result.output is None
    assert result.error is not None
    assert "missing-tool" in result.error
    assert result.request_id == request.request_id


@pytest.mark.asyncio
async def test_executor_returns_failure_for_tool_exception() -> None:
    """Executor should normalize unexpected execution exceptions."""
    registry = ToolRegistry()
    registry.register(FailingTool())

    executor = ToolExecutor(registry)
    request = ToolRequest(tool_name="failing-tool")

    result = await executor.execute(request)

    assert result.success is False
    assert result.tool_name == "failing-tool"
    assert result.error == (
        "Tool execution failed: Intentional tool failure."
    )
    assert result.request_id == request.request_id


def test_executor_exposes_registry() -> None:
    """Executor should expose its configured registry."""
    registry = ToolRegistry()
    executor = ToolExecutor(registry)

    assert executor.registry is registry

## Export - code src\full_stack_ai_shared\tools\__init__.py

"""Shared AI tool abstractions and execution services."""

from full_stack_ai_shared.tools.base import BaseTool
from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.exceptions import (
    ToolAlreadyRegisteredError,
    ToolError,
    ToolNotFoundError,
)
from full_stack_ai_shared.tools.executor import ToolExecutor
from full_stack_ai_shared.tools.models import (
    ToolDefinition,
    ToolRequest,
    ToolResult,
)
from full_stack_ai_shared.tools.registry import ToolRegistry

__all__ = [
    "BaseTool",
    "ToolAlreadyRegisteredError",
    "ToolContext",
    "ToolDefinition",
    "ToolError",
    "ToolExecutor",
    "ToolNotFoundError",
    "ToolRegistry",
    "ToolRequest",
    "ToolResult",
]

## Run

uv run ruff format `
    src\full_stack_ai_shared\tools\executor.py `
    src\full_stack_ai_shared\tools\__init__.py `
    tests\test_tool_executor.py

uv run ruff check `
    src\full_stack_ai_shared\tools\executor.py `
    src\full_stack_ai_shared\tools\__init__.py `
    tests\test_tool_executor.py

uv run mypy src

 uv run pytest tests\test_tool_executor.py 

uv run pytest `
    tests\test_tool_context.py `
    tests\test_tool_registry.py `
    tests\test_tool_executor.py `
    -v

Run

git status
git add `
shared-infrastructure/python/src/full_stack_ai_shared/tools/__init__.py `
shared-infrastructure/python/src/full_stack_ai_shared/tools/context.py `
shared-infrastructure/python/src/full_stack_ai_shared/tools/decorators.py `
shared-infrastructure/python/src/full_stack_ai_shared/tools/exceptions.py `
shared-infrastructure/python/src/full_stack_ai_shared/tools/executor.py `
shared-infrastructure/python/tests/test_tool_context.py `
shared-infrastructure/python/tests/test_tool_decorators.py `
shared-infrastructure/python/tests/test_tool_exceptions.py `
shared-infrastructure/python/tests/test_tool_executor.py

git commit -m "Add shared AI agent orchestration and tool execution framework"
git status

## Step 16 — Shared AI Agent Planning Framework

This layer will allow agents to convert a user request into structured, ordered execution steps before the orchestrator runs them.

## Step 16.1 — Create the Agent Plan Models
## From the parent project folder:

## cd shared-infrastructure\python

## Files

New-Item -ItemType File -Force `
    src\full_stack_ai_shared\agents\planning.py | Out-Null

New-Item -ItemType File -Force `
    tests\test_agent_planning.py | Out-Null

## File 1 — code src\full_stack_ai_shared\agents\planning.py

"""Planning models for shared AI-agent workflows."""

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any
from uuid import uuid4


class PlanStepStatus(StrEnum):
    """Represent the execution status of an agent plan step."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass(slots=True)
class AgentPlanStep:
    """Represent one executable step in an agent plan."""

    description: str
    step_id: str = field(default_factory=lambda: str(uuid4()))
    tool_name: str | None = None
    agent_name: str | None = None
    arguments: dict[str, Any] = field(default_factory=dict)
    status: PlanStepStatus = PlanStepStatus.PENDING
    result: Any = None
    error: str | None = None

    def __post_init__(self) -> None:
        """Validate the plan step after initialization."""
        if not self.description.strip():
            raise ValueError("Plan step description must not be empty.")

        if not self.step_id.strip():
            raise ValueError("Plan step ID must not be empty.")

        if self.tool_name is not None and not self.tool_name.strip():
            raise ValueError("Tool name must not be empty.")

        if self.agent_name is not None and not self.agent_name.strip():
            raise ValueError("Agent name must not be empty.")

    def mark_running(self) -> None:
        """Mark the plan step as currently running."""
        self.status = PlanStepStatus.RUNNING
        self.error = None

    def mark_completed(self, result: Any = None) -> None:
        """Mark the plan step as successfully completed."""
        self.status = PlanStepStatus.COMPLETED
        self.result = result
        self.error = None

    def mark_failed(self, error: str) -> None:
        """Mark the plan step as failed."""
        if not error.strip():
            raise ValueError("Plan step error must not be empty.")

        self.status = PlanStepStatus.FAILED
        self.error = error

    def mark_skipped(self) -> None:
        """Mark the plan step as skipped."""
        self.status = PlanStepStatus.SKIPPED


@dataclass(slots=True)
class AgentPlan:
    """Represent an ordered execution plan for an AI agent."""

    objective: str
    plan_id: str = field(default_factory=lambda: str(uuid4()))
    steps: list[AgentPlanStep] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate the agent plan after initialization."""
        if not self.objective.strip():
            raise ValueError("Agent plan objective must not be empty.")

        if not self.plan_id.strip():
            raise ValueError("Agent plan ID must not be empty.")

    @property
    def is_complete(self) -> bool:
        """Return whether every plan step has reached a terminal state."""
        terminal_statuses = {
            PlanStepStatus.COMPLETED,
            PlanStepStatus.FAILED,
            PlanStepStatus.SKIPPED,
        }

        return bool(self.steps) and all(
            step.status in terminal_statuses for step in self.steps
        )

    @property
    def has_failures(self) -> bool:
        """Return whether any plan step has failed."""
        return any(step.status == PlanStepStatus.FAILED for step in self.steps)

    def add_step(self, step: AgentPlanStep) -> None:
        """Append a step to the execution plan."""
        self.steps.append(step)

    def get_step(self, step_id: str) -> AgentPlanStep:
        """Return a plan step by its identifier."""
        for step in self.steps:
            if step.step_id == step_id:
                return step

        raise KeyError(f"Plan step '{step_id}' was not found.")

## File 2 — code tests\test_agent_planning.py

"""Tests for shared AI-agent planning models."""

import pytest

from full_stack_ai_shared.agents.planning import (
    AgentPlan,
    AgentPlanStep,
    PlanStepStatus,
)


def test_agent_plan_step_defaults() -> None:
    """Plan steps should provide generated IDs and pending status."""
    step = AgentPlanStep(description="Retrieve maintenance records.")

    assert step.step_id
    assert step.description == "Retrieve maintenance records."
    assert step.tool_name is None
    assert step.agent_name is None
    assert step.arguments == {}
    assert step.status == PlanStepStatus.PENDING
    assert step.result is None
    assert step.error is None


def test_agent_plan_step_marks_running() -> None:
    """Plan steps should transition to running."""
    step = AgentPlanStep(description="Search enterprise documents.")

    step.mark_running()

    assert step.status == PlanStepStatus.RUNNING
    assert step.error is None


def test_agent_plan_step_marks_completed() -> None:
    """Plan steps should store successful execution results."""
    step = AgentPlanStep(description="Analyze retrieved records.")

    step.mark_completed({"risk_level": "medium"})

    assert step.status == PlanStepStatus.COMPLETED
    assert step.result == {"risk_level": "medium"}
    assert step.error is None


def test_agent_plan_step_marks_failed() -> None:
    """Plan steps should store execution errors."""
    step = AgentPlanStep(description="Call diagnostic tool.")

    step.mark_failed("Diagnostic tool was unavailable.")

    assert step.status == PlanStepStatus.FAILED
    assert step.error == "Diagnostic tool was unavailable."


def test_agent_plan_step_rejects_empty_description() -> None:
    """Plan steps should reject empty descriptions."""
    with pytest.raises(
        ValueError,
        match="Plan step description must not be empty.",
    ):
        AgentPlanStep(description="   ")


def test_agent_plan_defaults() -> None:
    """Agent plans should provide generated IDs and empty collections."""
    plan = AgentPlan(objective="Analyze equipment health.")

    assert plan.plan_id
    assert plan.objective == "Analyze equipment health."
    assert plan.steps == []
    assert plan.metadata == {}
    assert plan.is_complete is False
    assert plan.has_failures is False


def test_agent_plan_adds_and_retrieves_step() -> None:
    """Agent plans should store and retrieve ordered steps."""
    plan = AgentPlan(objective="Analyze equipment health.")
    step = AgentPlanStep(description="Retrieve sensor readings.")

    plan.add_step(step)

    assert plan.steps == [step]
    assert plan.get_step(step.step_id) is step


def test_agent_plan_reports_completion() -> None:
    """Agent plans should report completion for terminal steps."""
    completed_step = AgentPlanStep(description="Retrieve data.")
    skipped_step = AgentPlanStep(description="Request human review.")

    completed_step.mark_completed({"records": 10})
    skipped_step.mark_skipped()

    plan = AgentPlan(
        objective="Analyze equipment health.",
        steps=[completed_step, skipped_step],
    )

    assert plan.is_complete is True
    assert plan.has_failures is False


def test_agent_plan_reports_failures() -> None:
    """Agent plans should report failed steps."""
    step = AgentPlanStep(description="Execute diagnostic tool.")
    step.mark_failed("Execution failed.")

    plan = AgentPlan(
        objective="Analyze equipment health.",
        steps=[step],
    )

    assert plan.is_complete is True
    assert plan.has_failures is True


def test_agent_plan_get_step_rejects_unknown_id() -> None:
    """Agent plans should reject unknown step identifiers."""
    plan = AgentPlan(objective="Analyze equipment health.")

    with pytest.raises(
        KeyError,
        match="Plan step 'missing-step' was not found.",
    ):
        plan.get_step("missing-step")

## Update the public agents API     code src\full_stack_ai_shared\agents\__init__.py

from full_stack_ai_shared.agents.planning import (
    AgentPlan,
    AgentPlanStep,
    PlanStepStatus,
)

Add these names to __all__:

"AgentPlan",
"AgentPlanStep",
"PlanStepStatus",

## Run

uv run ruff format `
    src\full_stack_ai_shared\agents\planning.py `
    src\full_stack_ai_shared\agents\__init__.py `
    tests\test_agent_planning.py

uv run ruff check `
    src\full_stack_ai_shared\agents\planning.py `
    src\full_stack_ai_shared\agents\__init__.py `
    tests\test_agent_planning.py

uv run mypy src

## Get-Content tests\test_agent_planning.py

## code tests\test_agent_planning.py

"""Tests for the shared agent planning components."""

from full_stack_ai_shared.agents import (
    AgentExecutionContext,
    PlanningAgent,
    PlanningRequest,
    PlanningResult,
)


def test_planning_request_defaults() -> None:
    """PlanningRequest should initialize with default values."""
    request = PlanningRequest(
        goal="Build an enterprise AI platform",
    )

    assert request.goal == "Build an enterprise AI platform"
    assert request.context == {}
    assert request.constraints == []


def test_planning_request_custom_values() -> None:
    """PlanningRequest should preserve supplied values."""
    request = PlanningRequest(
        goal="Deploy AI service",
        context={"environment": "production"},
        constraints=["budget", "time"],
    )

    assert request.context["environment"] == "production"
    assert request.constraints == ["budget", "time"]


def test_planning_result_defaults() -> None:
    """PlanningResult should store generated execution plan."""
    result = PlanningResult(
        goal="Create API",
        steps=[
            "Design architecture",
            "Implement endpoints",
            "Write tests",
        ],
    )

    assert result.goal == "Create API"
    assert len(result.steps) == 3
    assert result.metadata == {}


def test_planning_result_metadata() -> None:
    """PlanningResult should preserve metadata."""
    result = PlanningResult(
        goal="Deploy platform",
        steps=["Deploy"],
        metadata={"estimated_hours": 8},
    )

    assert result.metadata["estimated_hours"] == 8


def test_planning_agent_generates_plan() -> None:
    """PlanningAgent should create a sequential execution plan."""
    agent = PlanningAgent()
    context = AgentExecutionContext()

    request = PlanningRequest(
        goal="Develop predictive maintenance application"
    )

    result = agent.plan(
        request=request,
        context=context,
    )

    assert isinstance(result, PlanningResult)
    assert result.goal == request.goal
    assert len(result.steps) >= 1
    assert any("predictive" in step.lower() or "develop" in step.lower() for step in result.steps)


def test_planning_agent_returns_metadata() -> None:
    """PlanningAgent should include planning metadata."""
    agent = PlanningAgent()

    result = agent.plan(
        request=PlanningRequest(goal="Build AI assistant"),
        context=AgentExecutionContext(),
    )

    assert isinstance(result.metadata, dict)


def test_planning_agent_empty_goal() -> None:
    """PlanningAgent should reject an empty goal."""
    agent = PlanningAgent()

    try:
        agent.plan(
            request=PlanningRequest(goal=""),
            context=AgentExecutionContext(),
        )
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for empty goal.")

## Run

uv run ruff format tests\test_agent_planning.py
uv run ruff check tests\test_agent_planning.py
uv run mypy src
uv run pytest tests\test_agent_planning.py -v

## code src\full_stack_ai_shared\agents\__init__.py

from full_stack_ai_shared.agents.planning import (
    PlanningAgent,
    PlanningRequest,
    PlanningResult,
)

## Run

uv run ruff format tests\test_agent_planning.py

uv run ruff check src\full_stack_ai_shared\agents\planning.py src\full_stack_ai_shared\agents\__init__.py tests\test_agent_planning.py

uv run mypy src

uv run pytest tests\test_agent_planning.py -v

uv run ruff format `
    src\full_stack_ai_shared\tools\exceptions.py `
    src\full_stack_ai_shared\tools\__init__.py

uv run ruff check `
    src\full_stack_ai_shared\tools\exceptions.py `
    src\full_stack_ai_shared\tools\__init__.py `
    tests\test_tool_exceptions.py

uv run pytest tests\test_tool_exceptions.py -v

## code src\full_stack_ai_shared\tools\decorators.py

"""Function-based tool implementations and decorators."""

from collections.abc import Awaitable, Callable
from inspect import isawaitable
from typing import Any

from full_stack_ai_shared.tools.base import BaseTool
from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.models import ToolResult

ToolFunction = Callable[..., Any | Awaitable[Any]]


class FunctionTool(BaseTool):
    """Expose a Python function through the shared tool interface."""

    def __init__(
        self,
        name: str,
        description: str,
        function: ToolFunction,
        input_schema: dict[str, Any] | None = None,
    ) -> None:
        """Initialize the function-backed tool."""
        super().__init__(
            name=name,
            description=description,
            input_schema=input_schema,
        )
        self._function = function

    async def execute(
        self,
        arguments: dict[str, Any],
        context: ToolContext | None = None,
    ) -> ToolResult:
        """Execute the wrapped function with the provided arguments."""
        del context

        try:
            output = self._function(**arguments)

            if isawaitable(output):
                output = await output

            return ToolResult(
                tool_name=self.name,
                success=True,
                output=output,
            )
        except Exception as error:
            return ToolResult(
                tool_name=self.name,
                success=False,
                error=str(error),
            )


def tool(
    name: str,
    description: str,
    input_schema: dict[str, Any] | None = None,
) -> Callable[[ToolFunction], FunctionTool]:
    """Convert a Python function into a shared AI tool."""

    def decorator(function: ToolFunction) -> FunctionTool:
        return FunctionTool(
            name=name,
            description=description,
            function=function,
            input_schema=input_schema,
        )

    return decorator

## code src\full_stack_ai_shared\tools\__init__.py

"""Shared AI tool abstractions and execution services."""

from full_stack_ai_shared.tools.base import BaseTool
from full_stack_ai_shared.tools.context import ToolContext
from full_stack_ai_shared.tools.decorators import FunctionTool, tool
from full_stack_ai_shared.tools.exceptions import (
    ToolAlreadyRegisteredError,
    ToolError,
    ToolExecutionError,
    ToolNotFoundError,
)
from full_stack_ai_shared.tools.executor import ToolExecutor
from full_stack_ai_shared.tools.models import (
    ToolDefinition,
    ToolRequest,
    ToolResult,
)
from full_stack_ai_shared.tools.registry import ToolRegistry

__all__ = [
    "BaseTool",
    "FunctionTool",
    "ToolAlreadyRegisteredError",
    "ToolContext",
    "ToolDefinition",
    "ToolError",
    "ToolExecutionError",
    "ToolExecutor",
    "ToolNotFoundError",
    "ToolRegistry",
    "ToolRequest",
    "ToolResult",
    "tool",
]

## Run

uv run ruff format `
    src\full_stack_ai_shared\tools\decorators.py `
    src\full_stack_ai_shared\tools\__init__.py

uv run ruff check `
    src\full_stack_ai_shared\tools\decorators.py `
    src\full_stack_ai_shared\tools\__init__.py

uv run mypy src

uv run pytest `
    tests\test_tool_decorators.py `
    tests\test_tools_public_api.py `
    tests\test_tool_exceptions.py `
    uv run pytest -v
    -v

## Step 16.1 — Request Logging Middleware

        ## cd shared-infrastructure\python
        
        ##  1. Create the files

New-Item -ItemType Directory -Force `
    src\full_stack_ai_shared\middleware | Out-Null

New-Item -ItemType File -Force `
    src\full_stack_ai_shared\middleware\request_logging.py | Out-Null

New-Item -ItemType File -Force `
    src\full_stack_ai_shared\middleware\__init__.py | Out-Null

New-Item -ItemType File -Force `
    tests\test_request_logging_middleware.py | Out-Null

##  2. Add  -   code src\full_stack_ai_shared\middleware\request_logging.py

"""HTTP request logging middleware."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import Any

from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from full_stack_ai_shared.logging import (
    clear_request_id,
    create_request_id,
    get_logger,
    set_request_id,
)

logger = get_logger(__name__)


class RequestLoggingMiddleware:
    """Log incoming HTTP requests and outgoing responses."""

    def __init__(
        self,
        app: ASGIApp,
        *,
        request_id_header: str = "X-Request-ID",
    ) -> None:
        """Initialize the request logging middleware."""
        self.app = app
        self.request_id_header = request_id_header

    async def __call__(
        self,
        scope: Scope,
        receive: Receive,
        send: Send,
    ) -> None:
        """Process and log an HTTP request."""
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        request_id = self._get_request_id(scope)
        set_request_id(request_id)

        method = str(scope.get("method", "UNKNOWN"))
        path = str(scope.get("path", "/"))
        client_ip = self._get_client_ip(scope)

        status_code: int | None = None

        async def send_wrapper(message: Message) -> None:
            nonlocal status_code

            if message["type"] == "http.response.start":
                status_code = int(message["status"])

                headers = MutableHeaders(scope=message)
                headers[self.request_id_header] = request_id

            await send(message)

        logger.info(
            "HTTP request started",
            extra={
                "request_id": request_id,
                "http_method": method,
                "http_path": path,
                "client_ip": client_ip,
            },
        )

        try:
            await self.app(scope, receive, send_wrapper)
        except Exception:
            logger.exception(
                "HTTP request failed",
                extra={
                    "request_id": request_id,
                    "http_method": method,
                    "http_path": path,
                    "client_ip": client_ip,
                },
            )
            raise
        else:
            logger.info(
                "HTTP request completed",
                extra={
                    "request_id": request_id,
                    "http_method": method,
                    "http_path": path,
                    "client_ip": client_ip,
                    "status_code": status_code,
                },
            )
        finally:
            clear_request_id()

    def _get_request_id(self, scope: Scope) -> str:
        """Return an incoming request ID or create a new one."""
        header_name = self.request_id_header.lower().encode("latin-1")

        for name, value in scope.get("headers", []):
            if name.lower() == header_name:
                request_id = value.decode("latin-1").strip()

                if request_id:
                    return request_id

        return create_request_id()

    @staticmethod
    def _get_client_ip(scope: Scope) -> str | None:
        """Return the client IP address when available."""
        client: Any = scope.get("client")

        if not client:
            return None

        return str(client[0])


RequestHandler = Callable[[Scope, Receive, Send], Awaitable[None]]

##  Update the middleware package exports -     code src\full_stack_ai_shared\middleware\__init__.py

"""Reusable HTTP middleware components."""

from full_stack_ai_shared.middleware.request_logging import (
    RequestLoggingMiddleware,
)

__all__ = [
    "RequestLoggingMiddleware",
]

##  4. Add the middleware tests -       code tests\test_request_logging_middleware.py

"""Tests for request logging middleware."""

from __future__ import annotations

import logging
from collections.abc import Iterator

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from full_stack_ai_shared.logging import get_request_id
from full_stack_ai_shared.middleware import RequestLoggingMiddleware


@pytest.fixture
def app() -> FastAPI:
    """Create a FastAPI application with request logging enabled."""
    application = FastAPI()
    application.add_middleware(RequestLoggingMiddleware)

    @application.get("/health")
    async def health() -> dict[str, str | None]:
        return {
            "status": "healthy",
            "request_id": get_request_id(),
        }

    @application.get("/failure")
    async def failure() -> None:
        raise RuntimeError("Unexpected middleware test failure.")

    return application


@pytest.fixture
def anyio_backend() -> str:
    """Use asyncio for async tests."""
    return "asyncio"


@pytest.fixture
def log_records(
    caplog: pytest.LogCaptureFixture,
) -> Iterator[pytest.LogCaptureFixture]:
    """Capture middleware log records."""
    caplog.set_level(
        logging.INFO,
        logger="full_stack_ai_shared.middleware.request_logging",
    )

    yield caplog


@pytest.mark.anyio
async def test_middleware_adds_generated_request_id(
    app: FastAPI,
) -> None:
    """Middleware should generate and return a request ID."""
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:
        response = await client.get("/health")

    assert response.status_code == 200
    assert response.headers["X-Request-ID"]
    assert response.json()["request_id"] == response.headers["X-Request-ID"]


@pytest.mark.anyio
async def test_middleware_preserves_incoming_request_id(
    app: FastAPI,
) -> None:
    """Middleware should preserve a valid incoming request ID."""
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:
        response = await client.get(
            "/health",
            headers={"X-Request-ID": "request-123"},
        )

    assert response.status_code == 200
    assert response.headers["X-Request-ID"] == "request-123"
    assert response.json()["request_id"] == "request-123"


@pytest.mark.anyio
async def test_middleware_logs_request_start_and_completion(
    app: FastAPI,
    log_records: pytest.LogCaptureFixture,
) -> None:
    """Middleware should log request start and completion."""
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:
        response = await client.get(
            "/health",
            headers={"X-Request-ID": "logging-test-123"},
        )

    assert response.status_code == 200

    messages = [record.getMessage() for record in log_records.records]

    assert "HTTP request started" in messages
    assert "HTTP request completed" in messages

    completion_record = next(
        record
        for record in log_records.records
        if record.getMessage() == "HTTP request completed"
    )

    assert completion_record.request_id == "logging-test-123"
    assert completion_record.http_method == "GET"
    assert completion_record.http_path == "/health"
    assert completion_record.status_code == 200


@pytest.mark.anyio
async def test_middleware_logs_unhandled_exception(
    app: FastAPI,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Middleware should log exceptions before re-raising them."""
    caplog.set_level(
        logging.ERROR,
        logger="full_stack_ai_shared.middleware.request_logging",
    )

    transport = ASGITransport(
        app=app,
        raise_app_exceptions=True,
    )

    with pytest.raises(
        RuntimeError,
        match="Unexpected middleware test failure",
    ):
        async with AsyncClient(
            transport=transport,
            base_url="http://test",
        ) as client:
            await client.get(
                "/failure",
                headers={"X-Request-ID": "failure-test-123"},
            )

    failure_record = next(
        record
        for record in caplog.records
        if record.getMessage() == "HTTP request failed"
    )

    assert failure_record.request_id == "failure-test-123"
    assert failure_record.http_method == "GET"
    assert failure_record.http_path == "/failure"

## 5. Confirm the required dependencies

uv add fastapi starlette
uv add --dev httpx pytest pytest-asyncio
uv sync

## Run

uv run ruff format `
    src\full_stack_ai_shared\middleware\request_logging.py `
    src\full_stack_ai_shared\middleware\__init__.py `
    tests\test_request_logging_middleware.py

uv run ruff check `
    src\full_stack_ai_shared\middleware\request_logging.py `
    src\full_stack_ai_shared\middleware\__init__.py `
    tests\test_request_logging_middleware.py `
    --fix

uv run ruff check `
    src\full_stack_ai_shared\middleware\request_logging.py `
    src\full_stack_ai_shared\middleware\__init__.py `
    tests\test_request_logging_middleware.py

uv run mypy src

## Step 16.2 — Create Request Timing Middleware

Create two files:

New-Item -ItemType File -Force `
    src\full_stack_ai_shared\middleware\timing.py | Out-Null

New-Item -ItemType File -Force `
    tests\test_timing_middleware.py | Out-Null

Open 

## code src\full_stack_ai_shared\middleware\timing.py

"""HTTP request timing middleware."""

from __future__ import annotations

from time import perf_counter

from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from full_stack_ai_shared.logging import get_logger

logger = get_logger(__name__)


class RequestTimingMiddleware:
    """Measure and report HTTP request execution time."""

    def __init__(
        self,
        app: ASGIApp,
        *,
        process_time_header: str = "X-Process-Time",
    ) -> None:
        """Initialize the request timing middleware."""
        self.app = app
        self.process_time_header = process_time_header

    async def __call__(
        self,
        scope: Scope,
        receive: Receive,
        send: Send,
    ) -> None:
        """Measure the execution duration of an HTTP request."""
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        started_at = perf_counter()
        method = str(scope.get("method", "UNKNOWN"))
        path = str(scope.get("path", "/"))

        async def send_wrapper(message: Message) -> None:
            if message["type"] == "http.response.start":
                elapsed_seconds = perf_counter() - started_at
                headers = MutableHeaders(scope=message)
                headers[self.process_time_header] = f"{elapsed_seconds:.6f}"

            await send(message)

        try:
            await self.app(scope, receive, send_wrapper)
        finally:
            elapsed_seconds = perf_counter() - started_at

            logger.info(
                "HTTP request timing",
                extra={
                    "http_method": method,
                    "http_path": path,
                    "duration_seconds": elapsed_seconds,
                },
            )

## code tests\test_timing_middleware.py

"""Tests for HTTP request timing middleware."""

import logging

from fastapi import FastAPI
from fastapi.testclient import TestClient

from full_stack_ai_shared.middleware.timing import RequestTimingMiddleware


def create_test_app() -> FastAPI:
    """Create an application configured with timing middleware."""
    app = FastAPI()
    app.add_middleware(RequestTimingMiddleware)

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "healthy"}

    return app


def test_timing_middleware_adds_process_time_header() -> None:
    """Middleware should add the request processing duration header."""
    client = TestClient(create_test_app())

    response = client.get("/health")

    assert response.status_code == 200
    assert "X-Process-Time" in response.headers
    assert float(response.headers["X-Process-Time"]) >= 0


def test_timing_middleware_preserves_response_body() -> None:
    """Middleware should not modify the application response body."""
    client = TestClient(create_test_app())

    response = client.get("/health")

    assert response.json() == {"status": "healthy"}


def test_timing_middleware_logs_request_duration(
    caplog: logging.LogCaptureFixture,
) -> None:
    """Middleware should log request execution timing information."""
    client = TestClient(create_test_app())

    with caplog.at_level(logging.INFO):
        response = client.get("/health")

    assert response.status_code == 200
    assert "HTTP request timing" in caplog.text

## Export the middleware - code src\full_stack_ai_shared\middleware\__init__.py

"""Reusable HTTP middleware components."""

from full_stack_ai_shared.middleware.request_logging import (
    RequestLoggingMiddleware,
)
from full_stack_ai_shared.middleware.timing import RequestTimingMiddleware

__all__ = [
    "RequestLoggingMiddleware",
    "RequestTimingMiddleware",
]

## Run

uv run ruff format `
    src\full_stack_ai_shared\middleware\timing.py `
    src\full_stack_ai_shared\middleware\__init__.py `
    tests\test_timing_middleware.py

uv run ruff check `
    src\full_stack_ai_shared\middleware\timing.py `
    src\full_stack_ai_shared\middleware\__init__.py `
    tests\test_timing_middleware.py

uv run mypy src

uv run pytest tests\test_timing_middleware.py -v

## Step 16.3 — Create Exception Handler Middleware

New-Item -ItemType File -Force `
    src\full_stack_ai_shared\middleware\exception_handler.py | Out-Null

New-Item -ItemType File -Force `
    tests\test_exception_handler_middleware.py | Out-Null

## code src\full_stack_ai_shared\middleware\exception_handler.py

"""Unhandled exception middleware."""

from __future__ import annotations

from http import HTTPStatus

from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

from full_stack_ai_shared.logging import get_logger, get_request_id

logger = get_logger(__name__)


class ExceptionHandlerMiddleware:
    """Convert unhandled application exceptions into JSON responses."""

    def __init__(
        self,
        app: ASGIApp,
        *,
        include_exception_details: bool = False,
    ) -> None:
        """Initialize the exception handler middleware."""
        self.app = app
        self.include_exception_details = include_exception_details

    async def __call__(
        self,
        scope: Scope,
        receive: Receive,
        send: Send,
    ) -> None:
        """Handle unhandled HTTP application exceptions."""
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        try:
            await self.app(scope, receive, send)
        except Exception as exc:
            request_id = get_request_id()

            logger.exception(
                "Unhandled HTTP application exception",
                extra={
                    "request_id": request_id,
                    "http_method": str(scope.get("method", "UNKNOWN")),
                    "http_path": str(scope.get("path", "/")),
                    "exception_type": type(exc).__name__,
                },
            )

            response_content: dict[str, str | int | None] = {
                "status_code": HTTPStatus.INTERNAL_SERVER_ERROR.value,
                "error": HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
                "message": "An unexpected error occurred.",
                "request_id": request_id,
            }

            if self.include_exception_details:
                response_content["detail"] = str(exc)

            response = JSONResponse(
                content=response_content,
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            )

            await response(scope, receive, send)

## code tests\test_exception_handler_middleware.py

"""Tests for unhandled exception middleware."""

import logging

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from full_stack_ai_shared.middleware.exception_handler import (
    ExceptionHandlerMiddleware,
)


def create_test_app(
    *,
    include_exception_details: bool = False,
) -> FastAPI:
    """Create an application configured with exception middleware."""
    app = FastAPI()
    app.add_middleware(
        ExceptionHandlerMiddleware,
        include_exception_details=include_exception_details,
    )

    @app.get("/success")
    async def success() -> dict[str, str]:
        return {"status": "healthy"}

    @app.get("/failure")
    async def failure() -> None:
        raise RuntimeError("Database connection failed.")

    return app


def test_exception_middleware_preserves_successful_response() -> None:
    """Middleware should preserve successful application responses."""
    client = TestClient(create_test_app())

    response = client.get("/success")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_exception_middleware_returns_internal_server_error() -> None:
    """Middleware should convert exceptions into JSON responses."""
    client = TestClient(create_test_app(), raise_server_exceptions=False)

    response = client.get("/failure")

    assert response.status_code == 500
    assert response.json()["status_code"] == 500
    assert response.json()["error"] == "Internal Server Error"
    assert response.json()["message"] == "An unexpected error occurred."


def test_exception_middleware_hides_exception_details_by_default() -> None:
    """Middleware should not expose internal exception details by default."""
    client = TestClient(create_test_app(), raise_server_exceptions=False)

    response = client.get("/failure")

    assert "detail" not in response.json()
    assert "Database connection failed." not in response.text


def test_exception_middleware_can_include_exception_details() -> None:
    """Middleware should expose details only when explicitly configured."""
    client = TestClient(
        create_test_app(include_exception_details=True),
        raise_server_exceptions=False,
    )

    response = client.get("/failure")

    assert response.status_code == 500
    assert response.json()["detail"] == "Database connection failed."


def test_exception_middleware_logs_unhandled_exception(
    caplog: pytest.LogCaptureFixture,
) -> None:
    """Middleware should log unhandled application exceptions."""
    client = TestClient(create_test_app(), raise_server_exceptions=False)

    with caplog.at_level(logging.ERROR):
        response = client.get("/failure")

    assert response.status_code == 500
    assert "Unhandled HTTP application exception" in caplog.text
    assert "Database connection failed." in caplog.text



























