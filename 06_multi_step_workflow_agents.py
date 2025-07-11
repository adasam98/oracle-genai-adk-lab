"""
06_multi_step_workflow_agents.py

Author: Ayyappa Dasam

This script demonstrates how to build a deterministically orchestrated workflow with agentic steps using the Oracle Generative AI Agent Development Kit (ADK).

Features:
- Integrates standard Python code (e.g., fetching user preferences) with agentic steps.
- Shows how to combine non-agentic and agentic steps in a workflow.
- Uses two collaborating agents (Researcher and Writer) to process user preferences, research trending keywords, and generate a blog post.
- Demonstrates how to pass outputs from one step as inputs to the next, maintaining full control over the workflow.

Usage:
- Update agent endpoint OCIDs, profile, and region as needed (or replace with environment variables for production).
- Run this script to see a deterministic, multi-step workflow with agentic and non-agentic steps.
"""

from oci.addons.adk import Agent, AgentClient
from custom_functon_tools_v1 import ResearcherToolkit, WriterToolkit

"""
This examples shows how you can build "deterministically orchestrated workflows with agentic steps".
"""

# Your (existing) vanilla python code to be integrated into this agentic workflow
def get_user_preferences():
    # Simulate result you fetched from a DB
    return {
        "email": "your@email.com",
        "style": ["casual", "humorous"],
        "topics": ["ai"]
    }

def main():

    client = AgentClient(
        auth_type="api_key",
        profile="DEFAULT",
        region="us-chicago-1"
    )

    researcher = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint...",
        name="Researcher",
        instructions="You are a researcher. You research trending keywords based on the user preferences.",
        tools=[ResearcherToolkit()]
    )

    writer = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint...",
        name="Writer",
        instructions="You are a writer. You write a blog post based on the trending keywords and the user preferences.",
        tools=[WriterToolkit()]
    )

    researcher.setup()
    writer.setup()

    # Step 1: Fetch user preferences or any pre-processing information. (non-agentic step)
    user_preferences = get_user_preferences()

    # Step 2: Research trending keywords using outputs from the previous steps as input. (agentic step)
    topics = user_preferences['topics']
    researcher_prompt = f"Research trending keywords for the following topics: {topics}"
    last_run_response = researcher.run(researcher_prompt)

    # Step 3: Write a blog post using outputs from last two steps as input. (agentic step) 
    keywords = last_run_response.output
    style = user_preferences['style']
    email = user_preferences['email']
    writer_prompt = f"Write a 5 sentences blog post and email it to {email}. Use style: {style}. Blog post should be based on: {keywords}."
    last_run_response = writer.run(writer_prompt)

    # Step 4: Do whatever you want with the last step output. Here we just print it.
    last_run_response.pretty_print()

if __name__ == "__main__":
    main()