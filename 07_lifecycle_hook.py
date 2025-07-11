"""
07_lifecycle_hook.py

Author: Ayyappa Dasam

This script demonstrates how to use lifecycle hooks (callback functions) with the Oracle Generative AI Agent Development Kit (ADK).

Features:
- Shows how to register callback functions for agent lifecycle events, such as when a required action is fulfilled or a remote service is invoked.
- Integrates custom logging or processing logic into the agent's workflow using these hooks.
- Uses the prebuilt CalculatorToolkit as a tool for the agent.

Usage:
- Update agent endpoint OCID, profile, and region as needed (or replace with environment variables for production).
- Implement your custom logic in the callback functions as required.
- Run this script to see lifecycle hooks in action during agent execution.
"""

import json

from rich.console import Console

from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.tool.prebuilt import CalculatorToolkit
from oci.addons.adk.run.types import RequiredAction, PerformedAction

# A callback function that is called when a required action is fulfilled
def handle_fulfilled_required_action(required_action: RequiredAction, performed_action: PerformedAction):
    # Implement your custom logging or processing here
    # Access the required action and performed action objects to get the details
    pass

# A callback function that is called when a remote service is invoked
def handle_invoked_remote_service(chat_request, chat_response):
    # Implement your custom logging or processing here
    # Access the chat request and response objects to get the details
    pass

def main():
    # Create an AgentClient for communicating with OCI Generative AI Agents service
    client = AgentClient(
        auth_type="api_key",
        profile="DEFAULT",
        region="us-chicago-1"
    )

    # Create the agent with the CalculatorToolkit tool
    agent = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint...",
        instructions="You're a helpful assistant that can perform calculations.",
        tools=[CalculatorToolkit()]
    )

    # Sync local instructions and tools to the remote agent resource
    agent.setup()

    input = "What's the square root of 475695037565?"
    response = agent.run(
        input,
        max_steps=6,
        on_fulfilled_required_action=handle_fulfilled_required_action,
        on_invoked_remote_service=handle_invoked_remote_service,
    )

    response.pretty_print()

if __name__ == "__main__":
    main()