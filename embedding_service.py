"""
embedding_service.py

Purpose:
Handles conversion of text into embeddings using OpenAI embedding models.

Why this file exists:
We separate embedding logic so we can later replace OpenAI embeddings
with Azure OpenAI embeddings or any enterprise embedding service
without changing the Streamlit pages.

Architectural concept demonstrated:
Loose coupling between AI services and application UI.
"""

from openai import OpenAI
import os


# Create OpenAI client
# Make sure your OPENAI_API_KEY is set as environment variable
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_embedding(text):
    """
    Convert input text into embedding vector.

    Embeddings allow semantic comparison between text.
    Example:
    "Uber ride" and "Taxi trip" will produce similar vectors.

    Parameters:
    text (str) : input text to convert into embedding

    Returns:
    list[float] : embedding vector
    """

    response = client.embeddings.create(
        model="text-embedding-3-small",  # cost-effective and high quality
        input=text
    )

    return response.data[0].embedding