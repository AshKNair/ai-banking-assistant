"""
rag_01_pipeline_explainer.py

Purpose:
This page explains the Retrieval Augmented Generation (RAG) architecture
used in the AI Financial Insights Assistant portfolio project.

Why this page exists:
A Solution Architect should not only build AI-enabled features,
but also clearly explain the architecture pattern to stakeholders,
interviewers, project teams, and decision-makers.

This page is intentionally explanatory.
It does not execute RAG logic.
It helps the viewer understand:

1. Why standard prompting has limitations
2. What RAG adds to the architecture
3. How the data flows through the solution
4. Why this pattern is more scalable and enterprise-friendly

Portfolio value demonstrated:
- AI architecture communication
- Explainable AI design
- Enterprise AI pattern awareness
- Controlled evolution from basic AI to grounded AI
"""

import streamlit as st
from security import check_access

check_access()


# -------------------------------------------------------------
# Page configuration
# -------------------------------------------------------------
st.set_page_config(
    page_title="RAG Pipeline Explainer",
    page_icon="🧠",
    layout="wide"
)


# -------------------------------------------------------------
# Page title and introduction
# -------------------------------------------------------------
st.title("🧠 RAG Pipeline Explainer")
st.subheader("Retrieval Augmented Generation in the AI Financial Insights Assistant")


st.markdown("""
This page explains how the application evolves from a **basic AI prompt pattern**
to a more scalable and reliable **Retrieval Augmented Generation (RAG)** architecture.

In the earlier pages of this portfolio project, the AI model was given pre-prepared
transaction context directly in the prompt. That works well for small datasets.

However, as the dataset grows, sending all records to the model becomes inefficient.
This introduces several architectural concerns:

- higher token usage
- higher cost
- lower scalability
- greater risk of irrelevant context
- more chance of weak or noisy answers

RAG solves this by retrieving only the **most relevant data first**,
then sending that filtered data to the model.
""")


# -------------------------------------------------------------
# Section 1 - Problem statement
# -------------------------------------------------------------
st.markdown("---")
st.header("1. Why basic prompting is not enough")


col1, col2 = st.columns(2)

with col1:
    st.markdown("### Basic Prompting Approach")
    st.info("""
    In a simple AI workflow:

    - User uploads transaction data
    - Application prepares a summary
    - Entire or large portions of the dataset are added to the prompt
    - LLM generates a response

    This is acceptable for smaller data volumes,
    but becomes inefficient as the dataset grows.
    """)

with col2:
    st.markdown("### Common Limitations")
    st.warning("""
    Problems with large prompt-based grounding:

    - Too much irrelevant context
    - Prompt size grows quickly
    - Cost increases with token usage
    - Model focus may weaken
    - Harder to scale to enterprise datasets
    """)


# -------------------------------------------------------------
# Section 2 - What RAG is
# -------------------------------------------------------------
st.markdown("---")
st.header("2. What RAG adds to the architecture")


st.markdown("""
**Retrieval Augmented Generation (RAG)** is an architecture pattern where the system:

1. stores data in a searchable semantic form
2. converts the user query into an embedding
3. retrieves only the most relevant records
4. injects those retrieved results into the final prompt
5. asks the language model to answer using grounded context

This means the language model is no longer asked to reason over everything.
Instead, it reasons over **only the most relevant information**.
""")


st.success("""
Key idea:
The retrieval layer improves grounding before the generation layer begins.
""")


# -------------------------------------------------------------
# Section 3 - RAG pipeline flow
# -------------------------------------------------------------
st.markdown("---")
st.header("3. RAG pipeline flow")


st.code(
    """
Step A  -> User uploads transaction CSV
Step B  -> Application reads and validates data
Step C  -> Transaction descriptions are converted into embeddings
Step D  -> Embeddings are stored in a vector store
Step E  -> User asks a natural language question
Step F  -> User question is converted into an embedding
Step G  -> Similarity search finds the most relevant transactions
Step H  -> Retrieved transactions are added to the prompt
Step I  -> LLM generates a grounded response
Step J  -> User receives a more relevant and scalable answer
    """,
    language="text"
)


st.markdown("### Simplified architecture view")

st.code(
    """
CSV Transactions
      ↓
Deterministic preprocessing
      ↓
Embedding generation
      ↓
Vector storage
      ↓
User question
      ↓
Query embedding
      ↓
Semantic similarity search
      ↓
Relevant transactions retrieved
      ↓
Augmented prompt construction
      ↓
LLM grounded response
    """,
    language="text"
)


