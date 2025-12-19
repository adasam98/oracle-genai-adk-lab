# Setup Instructions for OCI ADK Lab

## Prerequisites
- Python 3.8 or higher installed
- OCI account with access to AI Agents service

## Installation Steps

### 1. Create a Project Folder
```bash
mkdir oracle-genai-adk-lab
cd oracle-genai-adk-lab
```

### 2. Create and Activate Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages
```bash
pip install oci
pip install "oci[adk]"
```

### 4. Configure OCI Credentials
Ensure your OCI credentials are configured in `~/.oci/config` or via environment variables.

### 5. Run Sample Scripts
```bash
python 00_sample.py
```

## Next Steps
Refer to the README.md file for detailed examples and use cases.

