from pydantic import BaseModel

class SWOTAnalysis(BaseModel):

    strengths: list[str]

    weaknesses: list[str]

    opportunities: list[str]

    threats: list[str]