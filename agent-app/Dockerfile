FROM python:3.11-slim

# Install system dependencies for PDF processing, document parsing, and security tools
# Added dos2unix to handle line-ending conversions automatically
RUN apt-get update && apt-get install -y \
    build-essential \
    libmagic-dev \
    gcc \
    dos2unix \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file first to leverage Docker layer caching
COPY requirements.txt .

# Install Python dependencies
# Includes support for PDF, Excel, YAML, Docx, and Webhooks
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire agent-app directory contents into /app
COPY . .

# --- AUTOMATED LINE ENDING CONVERSION ---
# This finds all .py files and ensures they use Linux LF line endings
# and removes dos2unix afterwards to keep the image slim.
RUN find . -type f -name "*.py" -print0 | xargs -0 dos2unix && \
    apt-get --purge remove -y dos2unix

# Create necessary persistent and safe directories
RUN mkdir -p /app/output /app/knowledge /app/.crewai

# The command is handled in docker-compose.yml to enable unbuffered logs (-u)
# and interactive TTY support for Human-in-the-Loop prompts.

