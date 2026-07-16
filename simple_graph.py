from typing import Dict, TypedDict
from langgraph.graph import StateGraph
class Anushka(TypedDict):
    msg : str

def greeting_mode(state: Anushka) -> Anushka:
    state['msg'] = "Hello, World!"
    return state

graph = StateGraph(Anushka)
graph.add_node("hello world", greeting_mode)
graph.set_entry_point("hello world")
graph.set_finish_point("hello world")

app = graph.compile()

png = app.get_graph().draw_mermaid_png()

with open("graph.png", "wb") as f:
    f.write(png)

print("Graph saved successfully!")