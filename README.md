# oracle-genai-adk-lab
A collection of practical examples and utilities for working with the OCI Gen AI Agent Development Kit (ADK). This repository demonstrates agent creation, multi-turn conversations, multi-agent orchestration, deterministic workflows, lifecycle hooks, and session management using Python. Authored by Ayyappa Dasam.

## OCI Agent Development Kit (ADK) Sample Use Cases

**Tip:** We recommend you use the ADK to develop agents, except if your use case is one of the scenarios outlined in the "when to use OCI SDK" section.

### Overview
The OCI Agent Development Kit (ADK) provides high-level APIs to build AI agents on Oracle Cloud, offering a developer experience similar to other leading agent frameworks.

With OCI ADK, you can focus on agentic logic that's custom to your business—instead of writing boilerplate code and managing integration details.

**Example:**
Instead of spending hours developing a custom function-calling agent with the OCI SDK, you can create that agent in minutes using the ADK.

### Table of Contents
1. [Agent with a Function Tool](#1-agent-with-a-function-tool)
2. [Agent with RAG Tool](#2-agent-with-rag-tool)
3. [Agent with Multiple Tools](#3-agent-with-multiple-tools)
4. [Multi-Turn Conversations](#4-multi-turn-conversations)
5. [Multi-Agent Collaboration](#5-multi-agent-collaboration)
6. [Deterministic Workflow](#6-deterministic-workflow)
7. [Lifecycle Hooks](#7-lifecycle-hooks)
8. [Delete Sessions](#8-delete-sessions)

### 1. Agent with a Function Tool
**Code file:** `01_weather_agent.py`

**Description:**
Demonstrates how to create an OCI AI Agent that leverages a serverless function as a tool. The agent can invoke custom business logic or retrieve real-time data by calling an OCI Function, enhancing the capabilities of the base LLM.

**Key Benefits:**
- Extends agent functionality to take action or pull live data.
- Seamless integration with backend systems or custom logic in a secure, scalable way.
- Common uses: retrieving inventory, generating quotes, or executing business operations on demand.

### 2. Agent with RAG Tool
**Code file:** `02_support_agent.py`

**Description:**
Showcases an agent equipped with a Retrieval-Augmented Generation (RAG) tool. The agent can search an external knowledge source (such as a vector store or database) for relevant documents and use these results to answer user queries more accurately and contextually.

**Key Benefits:**
- Grounds LLM responses in enterprise data, combating hallucinations.
- Supports knowledge-driven use cases like compliance, HR, or product support.
- Keeps agent responses current as new documents are added.

### 3. Agent with Multiple Tools
**Code file:** `03_product_support_agent.py`

**Description:**
Features an agent that can access and utilize multiple tools (e.g., a function and a RAG tool). The agent dynamically selects or sequences tools based on user intent, enabling multi-step and composite tasks.

**Key Benefits:**
- Supports complex workflows and decision-making by chaining tool executions.
- Ideal for customer service scenarios requiring various actions and information retrieval.
- Easily scalable: add more tools as business needs grow.

### 4. Multi-Turn Conversations
**Code file:** `04_calculator_multi_turns_agent.py`

**Description:**
Shows an agent capable of maintaining context across multiple conversational turns. The agent remembers previous user inputs, making the conversation flow more natural and contextually relevant.

**Key Benefits:**
- Enables realistic, context-aware chat experiences.
- Useful for troubleshooting, onboarding, or guided workflows.
- Personalizes the user journey by carrying over important information.

### 5. Multi-Agent Collaboration
**Code file:** `05_multi_agents.py`

**Description:**
Illustrates collaboration between multiple specialized agents. For example, a primary agent can route parts of a query to domain-specific agents (HR, IT, Finance, etc.), aggregate their responses, and present a unified answer.

**Key Benefits:**
- Models real-world expertise boundaries and teamwork.
- Efficiently resolves cross-domain queries or workflows.
- Modularizes development and maintenance.

### 6. Deterministic Workflow
**Code file:** `06_multi_step_workflow_agents.py`

**Description:**
Implements a deterministic, rule-based workflow where the agent strictly follows predefined steps and decision points, rather than generating freeform responses. Crucial for transactional or compliance scenarios.

**Key Benefits:**
- Ensures process consistency and traceability.
- Suitable for regulated industries and strict business processes.
- Common uses: onboarding, approvals, regulated transactions.

### 7. Lifecycle Hooks
**Code file:** `07_lifecycle_hook.py`

**Description:**
Demonstrates the use of lifecycle hooks to inject custom behavior at various agent stages—such as session start, before tool use, or before response send. Supports custom logging, telemetry, or session-based logic.

**Key Benefits:**
- Enables advanced customization for analytics, security, or user experience.
- Supports monitoring, audit, and personalization.
- Allows pre- and post-processing for more intelligent operations.

### 8. Delete Sessions
**Code file:** `08_delete_sessions.py`

**Description:**
Shows how to programmatically delete user/agent conversation sessions, supporting privacy, compliance, and data management needs.

**Key Benefits:**
- Meets GDPR and similar data protection requirements.
- Optimizes storage and cost by removing obsolete sessions.
- Empowers users and admins to control the conversation data lifecycle.
