#!/bin/bash

# Specify your Conda environment name
CONDA_ENV_NAME="PyVerseAI"

# Function to check if Conda is available
function check_conda() {
  if command -v conda &> /dev/null; then
    echo "Conda detected."
    return 0
  else
    echo "Conda not found."
    return 1
  fi
}

# Function to check if a virtual environment is activated
function check_virtual_env() {
  if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "Virtual environment is not activated."
    return 1
  else
    echo "Virtual environment detected."
    return 0
  fi
}

# Check and activate the Conda environment if available
if check_conda; then
  if conda env list | grep -q "$CONDA_ENV_NAME"; then
    echo "Activating Conda environment: $CONDA_ENV_NAME"
    eval "$(conda shell.bash hook)"
    conda activate "$CONDA_ENV_NAME"
  else
    echo "Conda environment '$CONDA_ENV_NAME' does not exist."
    echo "Create it with: conda create -n $CONDA_ENV_NAME python=3.11"
    exit 1
  fi
# Check if a virtual environment is activated
elif check_virtual_env; then
  echo "Using active virtual environment."
else
  echo "No Conda environment or virtual environment detected."
  echo "Activate your environment or create one."
  exit 1
fi

# Check if .env file exists
if [[ ! -f ".env" ]]; then
  echo ".env file not found. Please create it with the necessary environment variables."
  exit 1
fi

# Export environment variables from .env file
export $(grep -v '^#' .env | xargs)

# Debugging: Print Python and environment details
echo "Python version:"
python3 --version
echo "Environment:"
env | grep -E "OPENAI_API_KEY|WHISPER_API_KEY"

# Run the agent and log the output
echo "Starting AgentX..."
python3 core/agent.py
AGENT_EXIT_CODE=$?

if [[ $AGENT_EXIT_CODE -ne 0 ]]; then
  echo "AgentX failed to start. Exit code: $AGENT_EXIT_CODE"
  exit $AGENT_EXIT_CODE
else
  echo "AgentX stopped successfully."
fi
