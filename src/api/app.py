from fastapi import FastAPI
from rag_core import ContextualHybridRAG

app = FastAPI()

rag = ContextualHybridRAG()

@app.post("/query")
async def query_endpoint(query: str, top_k: int = 5):
    return rag.query(query, top_k)
