#!/usr/bin/env python3
"""
Demo: Simple RAG (Retrieval-Augmented Generation) Example

This demo script showcases the basic concepts of RAG without requiring
full Google Cloud setup. It demonstrates:
1. Document ingestion and chunking
2. Vector similarity search simulation
3. Context-aware response generation

Usage:
    python demo_rag_simple.py
"""

import json
import os
from typing import List, Dict, Any
from datetime import datetime


class SimpleRAGDemo:
    """
    A simplified RAG implementation for demonstration purposes.
    This simulates the core concepts without external dependencies.
    """
    
    def __init__(self):
        self.documents = []
        self.chunks = []
        self.knowledge_base = {}
        
    def add_document(self, content: str, title: str = "Untitled") -> None:
        """Add a document to the knowledge base."""
        doc_id = len(self.documents)
        document = {
            "id": doc_id,
            "title": title,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        self.documents.append(document)
        self._create_chunks(document)
        print(f"✅ Added document: '{title}' with {len(content)} characters")
    
    def _create_chunks(self, document: Dict[str, Any], chunk_size: int = 200) -> None:
        """Break document into smaller chunks for better retrieval."""
        content = document["content"]
        words = content.split()
        
        for i in range(0, len(words), chunk_size // 10):  # Rough word-based chunking
            chunk_words = words[i:i + chunk_size // 10]
            chunk_content = " ".join(chunk_words)
            
            if chunk_content.strip():
                chunk = {
                    "id": len(self.chunks),
                    "doc_id": document["id"],
                    "doc_title": document["title"],
                    "content": chunk_content,
                    "keywords": self._extract_keywords(chunk_content)
                }
                self.chunks.append(chunk)
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Simple keyword extraction (in real RAG, this would use embeddings)."""
        # Remove common words and extract meaningful terms
        stop_words = {"the", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by", "a", "an", "is", "are", "was", "were", "be", "been", "have", "has", "had", "do", "does", "did", "will", "would", "could", "should", "this", "that", "they", "them", "their", "there", "then", "than", "what", "when", "where", "which", "while", "who", "why", "how"}
        words = text.lower().replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace("(", "").replace(")", "").split()
        keywords = [word for word in words if len(word) > 2 and word not in stop_words]  # Reduced minimum length to 3
        return list(set(keywords[:15]))  # Return unique keywords, max 15
    
    def search_relevant_chunks(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Find relevant chunks for a given query.
        In a real RAG system, this would use vector similarity.
        Here we use simple keyword matching for demo purposes.
        """
        query_keywords = self._extract_keywords(query)
        chunk_scores = []
        
        for chunk in self.chunks:
            # Calculate relevance score based on keyword overlap
            overlap = len(set(query_keywords) & set(chunk["keywords"]))
            score = overlap / max(len(query_keywords), 1)
            
            # Boost score if query words appear directly in content
            content_lower = chunk["content"].lower()
            for word in query.lower().split():
                if word in content_lower and len(word) > 2:  # Reduced minimum length
                    score += 0.3  # Increased boost for direct matches
            
            chunk_scores.append((chunk, score))
        
        # Sort by relevance score and return top_k
        chunk_scores.sort(key=lambda x: x[1], reverse=True)
        relevant_chunks = [chunk for chunk, score in chunk_scores[:top_k] if score > 0]
        
        print(f"🔍 Found {len(relevant_chunks)} relevant chunks for query: '{query}'")
        return relevant_chunks
    
    def generate_response(self, query: str) -> str:
        """
        Generate a response using retrieved context.
        This simulates what a real LLM would do with the context.
        """
        relevant_chunks = self.search_relevant_chunks(query)
        
        if not relevant_chunks:
            return f"I don't have enough information to answer: '{query}'. Please add more relevant documents to the knowledge base."
        
        # Construct context from relevant chunks
        context_parts = []
        for chunk in relevant_chunks:
            context_parts.append(f"From '{chunk['doc_title']}': {chunk['content']}")
        
        context = "\n\n".join(context_parts)
        
        # Simulate LLM response generation (in reality, this would be an API call)
        response = f"""Based on the available information, here's what I found:

{context}

This information comes from {len(relevant_chunks)} relevant source(s) in the knowledge base."""
        
        return response
    
    def display_stats(self) -> None:
        """Display statistics about the knowledge base."""
        print("\n📊 Knowledge Base Statistics:")
        print(f"   Documents: {len(self.documents)}")
        print(f"   Chunks: {len(self.chunks)}")
        total_chars = sum(len(doc["content"]) for doc in self.documents)
        print(f"   Total content: {total_chars} characters")


def run_demo():
    """Run the RAG demo with sample data."""
    print("🚀 Starting Simple RAG Demo")
    print("=" * 50)
    
    # Initialize RAG system
    rag = SimpleRAGDemo()
    
    # Add sample documents (simulating what the Jupyter notebook does)
    sample_docs = [
        {
            "title": "What is RAG?",
            "content": """RAG (Retrieval-Augmented Generation) is a technique that enhances large language models by providing them with relevant external information during generation. It works by first retrieving relevant documents or passages from a knowledge base, then using this context to generate more accurate and informative responses. RAG is particularly useful for tasks that require up-to-date information or domain-specific knowledge that wasn't in the model's training data."""
        },
        {
            "title": "Weaviate Vector Database",
            "content": """Weaviate is an open-source vector database that stores and retrieves data based on semantic similarity rather than exact matches. It uses machine learning models to create vector embeddings of your data, allowing for intelligent search and retrieval. Weaviate supports various data types including text, images, and more, making it ideal for building RAG systems and other AI applications."""
        },
        {
            "title": "Vertex AI Platform",
            "content": """Google Cloud's Vertex AI is a unified machine learning platform that provides tools for building, deploying, and scaling ML models. It includes pre-trained models, custom model training capabilities, and managed services for various AI tasks. Vertex AI RAG Engine specifically helps developers build retrieval-augmented generation systems with minimal setup and maintenance."""
        }
    ]
    
    # Add documents to knowledge base
    for doc in sample_docs:
        rag.add_document(doc["content"], doc["title"])
    
    rag.display_stats()
    
    # Demo queries (similar to the notebook example)
    demo_queries = [
        "What is RAG and why is it helpful?",
        "How does Weaviate work?",
        "Tell me about Vertex AI",
        "What are vector databases used for?"
    ]
    
    print("\n🤖 Demo Queries and Responses:")
    print("=" * 50)
    
    for query in demo_queries:
        print(f"\n❓ Query: {query}")
        print("-" * 30)
        response = rag.generate_response(query)
        print(response)
        print()
    
    print("✨ Demo completed! This showcases the basic RAG workflow:")
    print("   1. Documents are ingested and chunked")
    print("   2. Relevant chunks are retrieved for queries")
    print("   3. Context is used to generate informed responses")


if __name__ == "__main__":
    run_demo()