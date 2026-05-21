from agents.base_agent import BaseAgent
from core.message import Message
from exceptions import AgentException


class Orchestrator:
    """Manages the conversation flow between agents."""

    def __init__(self, agents: list[BaseAgent], rounds: int = 3):
        self.agents = agents
        self.rounds = rounds
        self.history: list[Message] = []

    def run(self) -> None:
        print("=" * 50)
        print("Multi-Agent Conversation Start")
        print("=" * 50)

        for round_num in range(1, self.rounds + 1):
            print(f"\n--- Round {round_num} ---")
            for agent in self.agents:
                try:
                    message = agent.respond(self.history)
                    self.history.append(message)
                    print(message)
                except AgentException as e:
                    print(f"Error: {e}")

        print("\n" + "=" * 50)
        print("Multi-Agent Conversation End")
        print("=" * 50)

    def get_history(self) -> list[Message]:
        return self.history

    def reset(self) -> None:
        self.history.clear()
        print("Conversation history cleared.")