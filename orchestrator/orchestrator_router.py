from typing import Dict, Any
import uuid
from datetime import datetime

from agents.agent_loader import AgentLoader
from persistence.export.export_writer import ExportWriter
from persistence.export.hashing import sha256_obj


class Orchestrator:
    def __init__(self, seed: int = 0):
        self.loader = AgentLoader(seed=seed)

    def run(self, input_payload: Dict[str, Any]) -> Dict[str, Any]:
        manifestations = []

        # Green
        green = self.loader.get("green")
        green.ingest({"surface": input_payload.get("surface"), "ordering": 1})
        green.process()
        green_out = green.emit()
        manifestations.append(green_out["manifest"])

        # Red
        red = self.loader.get("red")
        red.ingest({"target": input_payload.get("target"), "ordering": 2})
        red.process()
        red_out = red.emit()
        manifestations.append(red_out["manifest"])

        # Blue
        blue = self.loader.get("blue")
        blue.ingest({"vectors": red_out["event"].get("vectors"), "ordering": 3})
        blue.process()
        blue_out = blue.emit()
        manifestations.append(blue_out["manifest"])

        # Build enriched event objects
        session_id = input_payload.get("session_id", "default")

        event_objs = []
        base_events = [
            ("green", green_out["event"]),
            ("red", red_out["event"]),
            ("blue", blue_out["event"])
        ]

        for seq, (agent_name, payload) in enumerate(base_events, start=1):
            enriched = {
                "agent": agent_name,
                "seq": seq,
                "ts": datetime.utcnow().isoformat() + "Z",
                "session_id": session_id,
                **payload
            }
            event_objs.append(enriched)

        # Apply prev_hash and event_hash
        prev_hash = "genesis"
        for event in event_objs:
            event["prev_hash"] = prev_hash
            event_hash = sha256_obj({k: v for k, v in event.items() if k != "event_hash"})
            event["event_hash"] = event_hash
            prev_hash = event_hash

        # Final state snapshot
        final_state = {
            "run_complete": True,
            "agent_order": ["green", "red", "blue"],
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "summary": {
                "green_metrics": green_out["event"],
                "red_vectors": red_out["event"],
                "blue_plan": blue_out["event"]
            }
        }

        # IDs for export
        run_id = str(uuid.uuid4())

        # Write export bundle
        writer = ExportWriter(export_dir=f"exports/{run_id}")
        writer.write_state_snapshot(final_state)
        writer.write_event_stream(event_objs)
        writer.write_manifest(run_id, session_id, event_objs)

        # Return structured output
        return {
            "sequence": {
                "green": green_out["event"],
                "red": red_out["event"],
                "blue": blue_out["event"]
            },
            "manifestations": manifestations,
            "export_path": f"exports/{run_id}",
            "run_id": run_id,
            "session_id": session_id
        }
