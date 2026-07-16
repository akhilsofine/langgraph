# LangGraph Learning

A hands-on repository documenting my journey of learning **LangGraph** by building graph-based AI workflows in Python. This project starts with the fundamentals of `StateGraph` and gradually progresses toward advanced concepts such as conditional routing, memory, tool calling, and AI agents.

## 🚀 Features

* Build workflows using `StateGraph`
* Manage application state with `TypedDict`
* Create and connect multiple graph nodes
* Define entry and finish points
* Execute sequential workflows
* Visualize graphs using Mermaid diagrams
* Generate graph images (`graph.png`)

## 📂 Project Structure

```text
langgraph/
│── simple_graph.py      # Basic LangGraph examples
│── graph.png            # Generated graph visualization
│── README.md
```

## 🛠️ Technologies Used

* Python 3.x
* LangGraph
* IPython
* Mermaid (Graph Visualization)

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/akhilsofine/langgraph.git
cd langgraph
```

Create a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install langgraph ipython
```

## ▶️ Running the Project

Run the example:

```bash
python simple_graph.py
```

The program will:

* Execute the LangGraph workflow
* Generate a Mermaid graph visualization
* Save the visualization as `graph.png`

## 📖 Concepts Covered

### ✅ Single-Node StateGraph

```text
START
  │
  ▼
hello_world
  │
  ▼
END
```

### ✅ Multi-Node Sequential StateGraph

```text
START
  │
  ▼
greeter
  │
  ▼
greeting_with_age
  │
  ▼
END
```

## 📚 LangGraph Concepts Learned

* StateGraph
* TypedDict
* State Management
* Nodes
* Edges
* Sequential Workflows
* Entry Point
* Finish Point
* Graph Compilation
* Graph Execution
* Mermaid Graph Visualization

## 🎯 Learning Roadmap

Planned additions to this repository include:

* Conditional Edges
* Branching Workflows
* Loops
* Tool Calling
* Memory
* ReAct Agents
* AI Agent Workflows
* Multi-Agent Systems
* Retrieval-Augmented Generation (RAG) with LangGraph

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome. Feel free to fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License.
