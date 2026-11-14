import logging

from services.llm import llm

from models.revenue import RevenueAnalysis

logger = logging.getLogger(__name__)

structured_llm = llm.with_structured_output(
    RevenueAnalysis
)

def revenue_agent(state):
    logger.info("Starting revenue agent analysis")

    prompt = f"""
    Startup Idea:

    {state["idea"]}

    Market Analysis:

    {state["market_analysis"]}

    Suggest:

    1. pricing model
    2. revenue streams
    """

    result = structured_llm.invoke(prompt)

    logger.info("Completed revenue agent analysis")
    return {
        "revenue_analysis": result.model_dump()
    }