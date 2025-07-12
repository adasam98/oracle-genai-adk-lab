# Oracle OCI ADK Lab [AI Agents]
A collection of practical examples and utilities for working with the OCI Agent Development Kit (ADK). This repository demonstrates agent creation, funtional calling, RAG, multi-turn conversations, multi-agent orchestration, deterministic workflows, lifecycle hooks, and session management using Python. Authored by Ayyappa Dasam [inspired from Oracle official examples in https://docs.oracle.com]

## OCI Agent Development Kit (ADK) Sample Use Cases

### Overview
The OCI ADK provides high-level APIs to build AI agents on Oracle Cloud, offering a developer experience similar to other leading agent frameworks [Google ADK, LangGraph, Crew AI etc.].

With OCI ADK, you can focus on agentic logic that's custom to your business—instead of writing boilerplate code and managing integration details.
**Example:**
Instead of spending hours developing a custom function-calling agent with the OCI SDK, you can create that agent in minutes using the ADK.

### Table of Contents
1. [How OCI ADK Works High Level Overview](#1-how-oci-adk-works–high-level-overview)
2. [Agent with a Function Tool](#2-agent-with-a-function-tool)
3. [Agent with RAG Tool](#3-agent-with-rag-tool)
4. [Agent with Multiple Tools](#4-agent-with-multiple-tools)
5. [Multi-Turn Conversations](#5-multi-turn-conversations)
6. [Multi-Agent Collaboration](#6-multi-agent-collaboration)
7. [Deterministic Workflow](#7-deterministic-workflow)
8. [Lifecycle Hooks](#8-lifecycle-hooks)
9. [Delete Sessions](#9-delete-sessions)
10. [Best Practices for Using OCI ADK](#10-best-practices-for-using-oci-adk)


### 1. How OCI ADK Works High Level Overview
Typically, your ADK code is embedded within a larger application—such as a web app, Slackbot, backend service, or standalone script deployed in your own environment.

Using ADK function tools, you can tightly integrate an agent with your local codebase, remote databases, microservices, or any other system, all while leveraging your environment's native authentication.

The ADK communicates with the OCI Generative AI Agents service by calling the agent endpoint. The main agent loop runs remotely in OCI, not in your environment.

When the agent loop needs to use a hosted tool (such as a RAG tool), that call happens directly within the OCI environment—no round trip to your ADK code.

When the agent loop needs to use a local function tool, control is handed back to your ADK code. The ADK executes your local tool logic, then returns the result to the OCI Generative AI Agents service, which continues with the next step in the agent loop.

In summary:
OCI ADK allows seamless, secure integration between Oracle's cloud-based AI agent orchestration and your local business logic, data, and systems—so your agents can act both in the cloud and in your own environment, as needed.

<img alt="image" src="https://github.com/user-attachments/assets/bbf48b61-c8c7-4024-988b-c8d041e36ea0">

### 2. Agent with a Function Tool
**Code file:** `01_weather_agent.py`

**Description:**
Demonstrates how to create an OCI AI Agent that leverages a serverless function as a tool. The agent can invoke custom business logic or retrieve real-time data by calling an OCI Function, enhancing the capabilities of the base LLM.

**Key Benefits:**
- Extends agent functionality to take action or pull live data.
- Seamless integration with backend systems or custom logic in a secure, scalable way.
- Common uses: retrieving inventory, generating quotes, or executing business operations on demand.

### 3. Agent with RAG Tool
**Code file:** `02_support_agent.py`

**Description:**
Showcases an agent equipped with a Retrieval-Augmented Generation (RAG) tool. The agent can search an external knowledge source (such as a vector store or database) for relevant documents and use these results to answer user queries more accurately and contextually.

**Key Benefits:**
- Grounds LLM responses in enterprise data, combating hallucinations.
- Supports knowledge-driven use cases like compliance, HR, or product support.
- Keeps agent responses current as new documents are added.

### 4. Agent with Multiple Tools
**Code file:** `03_product_support_agent.py`

**Description:**
Features an agent that can access and utilize multiple tools (e.g., a function and a RAG tool). The agent dynamically selects or sequences tools based on user intent, enabling multi-step and composite tasks.

**Key Benefits:**
- Supports complex workflows and decision-making by chaining tool executions.
- Ideal for customer service scenarios requiring various actions and information retrieval.
- Easily scalable: add more tools as business needs grow.

### 5. Multi-Turn Conversations
[Context Memory]
**Code file:** `04_calculator_multi_turns_agent.py`

**Description:**
Shows an agent capable of maintaining context across multiple conversational turns. The agent remembers previous user inputs, making the conversation flow more natural and contextually relevant.

**Key Benefits:**
- Enables realistic, context-aware chat experiences.
- Useful for troubleshooting, onboarding, or guided workflows.
- Personalizes the user journey by carrying over important information.

### 6. Multi-Agent Collaboration
**Code file:** `05_multi_agents.py`

**Description:**
Illustrates collaboration between multiple specialized agents. For example, a primary agent can route parts of a query to domain-specific agents (HR, IT, Finance, etc.), aggregate their responses, and present a unified answer.

**Key Benefits:**
- Models real-world expertise boundaries and teamwork.
- Efficiently resolves cross-domain queries or workflows.
- Modularizes development and maintenance.

### 7. Deterministic Workflow
**Code file:** `06_multi_step_workflow_agents.py`

**Description:**
Implements a deterministic, rule-based workflow where the agent strictly follows predefined steps and decision points, rather than generating freeform responses. Crucial for transactional or compliance scenarios.

**Key Benefits:**
- Ensures process consistency and traceability.
- Suitable for regulated industries and strict business processes.
- Common uses: onboarding, approvals, regulated transactions.

### 8. Lifecycle Hooks
**Code file:** `07_lifecycle_hook.py`

**Description:**
Demonstrates the use of lifecycle hooks to inject custom behavior at various agent stages—such as session start, before tool use, or before response send. Supports custom logging, telemetry, or session-based logic.

**Key Benefits:**
- Enables advanced customization for analytics, security, or user experience.
- Supports monitoring, audit, and personalization.
- Allows pre- and post-processing for more intelligent operations.

### 9. Delete Sessions
**Code file:** `08_delete_sessions.py`

**Description:**
Shows how to programmatically delete user/agent conversation sessions, supporting privacy, compliance, and data management needs.

### 10. Best Practices for Using OCI ADK

1. **Choose the ADK for Most Agent Use Cases**
   
   Use the ADK to build agents unless your use case is one of the rare scenarios that requires the OCI SDK directly.
   
   The ADK is designed to simplify agent creation, lifecycle, tool orchestration, and session management.

2. **Design Agent Logic to be Stateless and Deterministic**
   
   Keep agents stateless within a single request/response cycle.
   
   Avoid storing transient state in global variables or instance variables within your tools.
   
   Ensure that agents produce consistent outputs given the same inputs (deterministic behavior), which is essential for debugging and auditability.

3. **Implement Custom Tools for Business Logic**
   
   When you need custom actions or access to backend systems, implement your business logic as ADK tools.
   
   Tools should be independent, reusable, and focused on a single responsibility.
   
   Use tools to call external APIs, invoke OCI Functions, or perform calculations.

4. **Isolate External Integrations**
   
   Encapsulate external dependencies and integrations (databases, APIs, cloud services) within tools, not within the agent itself.
   
   This ensures the agent remains portable and easier to test or extend.

5. **Manage Sessions Thoughtfully**
   
   Use ADK's built-in session management for multi-turn conversations or scenarios requiring context.
   
   Store only essential context in sessions; avoid persisting sensitive or unnecessary data.

6. **Secure Sensitive Data**
   
   Never log, store, or expose sensitive data (such as secrets, passwords, or PII) unless absolutely necessary.
   
   If you must handle such data, always use encryption and adhere to security best practices.

7. **Test, Monitor, and Log Responsibly**
   
   Write tests for your agents and tools to validate their logic and ensure reliability.
   
   Use monitoring and logging to track agent activity and catch errors early, but avoid logging sensitive data.
   
   Monitor for unusual activity or failures and respond appropriately.

8. **Iterate and Improve with Feedback**
   
   Continuously refine your agents by incorporating user feedback and analytics.
   
   Monitor agent responses to improve accuracy and user satisfaction.

9. **Follow Principle of Least Privilege**
   
   Grant only the permissions needed for your agents and tools to function, nothing more.
   
   Regularly review and update permissions as requirements change.

10. **Stay Current with Documentation and Updates**
   
   Review the OCI ADK documentation regularly for new features, updates, and security guidance.
