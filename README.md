# LangGraph Learning

A beginner-friendly repository for learning **LangGraph** by building graph-based AI workflows using Python. This project demonstrates the core concepts of LangGraph, including state management, nodes, graph execution, and workflow visualization.

## 🚀 Features

* Build workflows using `StateGraph`
* Define and manage application state with `TypedDict`
* Create and connect graph nodes
* Set entry and finish points
* Compile and execute LangGraph applications
* Visualize workflow graphs using Mermaid diagrams

## 📂 Project Structure

```text
langgraph/
│── simple_graph.py      # Basic LangGraph example
│── graph.png            # Generated workflow graph
└── README.md
```

## 🛠️ Technologies Used

* Python 3.x
* LangGraph
* IPython
* Mermaid (for graph visualization)

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/akhilsofine/langgraph.git
cd langgraph
```

Create and activate a virtual environment:

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

Install the required packages:

```bash
pip install langgraph ipython
```

## ▶️ Run the Project

```bash
python simple_graph.py
```

If you're running the script from the terminal, save the generated graph as `graph.png` to view it. In Jupyter Notebook, the graph can be displayed directly.

## 📚 Concepts Covered

* StateGraph
* TypedDict
* Nodes
* State Management
* Entry Point
* Finish Point
* Graph Compilation
* Graph Execution
* Mermaid Graph Visualization

## 🎯 Learning Goal

This repository is part of my journey to learn LangGraph and build graph-based AI applications. Future updates will include:

* Multiple connected nodes
* Conditional edges
* Tool calling
* Agent workflows
* Memory integration
* Retrieval-Augmented Generation (RAG)
* Multi-agent systems

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome. Feel free to fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License.
