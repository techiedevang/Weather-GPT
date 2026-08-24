# WeatherGPT — Production Master README

WeatherGPT is an uncertainty-aware, evidence-validated, impact-based weather intelligence platform that transforms multi-source meteorological evidence into localized, user-specific and proactive decisions.

**Target:** SIH Internal Selection → SIH Final → Research Publication → Production Deployment  
**Primary stack:** Next.js + TypeScript + Tailwind + FastAPI + Python + PostgreSQL/Supabase + Redis + WebSocket + Groq/LLM

## 1. Product Vision
A conventional weather app answers:
“What is the weather?”

WeatherGPT answers:
“Given the available weather evidence, its uncertainty, my location/context and my upcoming activity, what should I do and why?”

Core capabilities:
- Real-time weather
- NWP/GFS evidence
- Observations
- Official warnings
- Multi-source fusion
- Observation-aware reliability
- Uncertainty estimation
- Impact/risk modelling
- User/activity context
- Grounded AI
- Evidence validation
- English/Hindi/Hinglish
- Proactive alerts
- Personal Weather Planner
- Calendar-weather conflict detection
- Best available time-window recommendation
- Feedback
- Research baselines and reproducible experiments

## 2. Core Research Positioning
WeatherGPT addresses the gap between uncertain meteorological forecasts and reliable localized action by fusing forecast and observation evidence, estimating uncertainty, mapping hazards to user-specific impacts, generating actionable advisories, and independently validating those advisories against the underlying evidence.

**Core loop:**
FORECAST → OBSERVATION CHECK → MULTI-SOURCE FUSION → UNCERTAINTY → IMPACT → USER / ACTIVITY CONTEXT → CALENDAR CONFLICT / PLANNING → ACTION → EVIDENCE VALIDATION → DELIVERY → FEEDBACK / EVALUATION

**Positioning:**
WeatherGPT is an intelligence, safety and decision-support layer above existing meteorological forecasting infrastructure.
It is **not**: A replacement for IMD, a replacement for GFS/WRF, a new global weather foundation model, a generic LLM wrapper, a simple weather API + chat UI, or a claim of perfect forecast accuracy.

## 3. Research Gaps — ALL Mandatory in Internal MVP
Every gap must have: Implementation → Demonstration → Measurement

| Gap | MVP implementation | Evidence |
| --- | --- | --- |
| Forecast → impact | Impact Engine | Impact + action |
| Forecast reliability vs observations | Observation Validator | MAE/RMSE/Bias |
| Multi-source disagreement | Forecast Fusion | Agreement score |
| Weather uncertainty | Uncertainty Engine | Confidence |
| Generic forecast vs user-specific decision | Context Engine | Context-specific action |
| LLM unsupported claims | Evidence Validator | Validation recall |
| Translation vs actionability | Action-preserving multilingual layer | Meaning/action preservation |
| Warning vs decision support | Personalized Alert Engine | Alert → impact → action |
| Reactive weather apps | Personal Weather Planner | Proactive conflict detection |
| “Best time” missing from weather apps | Time-slot optimizer | Lowest-risk valid window |
| No proof over baseline | Research baselines | Comparative metrics |
| No feedback loop | Feedback service | Acknowledgement/feedback |
| Reproducibility | Research framework | Data + scripts + results |

No research gap is merely future scope. Production-scale expansion can be future scope, but every research contribution must have a testable MVP implementation.

## 4. Personal Weather Planner — Mandatory Core Feature
The Personal Weather Planner is a core product differentiator, not a calendar API add-on.

**WeatherGPT vs Normal App:**
“Your 6 PM outdoor event conflicts with the forecast. 4:30 PM is the safer available window because rainfall risk is lower and no higher-severity warning is active.”

**Pipeline:**
Calendar Event → Event Classification → Location + Time Resolution → Hourly Weather / NWP Timeline → Observation + Official Warning Evidence → Uncertainty → Impact / Risk Per Time Slot → Constraint Checking → Best Available Window → Personalized Recommendation → Evidence Validation → Planner Card / Notification

## 5. Architecture & Principles
**Architecture Principles:**
- Evidence before generation.
- LLM never owns weather truth.
- Deterministic logic owns safety-critical risk decisions.
- Every recommendation is explainable.
- Every external dependency can fail safely.
- Source provenance and freshness are preserved.
- No fabricated weather data.
- All LLM output is schema-validated and evidence-checked.

## 6. Technology Stack
- **Frontend:** Next.js, React, TypeScript, Tailwind CSS, shadcn/ui, Framer Motion, TanStack Query, React Leaflet, Recharts
- **Backend:** Python, FastAPI, Pydantic, httpx, AsyncIO, WebSockets
- **AI:** Groq-compatible LLM, Structured output, Tool calling
- **Data:** PostgreSQL, Supabase, PostGIS, Redis
- **Infrastructure:** Docker, Docker Compose, Reverse proxy, CI/CD

## 7. Production Repository Structure
```
WeatherGPT/
├── frontend/
├── backend/
│   ├── app/
│   │   ├── api/, ai/, ingestion/, normalization/, services/, tools/, validation/, fusion/, uncertainty/, impact/, decision/, context/, planner/, feedback/, database/, schemas/, utils/
├── data/
├── research/
│   ├── literature/, baselines/, experiments/, results/
├── docs/
├── scripts/
├── .github/workflows/
├── docker-compose.yml
└── README.md
```

## 8. Definition of Done
The project is not done because the homepage works. It requires:
- **Weather:** Current weather, Forecast, NWP, Observation, Official alerts
- **Research:** Forecast → impact, Observation reliability, Multi-source fusion, Uncertainty, User context, Evidence validation, Multilingual action preservation, Personalized warnings, Calendar conflict detection, Best-window optimization, Feedback, Baseline comparison, Reproducible experiments
- **AI:** Intent extraction, Tool routing, Structured output, Grounded generation, Validator, Bounded regeneration, Safe fallback
- **Product:** Dashboard, Chat, Risk map, Alert center, Planner, Explainability, Feedback
- **Engineering:** Tests, CI, Docker, Logging, Health checks, Failure handling, Environment configuration

## 9. Six-Member Ownership
1. **AI + Validation:** LLM, Intent, Tool routing, Structured output, Evidence validation, Regeneration, Multilingual
2. **Weather/NWP/Observation:** Weather, NWP, Observations, Normalization, Provenance
3. **Research Intelligence:** Fusion, Uncertainty, Impact, Risk, Research metrics
4. **Frontend/UX:** Dashboard, Chat, Risk map, Planner, Alerts, Explainability, Feedback
5. **Backend/Database/Security:** FastAPI, Database, API contracts, Security, Integration
6. **Planner/Realtime/Research Evaluation:** Calendar, Event classification, Time-slot optimization, WebSockets, Baselines, Experiments, Metrics, Reproducibility

## 10. Final Demo Story
1. User asks weather question
2. Multi-source evidence retrieved
3. Observation agreement shown
4. Uncertainty calculated
5. Impact identified
6. User context changes recommendation
7. AI explains evidence
8. Validator approves
9. Planner finds safer time
10. Alert arrives proactively
11. User acknowledges
12. Research dashboard shows metrics

**Disclaimer**
WeatherGPT is a decision-support platform/prototype. Official government warnings and emergency instructions take precedence over recommendations generated by the platform. The interface must clearly communicate data freshness, source provenance and uncertainty.