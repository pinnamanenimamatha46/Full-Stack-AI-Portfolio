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
