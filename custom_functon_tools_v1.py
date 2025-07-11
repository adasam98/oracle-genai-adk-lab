from typing import Dict, List
from oci.addons.adk import tool, Toolkit

@tool
def get_trending_keywords(topic: str) -> Dict[str, List[str]]:
    """Get trending keywords for a given topic"""
    # In a real implementation, this might call an API or database.
    if topic == "ai":
        return {"topic": topic, "keywords": ["generative AI", "multi-agent systems", "LLM agents"]}
    return {"topic": topic, "keywords": ["unknown"]}

@tool
def send_email(recipient: str, subject: str, body: str) -> str:
    """Send an email with the given subject and body to the recipient"""
    # In a real implementation, this would send an actual email.
    print(f"Sending email to {recipient}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    return "Email sent successfully"

class ResearcherToolkit(Toolkit):
    """Toolkit for researching trending topics"""

    def __init__(self):
        super().__init__(name="ResearcherToolkit", description="Tools for researching trending topics")
        self.add_tool(get_trending_keywords)

class WriterToolkit(Toolkit):
    """Toolkit for writing content and sending emails"""

    def __init__(self):
        super().__init__(name="WriterToolkit", description="Tools for writing content and sending emails")
        self.add_tool(send_email)