# Use an official Python base image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing pyc files and to buffer output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

# Set working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install additional system dependencies for Vosk, sounddevice, and gTTS
RUN apt-get update && apt-get install -y --no-install-recommends \
    libasound2 libportaudio2 libportaudiocpp0 portaudio19-dev ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the application code into the container
COPY . /app

# Expose necessary ports (if the agent is extended for a web API, specify the port here)
EXPOSE 5000

# Entry point to run the agent
CMD ["bash", "./scripts/run_agent.sh"]
