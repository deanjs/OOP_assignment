from agents.base_agent import BaseAgent
from core.message import Message
from exceptions import AgentException


class SummarizerAgent(BaseAgent):
    """Agent responsible for summarizing the conversation history."""

    def __init__(self, name: str):
        super().__init__(name=name, role="Summarizer")

    def respond(self, history: list[Message]) -> Message:
        try:
            if not history:
                content = "[Summarizer] No conversation to summarize."
            else:
                speakers = list({m.sender for m in history})
                num_messages = len(history)
                last_topic = history[-1].content[:50]
                content = (
                    f"[Summarizer] Conversation summary: "
                    f"{num_messages} messages exchanged among "
                    f"{', '.join(speakers)}. "
                    f"Latest topic: '{last_topic}...'"
                )
            message = Message(sender=self.name, content=content)
            self.remember(message)
            return message
        except Exception as e:
            raise AgentException(self.name, f"Failed to generate response: {str(e)}")