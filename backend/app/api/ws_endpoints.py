from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.api.websocket import alert_manager

router = APIRouter()

@router.websocket("/ws/alerts")
async def websocket_alerts_endpoint(websocket: WebSocket):
    await alert_manager.connect(websocket)
    try:
        while True:
            # Keep connection alive and wait for messages from client
            data = await websocket.receive_text()
            print(f"Received WebSocket message from client: {data}")
    except WebSocketDisconnect:
        alert_manager.disconnect(websocket)
