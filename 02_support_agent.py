"""
02_support_agent.py - Agent with RAG Tool

This script demonstrates how to use the Oracle Generative AI Agent Development Kit (ADK) to build a support agent that leverages Retrieval-Augmented Generation (RAG) with a knowledge base.
It integrating a prebuilt RAG tool with an agent endpoint.

Features:
- Loads OCI credentials, agent endpoint OCID, and knowledge base OCID from environment variables (.env file).
- Registers the AgenticRagTool, which enables the agent to answer questions using the specified knowledge base.
- Sets up the agent with instructions and the RAG tool, and syncs them to the remote agent endpoint.
- Runs the agent with a sample user input and prints the response.

Usage:
1. Set up your `.env` file with the following variables:
    OCI_AI_AGENT_ENDPOINT_ID=<your_agent_endpoint_ocid>
    OCI_AI_KNOWLEDGE_BASE_ID=<your_knowledge_base_ocid>
    OCI_CONFIG_PROFILE=DEFAULT
    OCI_REGION=us-chicago-1
2. Run this script to test agent setup and RAG tool invocation.

"""

from oci.addons.adk import Agent, AgentClient
from oci.addons.adk.tool.prebuilt import AgenticRagTool
from dotenv import load_dotenv
import os


def main():
    # Load environment variables
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
    # Initialize environment variables
    OCI_AI_AGENT_ENDPOINT_ID = os.getenv("OCI_AI_AGENT_ENDPOINT_ID")
    OCI_CONFIG_PROFILE = os.getenv("OCI_CONFIG_PROFILE", "DEFAULT")
    OCI_REGION = os.getenv("OCI_REGION", "us-chicago-1")

    client = AgentClient(
        auth_type="api_key",
        profile=OCI_CONFIG_PROFILE,
        region=OCI_REGION
    )

    # Assuming the knowledge base is already provisioned
    knowledge_base_id = os.getenv("OCI_AI_KNOWLEDGE_BASE_ID")

    # Create a RAG tool that uses the knowledge base
    # The tool name and description are optional, but strongly recommended for LLM to understand the tool.
    rag_tool = AgenticRagTool(
        name="OCI RAG tool",
        description="If question is related to OCI - Use this tool to answer questions about Oracle Cloud Infrastructure (OCI).",
        knowledge_base_ids=[knowledge_base_id],
    )

    # Create the agent with the RAG tool
    agent = Agent(
        client=client,
        agent_endpoint_id=OCI_AI_AGENT_ENDPOINT_ID,
        instructions="Answer question using the OCI RAG tool.",
        tools=[rag_tool]
    )

    # Set up the agent once
    agent.setup()

    # Run the agent with a user query
    input = "Tell me about Oracle Cloud Infrastructure."
    response = agent.run(input)
    response.pretty_print()


if __name__ == "__main__":
    main()