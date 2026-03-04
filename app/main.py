from fastapi import FastAPI, Response
from datetime import datetime
import socket
import logging
import os
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
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
    REQUEST_COUNT.inc()

    with REQUEST_LATENCY.time():
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

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total HTTP requests"
)

REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Latency of HTTP requests"
)