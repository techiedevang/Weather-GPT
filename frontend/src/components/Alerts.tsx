"use client";

import { useEffect, useState } from "react";

interface Alert {
  title: string;
  description: string;
  severity: string;
  location: string;
  timestamp: string;
}

export default function Alerts() {
  const [alerts, setAlerts] = useState<Alert[]>([]);

  useEffect(() => {
    // Fetch initial alerts
    fetch("http://localhost:8000/api/v1/alerts")
      .then((res) => res.json())
      .then((data) => setAlerts(data))
      .catch((err) => console.error("Failed to fetch alerts", err));

    // Listen to WebSocket for real-time alerts
    const ws = new WebSocket("ws://localhost:8000/api/v1/ws/alerts");
    
    ws.onmessage = (event) => {
      const newAlert = JSON.parse(event.data);
      setAlerts((prev) => [newAlert, ...prev]);
    };

    return () => {
      ws.close();
    };
  }, []);

  return (
    <div className="bg-white/80 backdrop-blur-md border border-red-200/50 rounded-2xl overflow-hidden shadow-xl">
      <div className="bg-gradient-to-r from-red-600 to-rose-500 text-white p-4 font-bold flex justify-between items-center shadow-sm">
        <span>Live Alert Center</span>
        <span className="text-xs bg-white/20 px-3 py-1 rounded-full animate-pulse shadow-inner">Live Stream</span>
      </div>
      <div className="p-4 max-h-[400px] overflow-y-auto space-y-3">
        {alerts.length === 0 ? (
          <p className="text-slate-500 text-center py-8 font-medium">No active extreme weather alerts.</p>
        ) : (
          alerts.map((alert, i) => (
            <div key={i} className="border-l-4 border-red-500 bg-white p-4 rounded-r-xl shadow-sm">
              <h3 className="font-bold text-red-700">{alert.title}</h3>
              <p className="text-sm text-slate-600 mt-1">{alert.description}</p>
              <div className="mt-3 flex gap-2 text-xs text-slate-500">
                <span className="font-bold bg-red-100 text-red-800 px-2 py-1 rounded-md">{alert.severity}</span>
                <span className="bg-slate-100 px-2 py-1 rounded-md">📍 {alert.location}</span>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
