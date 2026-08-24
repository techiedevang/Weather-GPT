"use client";
import { useState, useEffect } from "react";

export default function WeatherWidget() {
  const [weather, setWeather] = useState<any>(null);
  const [error, setError] = useState(false);
  
  useEffect(() => {
    // Fetch mock weather for initial load
    fetch("http://localhost:8000/api/v1/ai/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: "current weather in Noida", language: "english" })
    })
      .then(res => {
        if (!res.ok) throw new Error("Network response was not ok");
        return res.json();
      })
      .then(data => {
        if(data.weather_data) setWeather(data.weather_data);
      })
      .catch((err) => {
        console.error("Weather widget error:", err);
        setError(true);
      });
  }, []);

  if (error) return (
    <div className="bg-red-50 text-red-600 rounded-2xl p-6 shadow-xl border border-red-200">
      <h3 className="font-bold">Backend Connection Failed</h3>
      <p className="text-sm mt-1">Please ensure the FastAPI backend is running on port 8000.</p>
    </div>
  );

  if (!weather) return (
    <div className="bg-white/80 backdrop-blur-md rounded-2xl p-6 shadow-xl animate-pulse text-blue-900 border border-white/50 h-[200px] flex items-center justify-center">
      <span className="font-medium">Loading live weather data...</span>
    </div>
  );

  return (
    <div className="bg-gradient-to-br from-blue-500 to-indigo-600 text-white rounded-2xl p-6 shadow-xl relative overflow-hidden border border-blue-400">
      {/* Decorative inner cloud */}
      <div className="absolute -top-10 -right-10 opacity-20 text-9xl">☁️</div>
      <div className="relative z-10">
        <h3 className="text-sm font-semibold tracking-wider text-blue-100 uppercase">Current Conditions</h3>
        <div className="flex justify-between items-end mt-4">
          <div>
            <h1 className="text-5xl font-black">{weather.temperature}°C</h1>
            <p className="text-xl font-medium mt-1">{weather.location}</p>
          </div>
          <div className="text-right">
            <div className="text-4xl mb-1">{weather.condition?.includes("Cloud") ? "🌥️" : "☀️"}</div>
            <p className="text-sm text-blue-100">{weather.condition}</p>
          </div>
        </div>
        <div className="grid grid-cols-2 gap-4 mt-6 pt-4 border-t border-blue-400/50">
          <div>
            <p className="text-xs text-blue-200">Wind</p>
            <p className="font-semibold">{weather.wind_speed} km/h</p>
          </div>
          <div>
            <p className="text-xs text-blue-200">Rain Prob.</p>
            <p className="font-semibold">{weather.rain_probability || 0}%</p>
          </div>
        </div>
      </div>
    </div>
  );
}
