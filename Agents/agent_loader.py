from agents.red.CoreLogic.red_agent import RedAgent
from agents.green.CoreLogic.green_agent import GreenAgent
from agents.blue.CoreLogic.blue_agent import BlueAgent

class AgentLoader:
    def __init__(self, seed: int = 0):
        self.seed = seed
        self.registry = {
            "red": RedAgent(seed=self.seed),
            "green": GreenAgent(seed=self.seed),
            "blue": BlueAgent(seed=self.seed)
        }

    def get(self, agent_name: str):
        return self.registry.get(agent_name)

    def all_agents(self):
        return list(self.registry.values())
