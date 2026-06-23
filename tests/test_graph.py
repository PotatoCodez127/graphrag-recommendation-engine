import pytest
from unittest.mock import MagicMock, patch
import networkx as nx
from graph_engine import build_knowledge_graph, get_graph_context, query_graph


def test_build_knowledge_graph():
    G = build_knowledge_graph()
    assert isinstance(G, nx.DiGraph)
    assert "Oppenheimer" in G
    assert "Christopher Nolan" in G
    assert G.nodes["Oppenheimer"]["type"] == "Movie"


def test_get_graph_context():
    G = build_knowledge_graph()
    context = get_graph_context(G, "Oppenheimer", max_hops=1)
    
    # Assert relational correctness within the 1-hop boundary
    assert "Christopher Nolan DIRECTED Oppenheimer" in context
    assert "Cillian Murphy ACTED_IN Oppenheimer" in context


@patch("graph_engine.client.chat")
def test_query_graph(mock_chat):
    mock_chat.return_value = {
        "message": {"content": "Test recommendation path: Interstellar via Nolan connection."}
    }
    
    # Run query mapping pipeline to verify execution flow passes safely
    query_graph("Recommend a sci-fi movie", "Oppenheimer")
    mock_chat.assert_called_once()