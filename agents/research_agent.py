import os
import requests
from agents.base_agent import BaseAgent
from core.message import Message
from tools.rag_tool import RAGTool
from exceptions import AgentException


class ResearchAgent(BaseAgent):
    """Agent responsible for generating research-based responses."""

    def __init__(self, name: str, topic: str):
        super().__init__(name=name, role="Researcher")
        self.topic = topic
        self.tool = RAGTool()

    def respond(self, history: list[Message]) -> Message:
        try:
            query = f"Explain about {self.topic} in the context of multi-agent systems."
            result = self.tool.run(query)
            content = f"[Research] {result}"
            message = Message(sender=self.name, content=content)
            self.remember(message)
            return message
        except Exception as e:
            raise AgentException(self.name, f"Failed to generate response: {str(e)}")