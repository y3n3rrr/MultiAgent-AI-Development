from tools.tool import Tool
from utils import retry

class ShipmentLookupTool(Tool):
    name = "shipment_lookup"

    def _fetch_shipment(self, tracking_id: str | None) -> dict:
        # Mocked external API response
        return {
            "tracking_id": tracking_id,
            "status": "Delayed",
            "reason": "Customs processing",
            "eta": "2 business days",
        }

    def run(self, input_data: dict) -> dict:
        tracking_id = input_data.get("tracking_id")
        return retry(
            lambda: self._fetch_shipment(tracking_id),
            attempts=3,
            delay_seconds=0.5,
        )
