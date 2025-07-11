"""
04_calculator_multi_turns_agent.py : agent that maintain context across conversation turns

Author: Ayyappa Dasam

This script demonstrates how to build and run a multi-turn conversational agent using the Oracle Generative AI Agent Development Kit (ADK).

Features:
- Loads OCI credentials and agent endpoint OCID from environment variables (.env file).
- Registers the prebuilt CalculatorToolkit as a tool for the agent.
- Sets up the agent with instructions and tools, and syncs them to the remote agent endpoint.
- Demonstrates a multi-turn conversation, maintaining session context between turns.

Usage:
1. Set up your `.env` file with the following variables:
    OCI_AI_AGENT_ENDPOINT_ID=<your_agent_endpoint_ocid>
    OCI_CONFIG_PROFILE=DEFAULT
    OCI_REGION=us-chicago-1
2. Run this script to test multi-turn agent conversation and tool invocation.
"""

from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.tool.prebuilt import CalculatorToolkit
from dotenv import load_dotenv
import os


def main():
    # Load environment variables from .env file
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

    # Fetch values from environment variables
    agent_endpoint_id = os.getenv("OCI_AI_AGENT_ENDPOINT_ID")
    profile = os.getenv("OCI_CONFIG_PROFILE", "DEFAULT")
    region = os.getenv("OCI_REGION", "us-chicago-1")

    # Create an AgentClient for communicating with OCI Generative AI Agents service
    client = AgentClient(
        auth_type="api_key",
        profile=profile,
        region=region
    )

    # Create the agent with the CalculatorToolkit tool
    agent = Agent(
        client=client,
        agent_endpoint_id=agent_endpoint_id,
        instructions="You perform calculations using tools provided.",
        tools=[CalculatorToolkit()]
    )

    # Sync local instructions and tools to the remote agent resource
    agent.setup()

    # First turn (start a new session)
    input = "What is the square root of 256?"
    response = agent.run(input, max_steps=3)
    response.pretty_print()

    # Second turn (continue the same session using session_id)
    input = "do the same thing for 81"
    response = agent.run(input, session_id=response.session_id, max_steps=3)
    response.pretty_print()

if __name__ == "__main__":
    main()