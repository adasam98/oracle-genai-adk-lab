"""
sample.py

Author: Ayyappa Dasam

This script demonstrates how to test connectivity and basic interaction between a local machine and Oracle Cloud Infrastructure (OCI) Generative AI Services using the Python OCI SDK and API key authentication.

Usage:
- Ensure you have a valid OCI config file with API key credentials.
- Update the compartment OCID and config profile as needed.
- Run this script to send a sample prompt to the OCI Generative AI endpoint and print the model's response.

Purpose:
- Validate network and authentication setup from your local environment to OCI Generative AI.
- Confirm that the OCI Generative AI Python SDK is working as expected.
- Useful for initial connectivity and API testing before building more advanced integrations.
"""

import os
import oci
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

# OCI authentication and compartment setup
compartment_id = os.getenv("OCI_COMPARTMENT_ID")
CONFIG_PROFILE = os.getenv("OCI_CONFIG_PROFILE", "DEFAULT")
OCI_CONFIG_PATH = os.getenv("OCI_CONFIG_PATH", os.path.join(os.path.dirname(__file__), ".oci", "config"))
MODEL_ID = os.getenv("MODEL_ID", "ocid1.generativeaimodel.oc1.us-chicago-1.amaaaaaask7dceyanrlpnq5ybfu5hnzarg7jomak3q6kyhkzjsl4qj24fyoq")
ENDPOINT = os.getenv("OCI_GENAI_ENDPOINT", "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com")

config = oci.config.from_file(
    OCI_CONFIG_PATH,
    CONFIG_PROFILE
)

# Initialize Generative AI client
generative_ai_inference_client = oci.generative_ai_inference.GenerativeAiInferenceClient(
    config=config,
    service_endpoint=ENDPOINT,
    retry_strategy=oci.retry.NoneRetryStrategy(),
    timeout=(10, 240)
)

# Prepare chat request
chat_detail = oci.generative_ai_inference.models.ChatDetails()
chat_request = oci.generative_ai_inference.models.CohereChatRequest()
chat_request.message = os.getenv("PROMPT", "what is oracle cloud in 1 line")
chat_request.max_tokens = int(os.getenv("MAX_TOKENS", 600))
chat_request.temperature = float(os.getenv("TEMPERATURE", 0))
chat_request.frequency_penalty = float(os.getenv("FREQUENCY_PENALTY", 1))
chat_request.top_p = float(os.getenv("TOP_P", 0.75))
chat_request.top_k = int(os.getenv("TOP_K", 0))

# Specify model and compartment
chat_detail.serving_mode = oci.generative_ai_inference.models.OnDemandServingMode(
    model_id=MODEL_ID
)
chat_detail.chat_request = chat_request
chat_detail.compartment_id = compartment_id

# Send chat request and print response
chat_response = generative_ai_inference_client.chat(chat_detail)

print("**************************Chat Result**************************")
try:
    print("Text:", chat_response.data.chat_response.text)
    print("Finish Reason:", chat_response.data.chat_response.finish_reason)
    print("Total Tokens Used:", chat_response.data.chat_response.usage.total_tokens)
except Exception as e:
    print("Error extracting chat result:", e)
    print("Raw data:", chat_response.data)
