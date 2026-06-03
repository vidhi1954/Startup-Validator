from pydantic import BaseModel

class MarketAnalysis(BaseModel):

    target_audience: str

    market_demand: str

    challenges: list[str]