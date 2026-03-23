from fastapi import FastAPI
from app.routers import summarize_router
from app.routers.pii_router import router as pii_router
from app.logging_config import setup_logging
import logging
from app.middleware import RequestLoggingMiddleware
from app.routers.summarize_router import router as summarize_router


setup_logging()
logger = logging.getLogger("main1234")
    
app = FastAPI(title="Azure PII Detection Service")
app.add_middleware(RequestLoggingMiddleware)

logger.info("FastAPI application starting up")

app.include_router(pii_router)
app.include_router(summarize_router)

@app.get("/")
def root():
    logger.info("Root endpoint called-first endpoint")
    return {"status": "running", "service": "Azure PII Detection"}