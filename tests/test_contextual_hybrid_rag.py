from src.rag_core import ContextualHybridRAG


def test_query_returns_placeholders():
    rag = ContextualHybridRAG()
    results = rag.query("test", top_k=3)
    assert results == [
        "Result 1 for test",
        "Result 2 for test",
        "Result 3 for test",
    ]

