from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# Initialize LLM once
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

SYSTEM_PROMPT = """
You are an intent classification engine for a SaaS product called AutoStream.

Your job is to classify the user's message into EXACTLY one of the following labels:

- greeting
- product_inquiry
- high_intent

Rules:
- Return ONLY the label.
- Do NOT add explanations.
- Do NOT add punctuation.
- Do NOT add extra text.

Examples:
"hi" → greeting
"how much does it cost?" → product_inquiry
"I want to try the pro plan" → high_intent
"""

def detect_intent(message: str) -> str:
    response = llm.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=message)
    ])

    return response.content.strip().lower()