# -------------------------------------------------------------
# Section 4 - Explain components
# -------------------------------------------------------------
st.markdown("---")
st.header("4. Architecture components")


with st.expander("Embedding Service"):
    st.markdown("""
An embedding service converts text into a numeric vector representation.

Example:

- **'Uber ride'**
- **'Taxi trip'**

These may have different words, but embeddings allow the system
to identify that they are semantically similar.

In this project, the embedding service is separated into its own file
so that the implementation can later be upgraded from a simple API-based model
to a managed enterprise service such as **Azure OpenAI Embeddings**.
    """)

with st.expander("Vector Store"):
    st.markdown("""
A vector store is used to save embeddings and later search them by similarity.

In the initial implementation of this portfolio project, a local in-memory
or lightweight storage pattern is used for simplicity.

Later, this can be replaced with an enterprise-grade vector platform such as:

- Azure AI Search
- PostgreSQL with pgvector
- Pinecone
- Weaviate

The important architectural point is that the retrieval layer is designed
to be replaceable without changing the Streamlit UI pages.
    """)

with st.expander("Similarity Search"):
    st.markdown("""
Similarity search compares the embedding of the user's question
against the embeddings of stored transaction descriptions.

Instead of searching by exact keyword, the system searches by meaning.

Example question:

**'How much did I spend on transport?'**

Possible retrieved transactions:

- Uber
- Taxi
- Bus
- Train
- Fuel

Even if the word **transport** does not exist in the transaction descriptions,
the semantic search can still identify relevant records.
    """)

with st.expander("LLM Response Layer"):
    st.markdown("""
After retrieval, only the most relevant transactions are added to the prompt.

This has several advantages:

- reduces prompt size
- improves relevance
- lowers token cost
- reduces noise
- improves explainability

The language model is still important,
but its reasoning is now better grounded by a retrieval step.
    """)


# -------------------------------------------------------------
# Section 5 - Compare standard AI vs RAG
# -------------------------------------------------------------
st.markdown("---")
st.header("5. Standard AI vs RAG-enhanced AI")


comparison_col1, comparison_col2 = st.columns(2)

with comparison_col1:
    st.markdown("### Standard AI Pattern")
    st.markdown("""
- deterministic preprocessing
- static prompt grounding
- suitable for small datasets
- easier to start with
- limited scalability
- context may become too large
    """)

with comparison_col2:
    st.markdown("### RAG-Enhanced Pattern")
    st.markdown("""
- deterministic preprocessing
- semantic retrieval before prompt generation
- better scalability
- more selective grounding
- lower token usage
- more enterprise-aligned design
    """)


# -------------------------------------------------------------
# Section 6 - Why this matters in enterprise architecture
# -------------------------------------------------------------
st.markdown("---")
st.header("6. Why this matters in enterprise architecture")


st.markdown("""
RAG is a common enterprise AI pattern because it helps balance:

- accuracy
- scalability
- explainability
- operational cost
- architectural control

This pattern is highly relevant in domains such as:

- banking
- insurance
- government
- legal
- healthcare

In those environments, AI cannot simply generate answers from broad prompts.
It must be guided using trusted, relevant, and auditable data.
""")


# -------------------------------------------------------------
# Section 7 - Portfolio positioning
# -------------------------------------------------------------
st.markdown("---")
st.header("7. What this page demonstrates in the portfolio")


st.markdown("""
This page demonstrates that the project is not just using AI casually.

It shows deliberate architectural evolution:

- **Single AI call pattern**
- **Conversational AI pattern**
- **Shared analytics support**
- **RAG architecture pattern**

This is important because enterprise interviewers usually want to see:

- how you structure AI solutions
- how you separate concerns
- how you reduce hallucination risk
- how you design for future scalability
""")


# -------------------------------------------------------------
# Section 8 - Implementation note
# -------------------------------------------------------------
st.markdown("---")
st.header("8. Implementation strategy used in this project")


st.info("""
Implementation approach for this portfolio project:

1. Start with a simple local RAG implementation
2. Keep code modular and replaceable
3. Separate embedding, vector storage, and orchestration logic
4. Later upgrade the same design to enterprise services

This means the current local implementation is not a dead-end prototype.
It is the first step in an extensible architecture.
""")


# -------------------------------------------------------------
# Footer note
# -------------------------------------------------------------
st.markdown("---")
st.caption(
    "Portfolio note: This page explains the RAG architecture pattern. "
    "The actual implementation continues in the next RAG pages."
)