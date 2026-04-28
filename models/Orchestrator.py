
# ---- Orchestrator ----
from typing import List

from models.agent import Agent, AgentState


class MultiAgentOrchestrator:
    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def run(self, user_request: str) -> AgentState:
        state = AgentState(user_request=user_request)

        for agent in self.agents:
            try:
                state = agent.run(state)
            except Exception as exc:
                state.messages.append(f"{agent.name} failed: {exc}")
                raise

        return state