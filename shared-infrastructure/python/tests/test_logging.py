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
