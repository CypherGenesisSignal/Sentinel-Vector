"""
Sentinel Vector Prototype
Purple Orchestrator Module
Version 0.1

Purpose:
Coordinates agent stubs, collects outputs, aggregates results, and writes
a structured report. This is a minimal prototype orchestrator intended for
future expansion.
"""

import os
import datetime
import hashlib


class PurpleOrchestrator:
    def __init__(self, agents=None, log_dir="logs"):
        """
        Initialize the orchestrator.

        agents: list of instantiated agent objects.
        log_dir: directory for output logs.
        """
        self.agents = agents or []
        self.log_dir = log_dir

        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def run_cycle(self):
        """
        Run a single orchestrator cycle.
        Each agent returns a dictionary of results.
        These are aggregated into a final report.
        """
        aggregated = []

        for agent in self.agents:
            try:
                result = agent.run()
                aggregated.append(result)
            except Exception as exc:
                aggregated.append({"agent": agent.__class__.__name__, "error": str(exc)})

        report_path = self._write_report(aggregated)
        sha = self._hash_file(report_path)

        return {"report": report_path, "sha256": sha}

    def _write_report(self, data):
        """
        Create a timestamped text report containing aggregated results.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"case_report_{timestamp}.txt"
        full_path = os.path.join(self.log_dir, filename)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write("Sentinel Vector Prototype Report\n")
            f.write("Purple Orchestrator\n")
            f.write("----------------------------------------------------\n")
            f.write(f"Timestamp: {timestamp}\n")
            f.write("----------------------------------------------------\n\n")
            f.write("Agent Outputs:\n\n")

            for entry in data:
                f.write(str(entry) + "\n")

        return full_path

    def _hash_file(self, path):
        """
        Compute a SHA256 hash of the generated report file.
        """
        sha256 = hashlib.sha256()

        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)

        return sha256.hexdigest()


# Example agent stub for demonstration purposes
class ExampleAgent:
    def __init__(self, name="ExampleAgent"):
        self.name = name

    def run(self):
        return {
            "agent": self.name,
            "status": "ok",
            "message": "Prototype agent execution"
        }


if __name__ == "__main__":
    orchestrator = PurpleOrchestrator(agents=[ExampleAgent()])
    result = orchestrator.run_cycle()
    print("Report:", result["report"])
    print("SHA256:", result["sha256"])
