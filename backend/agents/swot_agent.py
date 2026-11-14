import logging

from services.llm import llm

from models.swot import SWOTAnalysis

logger = logging.getLogger(__name__)

structured_llm = llm.with_structured_output(
    SWOTAnalysis
)

def swot_agent(state):
    logger.info("Starting SWOT agent analysis")

    prompt = f"""
    Startup Idea:

    {state["idea"]}

    Market Analysis:

    {state["market_analysis"]}

    Revenue Analysis:

    {state["revenue_analysis"]}

    Generate SWOT Analysis.
    """

    result = structured_llm.invoke(prompt)

    logger.info("Completed SWOT agent analysis")
    return {
        "swot_analysis": result.model_dump()
    }