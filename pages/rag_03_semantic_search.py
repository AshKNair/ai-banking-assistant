"""
rag_03_semantic_search.py

Purpose:
Perform semantic similarity search on transaction data.

User question converted to embedding.
Similarity calculated against stored embeddings.

Portfolio concept demonstrated:
semantic search architecture
explainable retrieval layer
"""

import streamlit as st
import pandas as pd

from rag_pipeline import retrieve_relevant_transactions
from embedding_service import generate_embedding
from rag_pipeline import vector_store


# ---------------------------------------------------------
# page config
# ---------------------------------------------------------
st.set_page_config(
    page_title="RAG Semantic Search",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 RAG Semantic Search")
st.subheader("Retrieve relevant transactions using semantic similarity")


# ---------------------------------------------------------
# explanation
# ---------------------------------------------------------
st.markdown("""
Semantic search retrieves transactions based on meaning, not keywords.

Example:

Question:
"How much did I spend on transport?"

System retrieves:

Uber
Taxi
Fuel
Bus

Even if the exact word "transport" is not present.
""")


# ---------------------------------------------------------
# check session
# ---------------------------------------------------------
if "rag_source_data" not in st.session_state:

    st.warning("""
No dataset available.

Please first go to:

RAG Data Preparation page
""")

    st.stop()


df = st.session_state["rag_source_data"]


# ---------------------------------------------------------
# user input
# ---------------------------------------------------------
st.markdown("---")
st.header("Ask a question")

user_question = st.text_input(
    "Enter question",
    placeholder="Example: How much did I spend on food?"
)

top_k = st.slider(
    "Number of transactions to retrieve",
    min_value=1,
    max_value=10,
    value=5
)


# ---------------------------------------------------------
# search button
# ---------------------------------------------------------
if st.button("Retrieve relevant transactions"):

    if not user_question:

        st.warning("Please enter a question")
        st.stop()


    # -----------------------------------------------------
    # convert query to vector
    # -----------------------------------------------------
    query_embedding = generate_embedding(user_question)


    st.markdown("---")
    st.header("Query embedding vector")

    query_df = pd.DataFrame([query_embedding])

    st.write("""
User question converted into vector.
""")

    st.dataframe(query_df)


    # -----------------------------------------------------
    # retrieve matches
    # -----------------------------------------------------
    with st.spinner("Searching for relevant transactions..."):

        results = retrieve_relevant_transactions(
            user_question,
            top_k=top_k
        )


    # extract metadata
    retrieved_data = []

    for item in results:

        retrieved_data.append(
            item["metadata"]
        )


    results_df = pd.DataFrame(retrieved_data)


    st.success("Relevant transactions retrieved")


    # store for next page
    st.session_state["rag_retrieved_data"] = results_df
    st.session_state["rag_user_question"] = user_question


    # -----------------------------------------------------
    # show retrieved context
    # -----------------------------------------------------
    st.markdown("---")
    st.header("Retrieved transactions")

    st.dataframe(results_df)


    # -----------------------------------------------------
    # similarity scores
    # -----------------------------------------------------
    st.markdown("---")
    st.header("Similarity scores")

    similarity_scores = []

    for item in results:

        similarity_scores.append(
            item["similarity"]
        )


    similarity_df = pd.DataFrame({

        "description": results_df["description"],
        "similarity_score": similarity_scores

    })


    st.write("""
Higher score means stronger semantic match.
""")

    st.dataframe(similarity_df)



# ---------------------------------------------------------
# explanation
# ---------------------------------------------------------
st.markdown("---")
st.header("What happens in this step")

st.code(
"""
Step 1
User enters question

Step 2
Question converted to embedding vector

Step 3
Vector compared with stored vectors

Step 4
Similarity score calculated

Step 5
Top matching transactions returned

Step 6
Results passed to LLM
""",
language="text"
)


st.info("""
Explainability benefit:

User can see exactly which transactions
are passed to the AI model.

This reduces hallucination risk.
""")