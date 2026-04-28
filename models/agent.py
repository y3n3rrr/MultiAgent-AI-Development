from dataclasses import dataclass, field
from typing import Dict, List, Protocol


# ---- Shared State ----
@dataclass
class AgentState:
    user_request: str
    context: Dict[str, str] = field(default_factory=dict)
    messages: List[str] = field(default_factory=list)
    final_answer: str | None = None


# ---- Agent Contract ----
class Agent(Protocol):
    name: str

    def run(self, state: AgentState) -> AgentState:
        ...


# ---- Concrete Agents ----
class PlannerAgent:
    name = "planner"

    def run(self, state: AgentState) -> AgentState:
        state.messages.append("Plan: collect context → draft → finalize")
        return state


class ShipmentContextAgent:
    name = "shipment_context"

    def run(self, state: AgentState) -> AgentState:
        # simulate external data
        state.context["shipment_status"] = "Delayed"
        state.context["eta"] = "2 days"
        state.messages.append("Context collected.")
        return state


class ResponseAgent:
    name = "responder"

    def run(self, state: AgentState) -> AgentState:
        status = state.context.get("shipment_status", "unknown")
        eta = state.context.get("eta", "unknown")

        state.final_answer = (
            f"Your shipment is {status}. Estimated delivery: {eta}."
        )
        state.messages.append("Response generated.")
        return state





