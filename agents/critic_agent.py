from agents.base_agent import BaseAgent
from core.message import Message
from exceptions import AgentException


class CriticAgent(BaseAgent):
    """Agent responsible for critically evaluating previous responses."""

    def __init__(self, name: str):
        super().__init__(name=name, role="Critic")

    def respond(self, history: list[Message]) -> Message:
        try:
            if not history:
                content = "[Critic] No previous response to evaluate."
            else:
                last = history[-1]
                content = (
                    f"[Critic] Evaluating '{last.sender}'s response: "
                    f"While the response covers the topic, "
                    f"it lacks specific examples and empirical evidence. "
                    f"Further elaboration is needed."
                )
            message = Message(sender=self.name, content=content)
            self.remember(message)
            return message
        except Exception as e:
            raise AgentException(self.name, f"Failed to generate response: {str(e)}")