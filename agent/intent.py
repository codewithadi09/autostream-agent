def detect_intent(message: str) -> str:
    message = message.lower()

    # 1. Greeting
    if any(word in message for word in ["hi", "hello", "hey"]):
        return "greeting"

    # 2. High intent (must come BEFORE pricing)
    if any(word in message for word in ["sign up", "try", "subscribe", "ready", "start"]):
        return "high_intent"

    # 3. Product / pricing inquiry
    if any(word in message for word in ["price", "cost", "plan", "pricing"]):
        return "product_inquiry"

    # Default fallback
    return "product_inquiry"