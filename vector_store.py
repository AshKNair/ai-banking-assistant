"""
vector_store.py

Purpose:
Simple local in-memory vector store for RAG demonstration.

This stores documents together with their embeddings
and performs cosine similarity search.

Portfolio concept demonstrated:
local vector database pattern
retrieval layer abstraction
"""

import numpy as np


class LocalVectorStore:
    """
    Simple in-memory vector store.

    documents structure:
    [
        {
            "text": "...",
            "embedding": [...],
            "metadata": {...}
        }
    ]
    """

    def __init__(self):
        self.documents = []

    def add_document(self, text, embedding, metadata=None):
        """
        Add one embedded document into the vector store.
        """
        self.documents.append({
            "text": text,
            "embedding": embedding,
            "metadata": metadata
        })

    def clear(self):
        """
        Clear all stored documents.
        Useful when user uploads a new file.
        """
        self.documents = []

    def cosine_similarity(self, vec1, vec2):
        """
        Compute cosine similarity between two vectors.
        """
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)

        denominator = np.linalg.norm(vec1) * np.linalg.norm(vec2)

        if denominator == 0:
            return 0.0

        return float(np.dot(vec1, vec2) / denominator)

    def search(self, query_embedding, top_k=5):
        """
        Return top_k most similar documents.

        Output format:
        [
            {
                "similarity": 0.91,
                "text": "...",
                "embedding": [...],
                "metadata": {...}
            }
        ]
        """
        scored_results = []

        for doc in self.documents:
            similarity = self.cosine_similarity(
                query_embedding,
                doc["embedding"]
            )

            scored_results.append({
                "similarity": similarity,
                "text": doc["text"],
                "embedding": doc["embedding"],
                "metadata": doc["metadata"]
            })

        scored_results.sort(
            key=lambda x: x["similarity"],
            reverse=True
        )

        return scored_results[:top_k]