"""
rag_02_data_preparation.py

Purpose:
Prepare dataset for Retrieval Augmented Generation (RAG).

User uploads transaction CSV.
System generates embeddings for each transaction description.
Embeddings stored in vector store.

Portfolio concept demonstrated:
AI data preparation pipeline
"""

import streamlit as st
import pandas as pd

from rag_pipeline import prepare_embeddings, vector_store


# ---------------------------------------------------------
# Page config
# ---------------------------------------------------------
st.set_page_config(
    page_title="RAG Data Preparation",
    page_icon="📊",
    layout="wide"
)

st.title("📊 RAG Data Preparation")
st.subheader("Generate embeddings for transaction descriptions")


# ---------------------------------------------------------
# Explanation
# ---------------------------------------------------------
st.markdown("""
This step prepares the dataset for Retrieval Augmented Generation (RAG).

Each transaction description is converted into a vector embedding.

Embeddings allow semantic similarity search.

Example:

"Uber trip"
"Taxi ride"

Even though wording differs, embeddings recognise similar meaning.
""")


# ---------------------------------------------------------
# File upload
# ---------------------------------------------------------
st.markdown("---")
st.header("Upload transaction dataset")

uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)


# ---------------------------------------------------------
# Expected structure
# ---------------------------------------------------------
EXPECTED_COLUMNS = [
    "date",
    "description",
    "amount",
    "balance"
]


if uploaded_file:

    df = pd.read_csv(uploaded_file, header=None)

    # assign column names
    df.columns = [
        "date",
        "amount",
        "description",
        "balance"
    ]

    st.success("File uploaded successfully")

    st.write("Preview of uploaded dataset")
    st.dataframe(df.head())


    # -----------------------------------------------------
    # convert types
    # -----------------------------------------------------
    st.markdown("---")
    st.header("Data preparation")

    df["description"] = df["description"].astype(str)

    try:

        df["amount"] = pd.to_numeric(
            df["amount"],
            errors="coerce"
        )

        df["balance"] = pd.to_numeric(
            df["balance"],
            errors="coerce"
        )

    except Exception as e:

        st.error(f"Numeric conversion failed: {e}")
        st.stop()


    # -----------------------------------------------------
    # keep only expenses
    # -----------------------------------------------------
    df = df[df["amount"] < 0]

    st.info(
        f"{len(df)} expense transactions retained"
    )


    # -----------------------------------------------------
    # generate embeddings
    # -----------------------------------------------------
    st.markdown("---")
    st.header("Generate embeddings")

    if st.button("Generate embeddings"):

        with st.spinner("Generating embeddings..."):

            prepare_embeddings(df)

        st.success("Embeddings generated successfully")

        # store original dataset
        st.session_state["rag_source_data"] = df


        # -------------------------------------------------
        # SHOW EMBEDDINGS
        # -------------------------------------------------
        st.markdown("---")
        st.header("Preview of vector embeddings")

        preview_vectors = [doc["embedding"] for doc in vector_store.documents[:5]]

        embedding_df = pd.DataFrame(preview_vectors)

        st.write("""
        Each row below is a vector representation of a transaction description.

        These numbers capture semantic meaning mathematically.
        """)

        st.dataframe(embedding_df)


        st.info("""
Dataset ready.

Next step:

Go to RAG Semantic Search page.
""")



# ---------------------------------------------------------
# explanation
# ---------------------------------------------------------
st.markdown("---")
st.header("What happens in this step")

st.code(
"""
Step 1
CSV uploaded

Step 2
Descriptions extracted

Step 3
Descriptions converted to embeddings

Step 4
Embeddings stored in vector store

Step 5
Vectors used later for similarity search
""",
language="text"
)


st.info("""
In enterprise architecture this layer is typically implemented using:

Azure AI Search |
Pinecone |
Weaviate |
PostgreSQL pgvector

Current implementation is simplified for demonstration.
""")