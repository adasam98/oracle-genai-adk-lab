"""
08_delete_sessions.py

Author: Ayyappa Dasam

This script demonstrates how to explicitly delete an agent session using the Oracle Generative AI Agent Development Kit (ADK).

Features:
- Shows how to create an agent, run a session, and then explicitly delete the session using the session_id.
- Useful for cleaning up resources and managing session lifecycle in production environments.

Usage:
- Update agent endpoint OCID, profile, and region as needed (or replace with environment variables for production).
- Run this script to see how to delete an agent session after use.
"""

def main():

    agent = Agent(
        client=client,
        agent_endpoint_id="ocid1.genaiagentendpoint...",
        instructions="You are a helpful assistant that can perform calculations.",
        tools=[CalculatorToolkit()]
    )

    agent.setup()

    input = "What is the square root of 81?"
    response = agent.run(input)

    # You explicitly delete the session used by the last run
    agent.delete_session(response.session_id)

if __name__ == "__main__":
    main()