"""Exceptions raised by the shared AI tool framework."""


class ToolError(Exception):
    """Base exception for tool-related errors."""


class ToolAlreadyRegisteredError(ToolError):
    """Raised when attempting to register a duplicate tool."""

    def __init__(self, tool_name: str) -> None:
        super().__init__(f"Tool '{tool_name}' is already registered")


class ToolNotFoundError(ToolError):
    """Raised when a requested tool cannot be found."""

    def __init__(self, tool_name: str) -> None:
        super().__init__(f"Tool '{tool_name}' is not registered")
