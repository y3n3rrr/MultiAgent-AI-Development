from dataclasses import dataclass, field
from typing import Dict, List, Protocol

from tools.shipment_lookup_tool import ShipmentLookupTool


@dataclass
class AgentState:
    user_request: str
    context: Dict[str, str] = field(default_factory=dict)
    messages: List[str] = field(default_factory=list)
    final_answer: str | None = None


class Agent(Protocol):
    name: str

    def run(self, state: AgentState) -> AgentState:
        ...


class PlannerAgent:
    name = "planner"

    def run(self, state: AgentState) -> AgentState:
        state.messages.append(
            "Plan: 1) collect shipment context, 2) draft response, 3) review response."
        )
        return state


class ShipmentContextAgent:
    name = "shipment_context"

    def run(self, state: AgentState) -> AgentState:
        # In real life, this could call an API, database, vector store, or tool.
        state.context["shipment_status"] = "Delayed due to customs processing"
        state.context["estimated_delivery"] = "2 business days"
        state.messages.append("Shipment context collected.")
        return state


class WriterAgent:
    name = "writer"

    def run(self, state: AgentState) -> AgentState:
        status = state.context.get("shipment_status", "currently being processed")
        eta = state.context.get("estimated_delivery", "soon")

        draft = (
            "We apologize for the delay with your shipment. "
            f"The current status is: {status}. "
            f"The estimated delivery time is {eta}. "
            "Thank you for your patience."
        )

        state.context["draft_response"] = draft
        state.messages.append("Draft response created.")
        return state


class ReviewerAgent:
    name = "reviewer"

    def run(self, state: AgentState) -> AgentState:
        draft = state.context.get("draft_response", "")

        if "apologize" not in draft.lower():
            draft = "We apologize for the inconvenience. " + draft

        if len(draft) > 500:
            draft = draft[:500]

        state.final_answer = draft
        state.messages.append("Draft reviewed and finalized.")
        return state
    
class ToolBasedContextAgent:
    name = "tool_based_context"

    def __init__(self, shipment_tool: ShipmentLookupTool):
        self.shipment_tool = shipment_tool

    def run(self, state: AgentState) -> AgentState:
        result = self.shipment_tool.run({"tracking_id": "ABC123"})

        state.context["shipment_status"] = result["status"]
        state.context["delay_reason"] = result["reason"]
        state.context["estimated_delivery"] = result["eta"]

        state.messages.append("Shipment context retrieved using tool.")
        return state