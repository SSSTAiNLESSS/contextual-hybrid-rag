import os

# Directory structure
dirs = [
    "contextual-hybrid-rag/config",
    "contextual-hybrid-rag/data/raw",
    "contextual-hybrid-rag/data/processed",
    "contextual-hybrid-rag/data/seed_knowledge",
    "contextual-hybrid-rag/notebooks",
    "contextual-hybrid-rag/scripts",
    "contextual-hybrid-rag/src/rag_core",
    "contextual-hybrid-rag/src/api",
    "contextual-hybrid-rag/src/memory",
    "contextual-hybrid-rag/tests",
    "contextual-hybrid-rag/examples",
    "contextual-hybrid-rag/docker",
    "contextual-hybrid-rag/docs",
    "contextual-hybrid-rag/.github/ISSUE_TEMPLATE",
    "contextual-hybrid-rag/.github/workflows"
]

# Files to create with minimal placeholder content
files = {
    "contextual-hybrid-rag/README.md": "# Contextual Hybrid RAG\n\nA state-of-the-art Retrieval-Augmented Generation (RAG) system for emotionally resonant storytelling.",
    "contextual-hybrid-rag/LICENSE": "MIT License\n\nCopyright (c) 2025",
    "contextual-hybrid-rag/CONTRIBUTING.md": "# Contributing\n\nThank you for considering contributing!",
    "contextual-hybrid-rag/CHANGELOG.md": "# Changelog\n\nAll notable changes to this project will be documented here.",
    "contextual-hybrid-rag/CODE_OF_CONDUCT.md": "# Code of Conduct\n\nBe respectful, inclusive, and collaborative.",
    "contextual-hybrid-rag/.gitignore": "*.pyc\n__pycache__/\n.env\n.venv/\n",
    "contextual-hybrid-rag/.env.example": "CONTEXT_WINDOW=4096\nCHUNK_SIZE=512\nEMBEDDING_MODEL=text-embedding-3-large",
    "contextual-hybrid-rag/requirements.txt": "numpy\npandas\nscikit-learn\nfastapi\nuvicorn\nelasticsearch\nchromadb\nsentence-transformers\n",
    "contextual-hybrid-rag/setup.py": "from setuptools import setup, find_packages\nsetup(name='contextual_hybrid_rag', packages=find_packages())",
    "contextual-hybrid-rag/pyproject.toml": "[build-system]\nrequires = [\"setuptools\", \"wheel\"]\nbuild-backend = \"setuptools.build_meta\"",

    "contextual-hybrid-rag/config/config.yaml": "# Main configuration file\n",
    "contextual-hybrid-rag/config/logging.yaml": "# Logging configuration\n",

    "contextual-hybrid-rag/data/raw/sample_documents.pdf": "",
    "contextual-hybrid-rag/data/processed/processed_chunks.json": "{}",
    "contextual-hybrid-rag/data/seed_knowledge/seed_knowledge.json": "{}",

    "contextual-hybrid-rag/notebooks/exploratory_analysis.ipynb": "{\n \"cells\": [],\n \"metadata\": {},\n \"nbformat\": 4,\n \"nbformat_minor\": 2\n}",

    "contextual-hybrid-rag/scripts/ingest_documents.py": "#!/usr/bin/env python3\n# Script to ingest documents\n",
    "contextual-hybrid-rag/scripts/train_embeddings.py": "#!/usr/bin/env python3\n# Script to train embeddings\n",
    "contextual-hybrid-rag/scripts/run_rag_pipeline.py": "#!/usr/bin/env python3\n# Script to run the RAG pipeline\n",
    "contextual-hybrid-rag/scripts/evaluate_system.py": "#!/usr/bin/env python3\n# Script to evaluate the system\n",

    "contextual-hybrid-rag/src/__init__.py": "",
    "contextual-hybrid-rag/src/main.py": "# Entry point for the Contextual Hybrid RAG system\n",

    "contextual-hybrid-rag/src/rag_core/__init__.py": "",
    "contextual-hybrid-rag/src/rag_core/document_processor.py": "# Document processing module\n",
    "contextual-hybrid-rag/src/rag_core/hybrid_retriever.py": "# Hybrid retriever module\n",
    "contextual-hybrid-rag/src/rag_core/contextual_embedder.py": "# Contextual embedder module\n",
    "contextual-hybrid-rag/src/rag_core/reranker.py": "# Reranker module\n",
    "contextual-hybrid-rag/src/rag_core/utils.py": "# Utility functions\n",

    "contextual-hybrid-rag/src/api/__init__.py": "",
    "contextual-hybrid-rag/src/api/app.py": "# FastAPI app\n",
    "contextual-hybrid-rag/src/api/routes.py": "# API routes\n",

    "contextual-hybrid-rag/src/memory/__init__.py": "",
    "contextual-hybrid-rag/src/memory/character_memory.py": "# Character memory module\n",

    "contextual-hybrid-rag/tests/__init__.py": "",
    "contextual-hybrid-rag/tests/test_document_processor.py": "# Test for document processor\n",
    "contextual-hybrid-rag/tests/test_hybrid_retriever.py": "# Test for hybrid retriever\n",
    "contextual-hybrid-rag/tests/test_contextual_embedder.py": "# Test for contextual embedder\n",
    "contextual-hybrid-rag/tests/test_reranker.py": "# Test for reranker\n",
    "contextual-hybrid-rag/tests/test_api.py": "# Test for API\n",

    "contextual-hybrid-rag/examples/example_query.py": "# Example query script\n",
    "contextual-hybrid-rag/examples/example_config.yaml": "# Example config\n",

    "contextual-hybrid-rag/docker/Dockerfile": "# Dockerfile for Contextual Hybrid RAG\n",
    "contextual-hybrid-rag/docker/docker-compose.yml": "# docker-compose for Contextual Hybrid RAG\n",

    "contextual-hybrid-rag/docs/index.md": "# Documentation Home\n",
    "contextual-hybrid-rag/docs/architecture.md": "# System Architecture\n",
    "contextual-hybrid-rag/docs/api_reference.md": "# API Reference\n",
    "contextual-hybrid-rag/docs/usage.md": "# Usage Guide\n",
    "contextual-hybrid-rag/docs/faq.md": "# FAQ\n",

    "contextual-hybrid-rag/.github/ISSUE_TEMPLATE/bug_report.md": "# Bug Report\n",
    "contextual-hybrid-rag/.github/ISSUE_TEMPLATE/feature_request.md": "# Feature Request\n",
    "contextual-hybrid-rag/.github/workflows/ci.yml": "# CI Workflow\n"
}

# Create directories
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Create files with placeholder content
for f, content in files.items():
    with open(f, "w", encoding="utf-8") as fp:
        fp.write(content)

print("Contextual Hybrid RAG project structure and files created successfully!")
