from langgraph.graph import StateGraph
from agent.intent import detect_intent
from agent.state import AgentState


def intent_router_node(state: AgentState) -> AgentState:
    message = state["user_message"]

    intent = detect_intent(message)
    state["intent"] = intent

    if intent == "greeting":
        state["response"] = "Hi! I’m AutoStream. I can help you with pricing and features."
        state["step"] = "greeted"

    elif intent == "product_inquiry":
        state["response"] = (
            "We have two plans:\n"
            "Basic: $29/month, 10 videos, 720p\n"
            "Pro: $79/month, unlimited videos, 4K, AI captions"
        )
        state["step"] = "pricing_shared"

    elif intent == "high_intent":
        state["response"] = (
            "That’s great to hear! I can help you get started. "
            "I’ll just need a few details."
        )
        state["step"] = "lead_detected"

    return state


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("intent_router", intent_router_node)
    graph.set_entry_point("intent_router")
    return graph.compile()
