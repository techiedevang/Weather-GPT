from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

# Import our modular engines
from app.normalization.evidence_normalizer import gather_normalized_evidence
from app.validation.observation_validator import validate_forecast_against_observation
from app.fusion.forecast_fusion import fuse_forecasts
from app.uncertainty.uncertainty_engine import calculate_uncertainty
from app.impact.impact_engine import determine_impact
from app.decision.risk_engine import calculate_risk_level
from app.planner.planner_service import evaluate_calendar_event
from app.ai.prompt_manager import generate_grounded_prompt
from app.ai.response_generator import generate_ai_response
from app.validation.evidence_validator import validate_ai_evidence

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    location: str = "New Delhi"
    lat: float = 28.6139
    lon: float = 77.2090
    user_type: str = "general" # e.g., "farmer", "traveller"
    activity: Optional[str] = None # e.g., "pesticide_spray", "outdoor_event"
    planned_time: Optional[str] = None # e.g., "16:00"

@router.post("/ask")
async def ask_weathergpt(request: ChatRequest):
    try:
        # STEP 1: Gather and Normalize Evidence (Phase 1)
        evidence = await gather_normalized_evidence(request.location, request.lat, request.lon)
        
        # STEP 2: Research Intelligence Loop (Phase 2)
        obs_validation = validate_forecast_against_observation(evidence)
        fusion_data = fuse_forecasts(evidence)
        uncertainty = calculate_uncertainty(obs_validation, fusion_data)
        
        # STEP 3: Impact and Risk (Phase 2)
        impact = determine_impact(fusion_data, request.user_type, request.activity or "general")
        risk = calculate_risk_level(fusion_data, evidence)
        
        # STEP 4: Personal Weather Planner (Phase 4)
        planner_recommendation = None
        if request.activity and request.planned_time:
            # Mock timeline for the planner based on fusion data
            mock_timeline = [
                {"time": request.planned_time, "risk_score": risk["risk_score"]},
                {"time": "14:00", "risk_score": 15},
                {"time": "18:00", "risk_score": 10}
            ]
            planner_recommendation = evaluate_calendar_event(request.activity, request.planned_time, mock_timeline)
            
        # Compile full evidence payload
        evidence_payload = {
            "evidence_sources": [r.source_id for r in evidence.records],
            "observation_validation": obs_validation,
            "forecast_fusion": fusion_data,
            "uncertainty": uncertainty,
            "impact": impact,
            "risk": risk,
            "planner": planner_recommendation
        }
        
        # STEP 5: AI Generation & Validation (Phase 3)
        prompt = generate_grounded_prompt(evidence_payload, language="english")
        
        # In a real system, you might loop this up to 3 times if validation fails
        ai_response = generate_ai_response(prompt)
        
        is_valid = validate_ai_evidence(ai_response, evidence_payload)
        
        if not is_valid:
            # Fallback if LLM hallucinated
            return {
                "status": "success",
                "answer": "System fallback: The forecast shows moderate risk. Please exercise caution. (LLM output was rejected by Evidence Validator).",
                "risk_level": risk["risk_level"],
                "evidence_payload": evidence_payload
            }

        return {
            "status": "success",
            "answer": ai_response.answer,
            "risk_level": ai_response.risk_level,
            "confidence": ai_response.confidence,
            "recommended_action": ai_response.recommended_action,
            "evidence_payload": evidence_payload
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
