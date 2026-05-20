from typing import TypedDict
from langgraph.graph import StateGraph, END

class AgentState(TypedDict):
    customer: dict
    vehicles: list
    recommendation: str

def fetch_customer(state):
    state["customer"] = {
        "membership": "gold"
    }
    return state

def fetch_vehicles(state):
    state["vehicles"] = [
        "Toyota Fortuner",
        "Hyundai Creta"
    ]
    return state

def recommend(state):
    if state["customer"]["membership"] == "gold":
        state["recommendation"] = "Upgrade to Toyota Fortuner"

    return state

graph = StateGraph(AgentState)

graph.add_node("customer", fetch_customer)
graph.add_node("vehicles", fetch_vehicles)
graph.add_node("recommend", recommend)

graph.set_entry_point("customer")

graph.add_edge("customer", "vehicles")
graph.add_edge("vehicles", "recommend")
graph.add_edge("recommend", END)

app = graph.compile()

result = app.invoke({})

print(result)