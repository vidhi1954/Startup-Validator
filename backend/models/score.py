from pydantic import BaseModel

class StartupScore(BaseModel):

    overall_score: float

    market_score: float

    revenue_score: float

    scalability_score: float

    risk_score: float

    recommendation: str