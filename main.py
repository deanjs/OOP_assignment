from dotenv import load_dotenv
from agents.research_agent import ResearchAgent
from agents.critic_agent import CriticAgent
from agents.summary_agent import SummarizerAgent
from core.orchestrator import Orchestrator

load_dotenv()

def main():
    # Initialize agents
    researcher = ResearchAgent(
        name="ResearchAgent",
        topic="multi-agent LLM systems"
    )
    critic = CriticAgent(name="CriticAgent")
    summarizer = SummarizerAgent(name="SummarizerAgent")

    # Initialize orchestrator
    orchestrator = Orchestrator(
        agents=[researcher, critic, summarizer],
        rounds=3
    )

    # Run conversation
    orchestrator.run()

    # Print full history
    print("\n--- Full History ---")
    for message in orchestrator.get_history():
        print(message)

if __name__ == "__main__":
    main()