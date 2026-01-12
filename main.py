from agent.graph import build_graph

def main():
    graph = build_graph()

    state = {
      "user_message": "",
      "response": "",
      "step": "start",
      "intent": None,
      "retrieved_context": None,
      "name": None,
      "email": None,
      "platform": None
}

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Goodbye!")
            break

        state["user_message"] = user_input
        state = graph.invoke(state)

        print("Agent:", state["response"])

if __name__ == "__main__":
    main()
