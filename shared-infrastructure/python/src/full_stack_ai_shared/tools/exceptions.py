"""Exceptions raised by the shared AI tool framework."""


class ToolError(Exception):
    """Base exception for tool-related errors."""


class ToolAlreadyRegisteredError(ToolError):
    """Raised when attempting to register a duplicate tool."""

    def __init__(self, tool_name: str) -> None:
        """Initialize the duplicate registration error."""
        self.tool_name = tool_name
        super().__init__(f"Tool '{tool_name}' is already registered.")


class ToolNotFoundError(ToolError):
    """Raised when a requested tool is not registered."""

    def __init__(self, tool_name: str) -> None:
        """Initialize the missing tool error."""
        self.tool_name = tool_name
        super().__init__(f"Tool '{tool_name}' is not registered")


class ToolExecutionError(ToolError):
    """Raised when execution of a registered tool fails."""

    def __init__(self, tool_name: str, message: str) -> None:
        """Initialize the tool execution error."""
        self.tool_name = tool_name
        self.message = message
        super().__init__(f"Tool '{tool_name}' execution failed: {message}")
