from pydantic import BaseModel

class RevenueAnalysis(BaseModel):

    pricing_model: str

    revenue_streams: list[str]