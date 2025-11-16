"""
Sentinel Vector Prototype
Routing Layer
Version 0.1

Purpose:
Provides a centralized place to load and assemble all agents for the
Purple Orchestrator. Keeps the orchestrator code clean and makes it
easy to swap or modify agent configurations.
"""

from Agents.Red.red_agent import RedAgent
from Agents.Red.red_agent_b import RedAgentB

from Agents.Blue.blue_agent_a import BlueAgentA
from Agents.Blue.blue_agent_b import BlueAgentB

from Agents.Green.green_agent_a import GreenAgentA
from Agents.Green.green_agent_b import GreenAgentB


def load_all_agents():
    """
    Returns a list of instantiated agents in the correct order.
    Red, Blue, Green. Purple is not included because Purple is the
    orchestrator itself.
    """
    agents = [
        RedAgent(name="RedAgent_A"),
        RedAgentB(name="RedAgent_B"),

        BlueAgentA(name="BlueAgent_A"),
        BlueAgentB(name="BlueAgent_B"),

        GreenAgentA(name="GreenAgent_A"),
        GreenAgentB(name="GreenAgent_B"),
    ]

    return agents
