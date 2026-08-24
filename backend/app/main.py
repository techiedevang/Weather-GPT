from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import get_db, get_redis
from app.utils.logging import logger
from app.api.chat import router as chat_router
from app.api.alerts import router as alerts_router
from app.api.ws_endpoints import router as ws_router

app = FastAPI(
    title="WeatherGPT Production Engine",
    description="Evidence-validated, uncertainty-aware weather intelligence platform.",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handling middleware
@app.middleware("http")
async def add_process_time_header_and_log(request: Request, call_next):
    start_time = time.time()
    try:
        response = await call_next(request)
    except Exception as e:
        logger.error(f"Unhandled Exception: {str(e)}", exc_info=True)
        return JSONResponse(status_code=500, content={"status": "error", "message": "Internal Server Error"})
    
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"{request.method} {request.url.path} - Status: {response.status_code} - Time: {process_time:.4f}s")
    return response

# Standard Production Health Probes
@app.get("/health", tags=["Monitoring"])
async def health_check():
    return {"status": "ok"}

@app.get("/liveness", tags=["Monitoring"])
async def liveness_check():
    return {"status": "alive"}

@app.get("/readiness", tags=["Monitoring"])
async def readiness_check(db: AsyncSession = Depends(get_db), redis_client = Depends(get_redis)):
    """Checks if external dependencies (DB, Redis) are reachable."""
    status = {"db": "down", "redis": "down"}
    http_status = 503
    
    try:
        await db.execute(text("SELECT 1"))
        status["db"] = "up"
    except Exception as e:
        logger.error(f"DB Readiness check failed: {e}")
        
    try:
        await redis_client.ping()
        status["redis"] = "up"
    except Exception as e:
        logger.error(f"Redis Readiness check failed: {e}")
        
    if status["db"] == "up" and status["redis"] == "up":
        http_status = 200
        
    return JSONResponse(status_code=http_status, content={"status": status})

# App Routers
app.include_router(chat_router, prefix="/api/chat", tags=["Chat & Intelligence"])
app.include_router(alerts_router, prefix="/api/alerts", tags=["Alerts"])
app.include_router(ws_router, tags=["WebSockets"])
