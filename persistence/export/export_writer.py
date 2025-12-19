import os
import json
from typing import List, Dict, Any
from datetime import datetime
from .canonical import canonical_dumps
from .hashing import sha256_obj, chain_hash

class ExportWriter:
    def __init__(self, export_dir: str):
        self.export_dir = export_dir
        os.makedirs(self.export_dir, exist_ok=True)

    def write_state_snapshot(self, state_obj: Dict[str, Any]) -> str:
        """
        Writes state_snapshot.json with deterministic hashing.
        """
        snapshot = dict(state_obj)
        snapshot["state_hash"] = sha256_obj({k: v for k, v in snapshot.items() if k != "state_hash"})

        path = os.path.join(self.export_dir, "state_snapshot.json")
        with open(path, "w", encoding="utf-8") as f:
            f.write(canonical_dumps(snapshot))

        return path

    def write_event_stream(self, events: List[Dict[str, Any]]) -> str:
        """
        Writes event_stream.jsonl with hash chaining.
        Each event gets event_hash and prev_hash fields.
        """
        if not events:
            raise ValueError("Event list empty")

        stream_path = os.path.join(self.export_dir, "event_stream.jsonl")

        prev_hash = "genesis"
        lines = []

        for event in events:
            event_obj = dict(event)
            event_obj["prev_hash"] = prev_hash
            event_hash = sha256_obj({k: v for k, v in event_obj.items() if k != "event_hash"})
            event_obj["event_hash"] = event_hash

            prev_hash = event_hash
            lines.append(event_obj)

        with open(stream_path, "w", encoding="utf-8") as f:
            for e in lines:
                f.write(canonical_dumps(e) + "\n")

        return stream_path

    def write_manifest(self, run_id: str, session_id: str, events: List[Dict[str, Any]]) -> str:
        """
        Writes manifest.json summarizing the chain.
        """
        manifest = {
            "run_id": run_id,
            "session_id": session_id,
            "event_count": len(events),
            "first_event_hash": events[0].get("event_hash"),
            "last_event_hash": events[-1].get("event_hash"),
            "ts": datetime.utcnow().isoformat() + "Z"
        }

        path = os.path.join(self.export_dir, "manifest.json")
        with open(path, "w", encoding="utf-8") as f:
            f.write(canonical_dumps(manifest))

        return path
