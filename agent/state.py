from typing import TypedDict

class AgentState(TypedDict):
    user_message: str
    response: str
    step: str
