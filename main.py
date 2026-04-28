# ---- Usage ----
from models import (
    MultiAgentOrchestrator,
    PlannerAgent,
    ReviewerAgent,
    ShipmentContextAgent,
    WriterAgent,
)


def main():
    orchestrator = MultiAgentOrchestrator(
            agents=[
                PlannerAgent(),
                ShipmentContextAgent(),
                WriterAgent(),
                ReviewerAgent(),
            ]
        )

    result = orchestrator.run(
        "Write a customer support response for a delayed shipment."
    )

    print("Final Answer:")
    print(result.final_answer)

    print("\nExecution Trace:")
    for message in result.messages:
        print("-", message)

if __name__ == "__main__":
    main()
