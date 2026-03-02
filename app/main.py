from fastapi import FastAPI
from datetime import datetime
import socket
import logging
import os

app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

hostname = socket.gethostname()


@app.get("/")
def home():
    logging.info("Home endpoint accessed")
    return {
        "message": os.getenv("APP_NAME"),
        "environment": os.getenv("ENVIRONMENT"),
        "hostname": hostname,
        "timestamp": datetime.utcnow()
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": os.getenv("APP_NAME"),
        "environment": os.getenv("ENVIRONMENT"),
        "time": datetime.utcnow()
    }
