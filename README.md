# 🌩️ WeatherGPT - SIH MVP

WeatherGPT is an AI-powered weather intelligence and early-warning layer. It integrates real-time meteorological data, NWP outputs, and official warnings to turn complex weather information into personalized, multilingual, and actionable decisions.

## 🚀 Features (Hackathon Ready)
- **Natural Language Querying**: Ask weather questions in English, Hindi, or Hinglish (powered by Groq / LLaMA3-70b).
- **Voice Enabled**: Native Web Speech API integration for Voice-to-Text and Text-to-Speech.
- **Risk & Advisory Engine**: Deterministic rules provide safe, non-hallucinated advice for Farmers and Citizens.
- **Real-Time Alerts**: WebSockets push critical disaster warnings to the dashboard instantly.
- **Climate Analytics**: Analyzes historical climate trends.
- **Modern UI**: Next.js App Router with Tailwind CSS glassmorphism & cloud theme.

## 🛠️ Tech Stack
- **Frontend**: Next.js, React, Tailwind CSS
- **Backend**: Python, FastAPI, WebSockets
- **AI**: Groq API (LLaMA3)
- **Database**: Supabase (PostgreSQL)

## ⚡ How to Run Locally

### 1. Environment Setup
Create a `.env` file inside the `backend/` directory:
```env
GROQ_API_KEY=your_groq_api_key_here
SUPABASE_URL=your_supabase_url_here (optional)
SUPABASE_ANON_KEY=your_supabase_key_here (optional)
```

### 2. Quick Start (Windows)
Simply double-click the `start.bat` file in the root directory! This will open two terminals and start both the backend and the frontend.

### 3. Manual Start
**Backend:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000` in your browser.

## 🧪 How to trigger a Real-Time Alert Demo
While the dashboard is open, open a new terminal and run:
```bash
curl -X POST "http://localhost:8000/api/v1/alerts" -H "Content-Type: application/json" -d "{\"title\":\"Cyclone Warning\",\"description\":\"Severe cyclonic storm approaching the coast within 24 hours. Evacuate low-lying areas.\",\"severity\":\"Critical\",\"location\":\"Coastal Regions\"}"
```
Watch the Alert Center instantly update on the frontend without a page refresh!