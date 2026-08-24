from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class ChatRequest(BaseModel):
    query: str
    language: Optional[str] = "english"

class ChatResponse(BaseModel):
    response: str
    intent: str
    location: str
    time: str
    language: str
    weather_data: Optional[Dict[str, Any]] = None
