# ---- Usage ----
from typing import List

from models.Orchestrator import run_pipeline
from models.agent import Agent, AgentState, PlannerAgent, ResponseAgent, ShipmentContextAgent


def main():
    state = AgentState(user_request="Where is my shipment?")

    agents: List[Agent] = [
        PlannerAgent(),
        ShipmentContextAgent(),
        ResponseAgent(),
    ]

    final_state = run_pipeline(state, agents)

    print("\nMessages:")
    for m in final_state.messages:
        print("-", m)

    print("\nFinal Answer:")
    print(final_state.final_answer)

if __name__ == "__main__":
    main()
    