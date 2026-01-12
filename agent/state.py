from typing import TypedDict, Optional

class AgentState(TypedDict):
    user_message: str
    response: str
    step: str
    intent: Optional[str]
    retrieved_context: Optional[str]
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]


