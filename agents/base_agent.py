from abc import ABC, abstractmethod
from core.message import Message
from core.memory import Memory

class BaseAgent(ABC):
    """Abstract base class for all agents"""

    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.memory = Memory(name)

    @abstractmethod
    def respond(self, history: list[Message]) -> Message:
        """Generate a response given the conversation history"""
        pass

    def remember(self, message: Message) -> None:
        self.memory.add(message)

    def __repr__(self):
        return f"Agent(name={self.name!r}, role={self.role!r})"
        