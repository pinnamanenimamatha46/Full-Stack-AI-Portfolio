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
