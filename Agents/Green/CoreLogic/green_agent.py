from typing import Dict, Any

class GreenAgent:
    def __init__(self, seed: int = 0):
        self.state = {}
        self.input_event = None
        self.output_event = None
        self.seed = seed

    def ingest(self, input_event: Dict[str, Any]) -> None:
        self.input_event = input_event
        self.state["ingest_ok"] = True

    def process(self) -> None:
        # Deterministic baseline sensing
        surface = self.input_event.get("surface", {})
        metrics = {
            "config_valid": bool(surface),
            "exposed_services": surface.get("services", []),
            "risk_floor": len(surface.get("services", []))
        }
        self.output_event = {
            "agent": "green",
            "metrics": metrics,
            "status": "completed"
        }

    def emit(self) -> Dict[str, Any]:
        return {
            "manifest": {
                "agent": "green",
                "state_hash": hash(str(self.output_event)),
                "ordering": self.input_event.get("ordering", 0)
            },
            "event": self.output_event
        }
