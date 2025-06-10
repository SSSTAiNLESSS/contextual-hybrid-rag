# Contextual Hybrid RAG

A state-of-the-art Retrieval-Augmented Generation system designed for emotionally resonant storytelling.  
This project combines hybrid retrieval, contextual chunk enhancement, and multi-stage reranking to generate coherent, heart-wrenching narratives from minimal seed inputs.

## Features
- Hybrid BM25 + Vector search
- Sentiment-aware reranking
- Modular architecture for scalability
- Evaluation metrics for emotional impact and coherence

## Running the API

Use the ``run_api.py`` helper script to start the development server. The script
detects your operating system and chooses the correct Python executable from the
``.venv`` directory. On Windows it uses ``.venv\Scripts\python.exe`` while on
Unix systems it uses ``.venv/bin/python``. Simply run:

```bash
python run_api.py
```

This will activate the virtual environment if necessary and launch Uvicorn with
automatic reload enabled.
