from fastapi import FastAPI
from datetime import datetime
import socket
import logging

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
        "message": "AI Powered DevOps Platform Running",
        "hostname": hostname,
        "timestamp": datetime.utcnow()
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "app",
        "time": datetime.utcnow()
    }
