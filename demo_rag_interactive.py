#!/usr/bin/env python3
"""
Interactive RAG Demo

This script provides an interactive interface to the RAG demo,
allowing users to add their own documents and ask questions.

Usage:
    python demo_rag_interactive.py
"""

import json
import os
from demo_rag_simple import SimpleRAGDemo


def load_config():
    """Load configuration if available."""
    config_file = "demo_config.json"
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️  Could not load config: {e}")
    return None


def interactive_demo():
    """Run an interactive RAG demo."""
    print("🤖 Interactive RAG Demo")
    print("=" * 40)
    print("Welcome! This demo lets you:")
    print("1. Add your own documents")
    print("2. Ask questions about them")
    print("3. See how RAG retrieval works")
    print()
    
    # Initialize RAG system
    rag = SimpleRAGDemo()
    config = load_config()
    
    # Load sample documents from config if available
    if config and "sample_documents" in config:
        print("Loading sample documents from config...")
        for doc in config["sample_documents"]:
            if doc["content"].strip() and "Add your own content" not in doc["content"]:
                rag.add_document(doc["content"], doc["title"])
        print()
    else:
        # Load default sample documents
        print("Loading default sample documents...")
        sample_docs = [
            {
                "title": "Machine Learning Basics",
                "content": "Machine learning is a subset of artificial intelligence that enables computers to learn and improve from experience without being explicitly programmed. It involves algorithms that can identify patterns in data and make predictions or decisions based on those patterns."
            },
            {
                "title": "Neural Networks",
                "content": "Neural networks are computing systems inspired by biological neural networks. They consist of interconnected nodes (neurons) that process information through weighted connections. Deep learning uses multi-layer neural networks to solve complex problems."
            }
        ]
        
        for doc in sample_docs:
            rag.add_document(doc["content"], doc["title"])
        print()
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a new document")
        print("2. Ask a question")
        print("3. View knowledge base stats")
        print("4. Quit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            add_document_interactive(rag)
        elif choice == "2":
            ask_question_interactive(rag)
        elif choice == "3":
            rag.display_stats()
        elif choice == "4":
            print("\n👋 Thanks for trying the RAG demo!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-4.")


def add_document_interactive(rag):
    """Interactive document addition."""
    print("\n📄 Add a New Document")
    print("-" * 25)
    
    title = input("Document title: ").strip()
    if not title:
        title = f"Document {len(rag.documents) + 1}"
    
    print("Document content (press Enter twice when done):")
    content_lines = []
    empty_line_count = 0
    
    while True:
        line = input()
        if line == "":
            empty_line_count += 1
            if empty_line_count >= 2:
                break
        else:
            empty_line_count = 0
            content_lines.append(line)
    
    content = "\n".join(content_lines).strip()
    
    if content:
        rag.add_document(content, title)
        print(f"✅ Added document '{title}'")
    else:
        print("❌ No content provided. Document not added.")


def ask_question_interactive(rag):
    """Interactive question asking."""
    print("\n❓ Ask a Question")
    print("-" * 18)
    
    if len(rag.documents) == 0:
        print("❌ No documents in knowledge base. Add some documents first!")
        return
    
    question = input("Your question: ").strip()
    
    if question:
        print(f"\n🔍 Searching for relevant information...")
        response = rag.generate_response(question)
        print(f"\n🤖 Answer:")
        print("-" * 8)
        print(response)
    else:
        print("❌ No question provided.")


def main():
    """Main function."""
    try:
        interactive_demo()
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted. Goodbye!")
    except Exception as e:
        print(f"\n💥 An error occurred: {e}")


if __name__ == "__main__":
    main()