```markdown
# Contextual Hybrid RAG

A state-of-the-art Retrieval-Augmented Generation (RAG) system designed for emotionally resonant storytelling. This project combines hybrid retrieval techniques, contextual chunk enhancement, and multi-stage reranking to generate coherent, heart-wrenching narratives from minimal seed inputs.

---

## Features

- Hybrid retrieval combining lexical (BM25) and semantic (vector) search for precision and depth.
- Contextual augmentation of document chunks to preserve narrative coherence.
- Sentiment-aware reranking to ensure emotional alignment.
- Modular architecture supporting scalable deployment.
- Evaluation metrics including Tear-Jerk Index (TJI) and Narrative Coherence Score.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Implementation](#implementation)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

Clone the repository and install dependencies:

```
git clone https://github.com/SSSTAiNLESSS/contextual-hybrid-rag.git
cd contextual-hybrid-rag
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Usage

Run the main pipeline or query the RAG system:

```
python src/main.py --query "Father receives terminal diagnosis"
```

Or use the Python API:

```
from src.rag_core import ContextualHybridRAG

rag = ContextualHybridRAG()
results = rag.query("Estranged daughter visits father in hospital", top_k=5)
for res in results:
    print(res)
```

---

## Configuration

Edit `config/config.yaml` to adjust parameters such as chunk size, embedding model, and fusion weights.

---

## Implementation

The system consists of:

- DocumentProcessor: Handles chunking and context enrichment.
- HybridRetriever: Performs lexical and semantic retrieval with reciprocal rank fusion.
- MultiStageReranker: Applies sentiment-aware reranking for emotional consistency.

See `src/rag_core/` for detailed modules.

---

## Evaluation

Metrics include:

- Tear-Jerk Index (TJI): Human-rated emotional impact score.
- Narrative Coherence Score: Automated BERT-based consistency metric.
- Hallucination Rate: Percentage of unsupported generated details.

---

## Contributing

Contributions are welcome! Please read `CONTRIBUTING.md` for guidelines.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.
```