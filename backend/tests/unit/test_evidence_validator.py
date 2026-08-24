import pytest
from app.validation.evidence_validator import validate_ai_evidence
from app.ai.structured_output import AIAdvisoryResponse

def test_evidence_validator_passes_valid_output():
    # Mock LLM Output
    ai_response = AIAdvisoryResponse(
        answer="Valid response",
        risk_level="HIGH",
        confidence="MODERATE",
        recommended_action="Stay indoors",
        reasons=[],
        language_used="english"
    )
    
    # Mock mathematical backend output
    evidence_payload = {
        "risk": {"risk_level": "HIGH"},
        "uncertainty": {"confidence": "MODERATE"}
    }
    
    assert validate_ai_evidence(ai_response, evidence_payload) == True

def test_evidence_validator_blocks_hallucinated_risk():
    ai_response = AIAdvisoryResponse(
        answer="Hallucinated response",
        risk_level="CRITICAL", # LLM hallucinates danger
        confidence="HIGH",
        recommended_action="Evacuate",
        reasons=[],
        language_used="english"
    )
    
    evidence_payload = {
        "risk": {"risk_level": "LOW"}, # Actual math says low risk
        "uncertainty": {"confidence": "HIGH"}
    }
    
    assert validate_ai_evidence(ai_response, evidence_payload) == False

def test_evidence_validator_blocks_hallucinated_confidence():
    ai_response = AIAdvisoryResponse(
        answer="Hallucinated response",
        risk_level="MODERATE",
        confidence="HIGH", # LLM hallucinates confidence
        recommended_action="Proceed",
        reasons=[],
        language_used="english"
    )
    
    evidence_payload = {
        "risk": {"risk_level": "MODERATE"},
        "uncertainty": {"confidence": "LOW"} # Actual math says low confidence due to model disagreement
    }
    
    assert validate_ai_evidence(ai_response, evidence_payload) == False
