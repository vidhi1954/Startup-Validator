import logging

from services.llm import llm

from models.market import MarketAnalysis

logger = logging.getLogger(__name__)

structured_llm = llm.with_structured_output(
    MarketAnalysis
)

def market_agent(state):
    logger.info("Starting market agent analysis")

    prompt = f"""
    You are a startup market analyst.

    Analyze this startup idea:

    {state["idea"]}

    Return:
    1. target audience
    2. market demand
    3. challenges
    """

    result = structured_llm.invoke(prompt)

    logger.info("Completed market agent analysis")
    return {
        "market_analysis": result.model_dump()
    }