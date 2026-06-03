from services.llm import llm

from models.market import MarketAnalysis

structured_llm = llm.with_structured_output(
    MarketAnalysis
)

def market_agent(state):

    print("\n=== MARKET AGENT START ===")

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
    
    print("\n=== MARKET AGENT END ===") 
    return {
        "market_analysis": result.model_dump()
    }