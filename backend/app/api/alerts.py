from fastapi import APIRouter
from typing import List
from app.schemas.alerts import Alert
from app.services.alert_service import get_recent_alerts, add_alert
from app.api.websocket import trigger_alert_broadcast

router = APIRouter()

@router.get("/alerts", response_model=List[Alert])
async def fetch_alerts():
    return get_recent_alerts()

@router.post("/alerts", response_model=Alert)
async def create_alert(alert: Alert):
    # This endpoint is primarily for internal/admin use to trigger a new alert
    new_alert = add_alert(alert)
    # Broadcast to all connected WebSocket clients
    await trigger_alert_broadcast(new_alert.model_dump(mode="json"))
    return new_alert
