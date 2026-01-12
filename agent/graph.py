from langgraph.graph import StateGraph
from agent.intent import detect_intent
from agent.state import AgentState
from agent.rag import retrieve_pricing_info
from agent.tools import mock_lead_capture


def intent_router_node(state: AgentState) -> AgentState:
    message = state["user_message"].strip()

    # 🔒 If already in lead collection, lock intent
    if state.get("step") in [
        "collecting_name",
        "collecting_email",
        "collecting_platform",
    ]:
        intent = "high_intent"
    else:
        intent = detect_intent(message)
        intent = intent.strip().lower()   # 🔑 normalize
        state["intent"] = intent

    # ---------- GREETING ----------
    if intent == "greeting":
        state["response"] = "Hi! I’m AutoStream. I can help you with pricing and features."
        state["step"] = "greeted"

    # ---------- PRODUCT INQUIRY ----------
    elif intent == "product_inquiry":
        pricing_info = retrieve_pricing_info()
        state["retrieved_context"] = pricing_info
        state["response"] = pricing_info
        state["step"] = "pricing_shared"

    # ---------- HIGH INTENT → LEAD CAPTURE ----------
    elif intent == "high_intent":

        if state.get("step") == "collecting_name":
            state["name"] = message
            state["response"] = "Thanks! What’s your email address?"
            state["step"] = "collecting_email"

        elif state.get("step") == "collecting_email":
            state["email"] = message
            state["response"] = "Awesome. Which platform do you create content on?"
            state["step"] = "collecting_platform"

        elif state.get("step") == "collecting_platform":
            state["platform"] = message
            mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )
            state["response"] = "You’re all set! Our team will reach out to you shortly 🚀"
            state["step"] = "lead_captured"

        else:
            state["response"] = "Great! What’s your name?"
            state["step"] = "collecting_name"

    # ---------- SAFETY NET ----------
    else:
        state["response"] = "Sorry, I didn’t quite get that. Could you rephrase?"
        state["step"] = "fallback"

    return state


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("intent_router", intent_router_node)
    graph.set_entry_point("intent_router")
    return graph.compile()
