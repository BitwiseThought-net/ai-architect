FROM python:3.11-slim

# Install system dependencies for PDF and document processing
RUN apt-get update && apt-get install -y \
    build-essential \
    libmagic-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
# 'crewai[docling]' handles Markdown, Docx, etc.
# 'openpyxl' and 'pandas' handle Excel and CSV
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Ensure the output directory exists for safe_write tools
RUN mkdir -p /app/output /app/knowledge

# We define the command in docker-compose.yml to allow for -u (unbuffered) flags
# and to easily switch between 'main.py' and a sleeping 'tail -f' for debugging.
