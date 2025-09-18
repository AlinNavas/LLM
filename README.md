# LLM Demo Repository

This repository contains demonstrations of Large Language Model (LLM) implementations and related technologies.

## Contents

### 📁 `gemini/rag-engine/`
- **`rag_engine_weaviate.ipynb`** - Jupyter notebook demonstrating Vertex AI RAG Engine with Weaviate vector database

### 🐍 `demo_rag_simple.py`
- **Simple RAG Demo** - A standalone Python script that demonstrates RAG (Retrieval-Augmented Generation) concepts without external dependencies

## Quick Start

### Running the Simple RAG Demo

The `demo_rag_simple.py` script provides an easy-to-understand demonstration of how RAG systems work:

```bash
python demo_rag_simple.py
```

This demo showcases:
1. **Document Ingestion** - Adding documents to a knowledge base
2. **Text Chunking** - Breaking documents into searchable chunks
3. **Retrieval** - Finding relevant information for queries
4. **Generation** - Using retrieved context to answer questions

### What is RAG?

RAG (Retrieval-Augmented Generation) is a technique that enhances language models by:
- Retrieving relevant information from external knowledge sources
- Using this context to generate more accurate and informative responses
- Enabling models to access up-to-date or domain-specific information

## Demo Features

The simple demo includes:
- ✅ Document ingestion and management
- ✅ Automatic text chunking
- ✅ Keyword-based similarity search (simulating vector search)
- ✅ Context-aware response generation
- ✅ Knowledge base statistics and insights

## Requirements

- Python 3.6+
- No external dependencies for the simple demo!

## Advanced Usage

For production RAG systems, see the Jupyter notebook which demonstrates:
- Google Cloud Vertex AI integration
- Weaviate vector database usage
- Real vector embeddings and similarity search
- Production-ready RAG pipelines

## Contributing

Feel free to add more demo scripts or improve existing ones!