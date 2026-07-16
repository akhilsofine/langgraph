from typing import TypedDict
from langgraph.graph import StateGraph


# Define the state
class Anushka(TypedDict):
    msg: str
    age: int


# Node 1: Greeter
def greeter(state: Anushka) -> Anushka:
    state["msg"] = "Hello!"
    return state


# Node 2: Greeting with age
def greeting_with_age(state: Anushka) -> Anushka:
    state["msg"] = f"{state['msg']} You are {state['age']} years old."
    return state


# Create the graph
graph = StateGraph(Anushka)

# Add nodes
graph.add_node("greeter", greeter)
graph.add_node("greeting_with_age", greeting_with_age)

# Set entry point
graph.set_entry_point("greeter")

# Connect the nodes
graph.add_edge("greeter", "greeting_with_age")

# Set finish point
graph.set_finish_point("greeting_with_age")

# Compile the graph
app = graph.compile()

# Run the graph
result = app.invoke({
    "msg": "",
    "age": 21
})

print(result)

# Save the graph as an image
png = app.get_graph().draw_mermaid_png()

with open("graph.png", "wb") as f:
    f.write(png)

print("Graph saved successfully!")