from fastapi import FastAPI
from datetime import datetime
import socket
import logging
import os

# ---------------------------------------------------
# Application Initialization
# ---------------------------------------------------

app = FastAPI()

hostname = socket.gethostname()

APP_NAME = os.getenv("APP_NAME", "AI DevOps Platform")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# ---------------------------------------------------
# Logging Configuration
# ---------------------------------------------------

LOG_DIR = "/var/log/app"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(f"{LOG_DIR}/app.log"),
        logging.StreamHandler()
    ],
)

logger = logging.getLogger(__name__)

logger.info("Application starting...")
logger.info(f"Service: {APP_NAME}")
logger.info(f"Environment: {ENVIRONMENT}")
logger.info(f"Hostname: {hostname}")

# ---------------------------------------------------
# Routes
# ---------------------------------------------------

@app.get("/")
def home():
    logger.info("Home endpoint accessed")

    return {
        "message": APP_NAME,
        "environment": ENVIRONMENT,
        "hostname": hostname,
        "timestamp": datetime.utcnow()
    }


@app.get("/health")
def health_check():
    logger.info("Health check executed")

    return {
        "status": "healthy",
        "service": APP_NAME,
        "environment": ENVIRONMENT,
        "time": datetime.utcnow()
    }