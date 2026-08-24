@echo off
echo ===================================================
echo Starting WeatherGPT Hackathon MVP...
echo ===================================================

echo [1/2] Starting FastAPI Backend on port 8000...
start cmd /k "cd backend && .\venv\Scripts\activate && uvicorn app.main:app --reload"

echo [2/2] Starting Next.js Frontend on port 3000...
start cmd /k "cd frontend && npm run dev"

echo.
echo Both servers are starting in new windows.
echo Please wait a few seconds and then open: http://localhost:3000
echo.
pause
