from fastapi import FastAPI
from app.routers.pii_router import router as pii_router
from app.logging_config import setup_logging
import logging
from app.middleware import RequestLoggingMiddleware

setup_logging()
logger = logging.getLogger("main123")

app = FastAPI(title="Azure PII Detection Service")
app.add_middleware(RequestLoggingMiddleware)

logger.info("FastAPI application starting up")

app.include_router(pii_router)

@app.get("/")
def root():
    logger.info("Root endpoint called-first endpoint")
    return {"status": "running", "service": "Azure PII Detection"}
