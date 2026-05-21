# custom exceptions
class AgentException(Exception):
    """Base exception for all agent-related errors"""
    def __init__(self, agent_name: str, message: str):
        self.agent_name = agent_name
        super().__init__(f"[{agent_name}] {message}")

class ToolException(Exception):
    """Base exception for all tool-related errors"""
    def __init__(self, tool_name: str, message: str):
        self.tool_name = tool_name
        super().__init__(f"[{tool_name}] {message}")