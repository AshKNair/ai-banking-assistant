"""
rag_pipeline.py

Purpose:
Coordinates embedding generation and vector search.

Acts as orchestration layer for RAG.

Architectural concept:
Separates orchestration logic from UI layer.
"""

from embedding_service import generate_embedding
from vector_store import LocalVectorStore


# global vector store instance
vector_store = LocalVectorStore()


def prepare_embeddings(dataframe):
    """
    Generate embeddings for each transaction description.

    dataframe expected columns:
    date
    description
    amount
    balance
    """

    # clear old vectors before loading a new dataset
    vector_store.clear()

    for _, row in dataframe.iterrows():

        description = str(row["description"])
        embedding = generate_embedding(description)

        metadata = {
            "date": row["date"],
            "amount": row["amount"],
            "balance": row["balance"],
            "description": description
        }

        vector_store.add_document(
            text=description,
            embedding=embedding,
            metadata=metadata
        )


def retrieve_relevant_transactions(query, top_k=5):
    """
    Retrieve semantically relevant transactions.
    """
    query_embedding = generate_embedding(query)

    results = vector_store.search(
        query_embedding,
        top_k=top_k
    )

    return results