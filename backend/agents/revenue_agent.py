from services.llm import llm

from models.revenue import RevenueAnalysis

structured_llm = llm.with_structured_output(
    RevenueAnalysis
)

def revenue_agent(state):
    print("\n=== REVENUE AGENT START ===")

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

    print("\n=== REVENUE AGENT END ===")
    return {
        "revenue_analysis": result.model_dump()
    }