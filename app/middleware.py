import logging
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("middleware")

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logger.info(f"Incoming request: {request.method} {request.url.path}")
        
        response = await call_next(request)
        
        logger.info(f"Response status: {response.status_code}")
        return response
