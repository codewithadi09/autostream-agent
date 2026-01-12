from langgraph.graph import StateGraph
from agent.state import AgentState

def simple_response_node(state: AgentState) -> AgentState:
    if state["step"] == "start":
        state["response"] = "Hi! I’m AutoStream. I can help you with pricing and features."
        state["step"] = "greeted"
    else:
        state["response"] = (
            "We have two plans:\n"
            "Basic: $29/month, 10 videos, 720p\n"
            "Pro: $79/month, unlimited videos, 4K, AI captions"
        )
        state["step"] = "pricing_shared"

    return state

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("simple", simple_response_node)
    graph.set_entry_point("simple")

    return graph.compile()
