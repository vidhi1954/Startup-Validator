from services.llm import llm

from models.score import StartupScore

structured_llm = llm.with_structured_output(
    StartupScore
)

def scoring_agent(state):
    print("\n=== SCORING AGENT START ===")

    prompt = f"""
    You are an expert startup investor.

    Evaluate the startup idea.

    Startup Idea:
    {state["idea"]}

    Market Analysis:
    {state["market_analysis"]}

    Revenue Analysis:
    {state["revenue_analysis"]}

    SWOT Analysis:
    {state["swot_analysis"]}

    Score each category from 0-10:

    1. Market Potential
    2. Revenue Potential
    3. Scalability
    4. Risk

    Generate:

    - overall_score
    - market_score
    - revenue_score
    - scalability_score
    - risk_score

    Also provide a short recommendation.

    Be realistic and critical.
    """

    result = structured_llm.invoke(prompt)

    print("\n=== SCORING AGENT END ===")
    return {
        "startup_score": result.model_dump()
    }