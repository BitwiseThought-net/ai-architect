# Use a stable, official Python runtime baseline matching your application stack
FROM python:3.11-slim

# Enforce clean terminal telemetry streams inside container environments
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Establish the secure system isolation root
WORKDIR /app

# Install native system binary compilation utilities required for heavy python extensions
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Stage dependency manifestations into the filesystem cache layer
COPY requirements.txt .

# --- CRITICAL RESOLUTION PHASE ---
# 1. Upgrade baseline packaging ecosystem binaries
# 2. Pre-install telemetry, typing, and modern langchain layers to break version loops 
# 3. Force installation via legacy resolver and ignore system package boundaries safely
RUN pip install --no-cache-dir --upgrade pip setuptools wheel --disable-pip-version-check && \
    pip install --no-cache-dir \
        "pydantic==2.10.6" \
        "opentelemetry-api==1.25.0" \
        "opentelemetry-sdk==1.25.0" \
        "opentelemetry-semantic-conventions==0.46b0" \
        "langchain-core>=0.3.0" \
        --break-system-packages --disable-pip-version-check && \
    pip install --no-cache-dir -r requirements.txt --use-deprecated=legacy-resolver --break-system-packages --disable-pip-version-check

# Pre-provision the required persistent system directories 
RUN mkdir -p /app/output /app/knowledge /app/io /app/.crewai

# Copy the complete functional orchestration logic layer into the image context
COPY . .

# Grant execution rights to python entrypoints inside the target runtime profile
RUN chmod +x main.py

# Execute the core workflow engine bootstrapper
CMD ["python", "main.py"]
