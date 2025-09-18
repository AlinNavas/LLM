#!/usr/bin/env python3
"""
Simple test for the RAG demo to ensure it works correctly.
"""

import sys
import os

# Add the current directory to the path to import our demo
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from demo_rag_simple import SimpleRAGDemo


def test_rag_demo():
    """Test the basic functionality of the RAG demo."""
    print("🧪 Testing RAG Demo functionality...")
    
    # Initialize RAG system
    rag = SimpleRAGDemo()
    
    # Test document addition
    test_content = "This is a test document about artificial intelligence and machine learning."
    rag.add_document(test_content, "Test Document")
    
    assert len(rag.documents) == 1, "Document should be added"
    assert len(rag.chunks) > 0, "Chunks should be created"
    print("✅ Document addition test passed")
    
    # Test keyword extraction
    keywords = rag._extract_keywords("artificial intelligence machine learning")
    assert "artificial" in keywords, "Should extract 'artificial' as keyword"
    assert "intelligence" in keywords, "Should extract 'intelligence' as keyword"
    print("✅ Keyword extraction test passed")
    
    # Test search functionality
    relevant_chunks = rag.search_relevant_chunks("artificial intelligence")
    assert len(relevant_chunks) > 0, "Should find relevant chunks"
    print("✅ Search functionality test passed")
    
    # Test response generation
    response = rag.generate_response("What is artificial intelligence?")
    assert len(response) > 0, "Should generate a response"
    assert "artificial intelligence" in response.lower(), "Response should contain the query term"
    print("✅ Response generation test passed")
    
    print("🎉 All tests passed! RAG demo is working correctly.")
    return True


def test_empty_knowledge_base():
    """Test behavior with empty knowledge base."""
    print("🧪 Testing empty knowledge base behavior...")
    
    rag = SimpleRAGDemo()
    response = rag.generate_response("What is the meaning of life?")
    
    assert "don't have enough information" in response, "Should indicate lack of information"
    print("✅ Empty knowledge base test passed")


if __name__ == "__main__":
    try:
        test_rag_demo()
        test_empty_knowledge_base()
        print("\n🏆 All tests completed successfully!")
        sys.exit(0)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        sys.exit(1)