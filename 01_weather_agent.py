"""
01_weather_agent.py - Agent with a Function Tool

This script demonstrates how to build and run a simple Oracle Generative AI Agent using the Oracle Agent Development Kit (ADK).
It follows the official Oracle example for registering a Python function as a tool and invoking it via an agent endpoint.

Features:
- Registers a Python function (`get_weather`) as a tool for the agent.
- Sets up the agent with instructions and tools, and syncs them to the remote agent endpoint.
- Runs the agent with a sample user input and prints the response.

Usage:
1. Set up your `.env` file with the following variables:
    OCI_AI_AGENT_ENDPOINT_ID=<your_agent_endpoint_ocid>
    OCI_CONFIG_PROFILE=DEFAULT
    OCI_REGION=us-chicago-1
2. Run this script to test agent setup and function tool invocation.

"""

import os
from typing import Dict
from oci.addons.adk import Agent, AgentClient, tool
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

# initialize environment variables
OCI_AI_AGENT_ENDPOINT_ID = os.getenv("OCI_AI_AGENT_ENDPOINT_ID")
OCI_CONFIG_PROFILE= os.getenv("OCI_CONFIG_PROFILE", "DEFAULT")
OCI_REGION = os.getenv("OCI_REGION", "us-chicago-1")

# Use @tool to signal that this Python function is a function tool.
# Apply standard docstring to provide function and parameter descriptions.
@tool
def get_weather(location: str) -> Dict[str, str]:
    """
    Get the weather for a given location.

    Args:
      location(str): The location for which weather is queried
    """
    return {"location": location, "temperature": 72, "unit": "F"}


def main():
    # Create an agent client with your authentication and region details
    # Replace the auth_type with your desired authentication method.
    client = AgentClient(
        auth_type="api_key",
        profile=OCI_CONFIG_PROFILE,
        region=OCI_REGION,
    )

    # Create a local agent object with the client, instructions, and tools.
    # You also need the agent endpoint id. To obtain the OCID, follow Step 1.
    agent = Agent(
        client=client,
        agent_endpoint_id=OCI_AI_AGENT_ENDPOINT_ID,
        instructions="You perform weather queries using tools.",
        tools=[get_weather]
    )

    # Sync local instructions and tools to the remote agent resource
    # You only need to invoke setup() when you change instructions and tools
    agent.setup()

    # Run the agent. You can embed this method in your webapp, slack bot, etc.
    # You invoke the run() when you need to handle your user's request.
    input = "Is it cold in Seattle?"
    response = agent.run(input)

    # Print the response
    response.pretty_print()

if __name__ == "__main__":
    main()