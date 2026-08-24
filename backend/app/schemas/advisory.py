from pydantic import BaseModel
from typing import List, Optional

class RiskScore(BaseModel):
    level: str  # Low, Moderate, High, Critical
    score: float
    factors: List[str]

class AdvisoryResult(BaseModel):
    domain: str
    risk: RiskScore
    advice: List[str]
