from fastapi import WebSocket
from typing import List
import json

class AlertConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast_alert(self, alert_data: dict):
        """
        Broadcasts an official warning to all connected dashboards.
        """
        message = json.dumps(alert_data)
        for connection in self.active_connections:
            await connection.send_text(message)

# Global singleton for the alerts manager
alert_manager = AlertConnectionManager()
