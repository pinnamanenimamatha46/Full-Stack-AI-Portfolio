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
