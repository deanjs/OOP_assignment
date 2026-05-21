from abc import ABC, abstractmethod

class BaseTool(ABC):
    """Abstract base class for all tools"""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def run(self, query: str) -> str:
        """Execute the toolwith the given query"""
        pass

    def __repr__(self):
        return f"Tool(name={self.name!r})"