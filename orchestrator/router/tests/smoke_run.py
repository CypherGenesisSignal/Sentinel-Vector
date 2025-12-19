from orchestrator_router import Orchestrator
from test_vectors import TEST_INPUT, EXPECTED_ORDERING

def smoke_run():
    orch = Orchestrator(seed=0)
    output = orch.run(TEST_INPUT)
    order = [m["ordering"] for m in output["manifestations"]]
    assert order == EXPECTED_ORDERING
    signature = hash(str(output))
    print("Smoke run OK. Signature:", signature)

if __name__ == "__main__":
    smoke_run()
