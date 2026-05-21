# OOP Assignment 2: Multi-Agent Conversation Simulator

## Description
A Multi-Agent Conversation Simulator built with Object-Oriented Programming (OOP) principles.
Three agents (ResearchAgent, CriticAgent, SummarizerAgent) collaborate through conversations
using the HuggingFace Inference API.

## Project Structure
multi_agent/
├── core/          # Message, Memory, Orchestrator
├── agents/        # BaseAgent, ResearchAgent, CriticAgent, SummarizerAgent
├── tools/         # BaseTool, RAGTool
├── exceptions.py  # Custom exceptions
└── main.py        # Entry point

## How to Run
pip install requests python-dotenv huggingface_hub

Create .env file:
HF_TOKEN=your_huggingface_token

python3 main.py
