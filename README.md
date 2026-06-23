# graphrag-recommendation-engine

[![CI Pipeline](https://github.com/potatocodez127/graphrag-recommendation-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/potatocodez127/graphrag-recommendation-engine/actions/workflows/ci.yml)

## Executive Summary
`graphrag-recommendation-engine` is an institutional-grade GraphRAG middleware pipeline designed to execute multi-hop relational reasoning across structured entity-relationship networks. By substituting traditional text vector proximity models with an in-memory directed graph topology, the engine traverses interconnected nodes (Directors, Movies, Actors, Genres) to solve complex "missing link" logical queries that fail under standard semantic search architectures.

## Architectural Ingenuity
* **Deterministic Relational Traversal**: Utilizes high-performance directed graphs (`NetworkX`) to map explicit entity paths, allowing the inference engine to navigate connections deterministically without experiencing semantic context drift.
* **Isolated Ego-Network Extraction**: Features an N-hop sub-graph compilation engine that executes shortest-path neighborhood cuts around a target node, restricting the context payload to highly localized topological paths to maximize prompt efficiency.
* **Mock-Validated Test Rig**: Features a robust, dependency-free continuous integration layout that validates structural graph characteristics and intercepts LLM execution layers using mocking hooks inside GitHub Actions.
* **Deterministic Container Layer**: Engineered around a layer-cached Docker footprint using `python:3.11-slim` with absolute `TZ=UTC` attributes to maintain environmental parity and eliminate temporal synchronization issues.

## Topology & Execution Pipeline
1. **Knowledge Graph Construction (`build_knowledge_graph`)**: Maps domain elements as absolute nodes and links them via directional, typed attributes (`DIRECTED`, `ACTED_IN`, `IS_GENRE`) inside an in-memory `nx.DiGraph` architecture.
2. **Sub-graph Context Extraction (`get_graph_context`)**: Casts the directed fabric into an undirected layout to compute single-source shortest path parameters within an explicit radius limit (`max_hops=3`), then projects those nodes back into a sub-graph to generate sorted relational strings.
3. **Prompt Grounding Loop (`query_graph`)**: Interpolates the derived sub-graph structural strings into a strict system role boundary constraint, enforcing structural logic checks before sending payload calls to the Ollama Cloud API.## The Problem Solved
Standard RAG relies on vector similarity, making it terrible at "Missing Link" problems (e.g., "Recommend a movie directed by the person who directed Inception, but in the Comedy genre"). Graph databases solve this by explicitly linking data nodes, allowing the AI to traverse paths to find exact, factual connections.

## Tech Stack
* **Python 3.10+**
* **NetworkX:** A Python library for the creation, manipulation, and study of complex networks (our local Graph DB substitute).
* **Ollama Cloud:** For the LLM reasoning phase.

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment.
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file and add your API key:
   `OLLAMA_API_KEY=your_api_key_here`

## Usage
Run the main graph engine:
`python graph_engine.py`