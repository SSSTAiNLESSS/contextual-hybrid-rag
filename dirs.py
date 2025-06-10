import os

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

files = [
    "contextual-hybrid-rag/README.md",
    "contextual-hybrid-rag/LICENSE",
    "contextual-hybrid-rag/CONTRIBUTING.md",
    "contextual-hybrid-rag/CHANGELOG.md",
    "contextual-hybrid-rag/CODE_OF_CONDUCT.md",
    "contextual-hybrid-rag/.gitignore",
    "contextual-hybrid-rag/.env.example",
    "contextual-hybrid-rag/requirements.txt",
    "contextual-hybrid-rag/setup.py",
    "contextual-hybrid-rag/pyproject.toml",
    "contextual-hybrid-rag/config/config.yaml",
    "contextual-hybrid-rag/config/logging.yaml",
    "contextual-hybrid-rag/data/raw/sample_documents.pdf",
    "contextual-hybrid-rag/data/processed/processed_chunks.json",
    "contextual-hybrid-rag/data/seed_knowledge/seed_knowledge.json",
    "contextual-hybrid-rag/notebooks/exploratory_analysis.ipynb",
    "contextual-hybrid-rag/scripts/ingest_documents.py",
    "contextual-hybrid-rag/scripts/train_embeddings.py",
    "contextual-hybrid-rag/scripts/run_rag_pipeline.py",
    "contextual-hybrid-rag/scripts/evaluate_system.py",
    "contextual-hybrid-rag/src/__init__.py",
    "contextual-hybrid-rag/src/main.py",
    "contextual-hybrid-rag/src/rag_core/__init__.py",
    "contextual-hybrid-rag/src/rag_core/document_processor.py",
    "contextual-hybrid-rag/src/rag_core/hybrid_retriever.py",
    "contextual-hybrid-rag/src/rag_core/contextual_embedder.py",
    "contextual-hybrid-rag/src/rag_core/reranker.py",
    "contextual-hybrid-rag/src/rag_core/utils.py",
    "contextual-hybrid-rag/src/api/__init__.py",
    "contextual-hybrid-rag/src/api/app.py",
    "contextual-hybrid-rag/src/api/routes.py",
    "contextual-hybrid-rag/src/memory/__init__.py",
    "contextual-hybrid-rag/src/memory/character_memory.py",
    "contextual-hybrid-rag/tests/__init__.py",
    "contextual-hybrid-rag/tests/test_document_processor.py",
    "contextual-hybrid-rag/tests/test_hybrid_retriever.py",
    "contextual-hybrid-rag/tests/test_contextual_embedder.py",
    "contextual-hybrid-rag/tests/test_reranker.py",
    "contextual-hybrid-rag/tests/test_api.py",
    "contextual-hybrid-rag/examples/example_query.py",
    "contextual-hybrid-rag/examples/example_config.yaml",
    "contextual-hybrid-rag/docker/Dockerfile",
    "contextual-hybrid-rag/docker/docker-compose.yml",
    "contextual-hybrid-rag/docs/index.md",
    "contextual-hybrid-rag/docs/architecture.md",
    "contextual-hybrid-rag/docs/api_reference.md",
    "contextual-hybrid-rag/docs/usage.md",
    "contextual-hybrid-rag/docs/faq.md",
    "contextual-hybrid-rag/.github/ISSUE_TEMPLATE/bug_report.md",
    "contextual-hybrid-rag/.github/ISSUE_TEMPLATE/feature_request.md",
    "contextual-hybrid-rag/.github/workflows/ci.yml"
]

for d in dirs:
    os.makedirs(d, exist_ok=True)

for f in files:
    with open(f, "w") as fp:
        if f.endswith(".md"):
            fp.write(f"# {os.path.basename(f)}\n")
        elif f.endswith(".py"):
            fp.write("#!/usr/bin/env python3\n")
        elif f.endswith(".json"):
            fp.write("{}\n")
        elif f.endswith(".yaml"):
            fp.write("# YAML config\n")
        else:
            fp.write("")

print("Project structure created successfully.")
