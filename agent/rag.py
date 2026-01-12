import json
from pathlib import Path

KNOWLEDGE_PATH = Path(__file__).parent.parent / "data" / "knowledge_base.json"

def load_knowledge():
    with open(KNOWLEDGE_PATH, "r") as f:
        return json.load(f)

def retrieve_pricing_info():
    data = load_knowledge()
    pricing = data["pricing"]

    response = (
        f"Basic Plan:\n"
        f"- Price: {pricing['basic']['price']}\n"
        f"- {pricing['basic']['videos']}\n"
        f"- Resolution: {pricing['basic']['resolution']}\n\n"
        f"Pro Plan:\n"
        f"- Price: {pricing['pro']['price']}\n"
        f"- {pricing['pro']['videos']}\n"
        f"- Resolution: {pricing['pro']['resolution']}\n"
        f"- Features: {', '.join(pricing['pro']['features'])}"
    )

    return response
