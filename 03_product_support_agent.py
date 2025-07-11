"""
03_product_support_agent.py - Agent with Multiple Tools

This script demonstrates how to build a customer support agent using the Oracle Generative AI Agent Development Kit (ADK) with multiple tools

Features:
- Loads OCI credentials, agent endpoint OCID, and knowledge base OCID from environment variables (.env file).
- Registers multiple tools with the agent:
    - AgenticRagTool: Enables the agent to answer product questions using a knowledge base (RAG).
    - AccountToolkit: Custom function tool to fetch user and organization information.
- Sets up the agent with instructions and tools, and syncs them to the remote agent endpoint.
- Demonstrates a multi-turn conversation, including context passing and session management.

Usage:
1. Set up your `.env` file with the following variables:
    OCI_AI_AGENT_ENDPOINT_ID=<your_agent_endpoint_ocid>
    OCI_AI_KNOWLEDGE_BASE_ID=<your_knowledge_base_ocid>
    OCI_CONFIG_PROFILE=DEFAULT
    OCI_REGION=us-chicago-1
2. Ensure `custom_function_tools.py` is present and defines `AccountToolkit`.
3. Run this script to test agent setup and multi-tool invocation.

"""

from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.tool.prebuilt import AgenticRagTool
from custom_function_tools import AccountToolkit
from dotenv import load_dotenv
import os

def main():
    # Load environment variables from .env file
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

    # Fetch values from environment variables
    agent_endpoint_id = os.getenv("OCI_AI_AGENT_ENDPOINT_ID")
    knowledge_base_id = os.getenv("OCI_AI_KNOWLEDGE_BASE_ID")
    profile = os.getenv("OCI_CONFIG_PROFILE", "DEFAULT")
    region = os.getenv("OCI_REGION", "us-chicago-1")

    client = AgentClient(
        auth_type="api_key",
        profile=profile,
        region=region
    )

    instructions = """
    You are customer support agent.
    Use RAG tool to answer product questions.
    Use function tools to fetch user and org info by id.
    Only orgs of Enterprise plan can use Responses API.
    """

    agent = Agent(
        client=client,
        agent_endpoint_id=agent_endpoint_id,
        instructions=instructions,
        tools=[
            AgenticRagTool(knowledge_base_ids=[knowledge_base_id]),
            AccountToolkit()
        ]
    )

    agent.setup()

    # This is a context your existing code is best at producing (e.g., fetching the authenticated user id)
    client_provided_context = "[Context: The logged in user ID is: user_123] "

    # Handle the first user turn of the conversation
    input = "Tell me about Oracle Cloud?"
    input = client_provided_context + " " + input
    response = agent.run(input)
    response.pretty_print()

    # Handle the second user turn of the conversation
    input = "Is my user account eligible for the Responses API?"
    input = client_provided_context + " " + input
    response = agent.run(input, session_id=response.session_id)
    response.pretty_print()


if __name__ == "__main__":
    main()