import uuid
from typing import Dict, Any

from persistence.export.export_writer import ExportWriter
from agents.agent_loader import AgentLoader


class Orchestrator:
    def __init__(self, seed: int = 0) -> None:
        self.loader = AgentLoader(seed=seed)

    def run(self, input_payload: Dict[str, Any]) -> Dict[str, Any]:
        manifestations = []

        # Green: stabilizing / intake
        green = self.loader.get("green")
        green.ingest(
            {
                "surface": input_payload.get("surface"),
                "ordering": 1,
            }
        )
        green.process()
        green_out = green.emit()
        manifestations.append(green_out["manifest"])

        # Red: adversarial / probing
        red = self.loader.get("red")
        red.ingest(
            {
                "target": input_payload.get("target"),
                "ordering": 2,
            }
        )
        red.process()
        red_out = red.emit()
        manifestations.append(red_out["manifest"])

        # Blue: observability / governance
        blue = self.loader.get("blue")
        blue.ingest(
            {
                "vectors": red_out["event"].get("vectors"),
                "ordering": 3,
            }
        )
        blue.process()
        blue_out = blue.emit()
        manifestations.append(blue_out["manifest"])

        # Build event objects for export
        event_objs = [
            green_out["event"],
            red_out["event"],
            blue_out["event"],
        ]

        # Generate run and session IDs
        run_id = str(uuid.uuid4())
        session_id = input_payload.get("session_id", "default")

        # Write export bundle
        export_path = f"exports/{run_id}"
        writer = ExportWriter(export_dir=export_path)
        writer.write_state_snapshot({"final_state": "ok"})
        writer.write_event_stream(event_objs)
        writer.write_manifest(run_id, session_id, event_objs)

        return {
            "sequence": {
                "green": green_out["event"],
                "red": red_out["event"],
                "blue": blue_out["event"],
            },
            "manifestations": manifestations,
            "export_path": export_path,
        }
