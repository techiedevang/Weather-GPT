from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Alert(BaseModel):
    id: Optional[str] = None
    title: str
    description: str
    severity: str # Low, Moderate, High, Critical
    location: str
    timestamp: datetime = datetime.now()
