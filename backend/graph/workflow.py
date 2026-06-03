from langgraph.graph import StateGraph

from graph.state import StartupState

from agents.market_agent import market_agent
from agents.revenue_agent import revenue_agent
from agents.swot_agent import swot_agent
from agents.scoring_agent import scoring_agent


builder = StateGraph(
    StartupState
)

builder.add_node(
    "market",
    market_agent
)

builder.add_node(
    "revenue",
    revenue_agent
)

builder.add_node(
    "swot",
    swot_agent
)

builder.add_node(
    "score",
    scoring_agent
)

builder.set_entry_point(
    "market"
)

builder.add_edge(
    "market",
    "revenue"
)

builder.add_edge(
    "revenue",
    "swot"
)

builder.add_edge(
    "swot",
    "score"
)

builder.set_finish_point(
    "score"
)

graph = builder.compile()