from services.llm import llm

from models.swot import SWOTAnalysis

structured_llm = llm.with_structured_output(
    SWOTAnalysis
)

def swot_agent(state):

    print("\n=== SWOT AGENT START ===")

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
    
    print("\n=== SWOT AGENT END ===")
    return {
        "swot_analysis": result.model_dump()
    }                                           