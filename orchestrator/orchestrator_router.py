from typing import Dict, Any
from agents.agent_loader import AgentLoader

class Orchestrator:
    def __init__(self, seed: int = 0):
        self.loader = AgentLoader(seed=seed)

    def run(self, input_payload: Dict[str, Any]) -> Dict[str, Any]:
        manifestations = []

        green = self.loader.get("green")
        green.ingest({"surface": input_payload.get("surface"), "ordering": 1})
        green.process()
        green_out = green.emit()
        manifestations.append(green_out["manifest"])

        red = self.loader.get("red")
        red.ingest({"target": input_payload.get("target"), "ordering": 2})
        red.process()
        red_out = red.emit()
        manifestations.append(red_out["manifest"])

        blue = self.loader.get("blue")
        blue.ingest({"vectors": red_out["event"].get("vectors"), "ordering": 3})
        blue.process()
        blue_out = blue.emit()
        manifestations.append(blue_out["manifest"])

        return {
            "sequence": {
                "green": green_out["event"],
                "red": red_out["event"],
                "blue": blue_out["event"]
            },
            "manifestations": manifestations
        }
