
# ---- Orchestrator ----
from typing import List

from models.agent import Agent, AgentState


def run_pipeline(state: AgentState, agents: List[Agent]) -> AgentState:
    for agent in agents:
        print(f"Running: {agent.name}")
        state = agent.run(state)
    return state