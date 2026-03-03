# Use lightweight Python base image
FROM python:3.11-slim

# Prevent python buffering
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies first (Docker cache optimization)
COPY requirements.txt .

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .

# Expose application port
EXPOSE 8000

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
CMD curl -f http://localhost:8000/health || exit 1