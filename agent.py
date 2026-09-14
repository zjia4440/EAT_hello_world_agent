"""A simple two-agent Hello World demonstration."""

from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

from google.adk.agents import Agent
from sage_adk import SageLlmRegistry
from .sub_agent import answer_agent, validate_agent

sage_llm = SageLlmRegistry.get_llm("sage-gemini-2.5-flash")

root_agent = Agent(
    name="hello_world_agent",
    model=sage_llm,
    description="Answers Hello World and validates the answer.",
    instruction="""
    Always call answer_agent first.
    Then pass its result to validate_agent.
    Return both the answer and the validation result.
    """,
    tools=[answer_agent, validate_agent],
)
