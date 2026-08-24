from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import Routers
from app.api.chat import router as chat_router
from app.api.alerts import router as alerts_router
from app.api.ws_endpoints import router as ws_router

app = FastAPI(
    title="WeatherGPT Production Engine",
    description="Evidence-validated, uncertainty-aware weather intelligence platform.",
    version="2.0.0"
)

# Configure CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "*"], # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(chat_router, prefix="/api/chat", tags=["Chat & Intelligence"])
app.include_router(alerts_router, prefix="/api/alerts", tags=["Alerts"])
app.include_router(ws_router, tags=["WebSockets"])

@app.get("/")
def read_root():
    return {"status": "online", "message": "WeatherGPT Intelligence Engine v2 is running."}
