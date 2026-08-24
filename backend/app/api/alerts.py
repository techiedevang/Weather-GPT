from fastapi import APIRouter, BackgroundTasks, HTTPException
from app.api.websocket import alert_manager
from pydantic import BaseModel
import uuid

router = APIRouter()

class AlertPayload(BaseModel):
    title: str
    severity: str
    description: str
    recommended_action: str

@router.post("/trigger")
async def trigger_manual_alert(payload: AlertPayload, background_tasks: BackgroundTasks):
    """
    For Hackathon Demo: Manually triggers a high-priority alert that is 
    broadcast via WebSockets to all connected clients immediately.
    """
    alert_data = {
        "alert_id": str(uuid.uuid4()),
        "title": payload.title,
        "severity": payload.severity.upper(),
        "description": payload.description,
        "recommended_action": payload.recommended_action,
        "timestamp": "Just Now",
        "type": "PROACTIVE_WARNING"
    }
    
    # Broadcast in the background
    background_tasks.add_task(alert_manager.broadcast_alert, alert_data)
    
    return {"status": "success", "message": "Alert triggered and broadcasting to clients.", "alert": alert_data}
