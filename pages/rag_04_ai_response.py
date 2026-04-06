"""
rag_04_ai_response.py

Purpose:
Generate the final AI response in the RAG pipeline.

This page takes:
1. the user's question
2. the semantically retrieved transactions

It then builds an augmented prompt and sends only the relevant
grounding context to the LLM.

Why this page matters:
This is the "Generation" part of Retrieval Augmented Generation (RAG).

Portfolio concepts demonstrated:
- grounded AI response generation
- prompt augmentation
- controlled AI orchestration
- explainable AI design
- modular separation between retrieval and generation
"""

import streamlit as st
import pandas as pd
from openai import OpenAI
from security import check_access

check_access()


# ---------------------------------------------------------
# OpenAI client
# ---------------------------------------------------------
# Assumes OPENAI_API_KEY is already configured in environment variables
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---------------------------------------------------------
# Page config
# ---------------------------------------------------------
st.set_page_config(
    page_title="RAG AI Response",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 RAG AI Response")
st.subheader("Generate grounded AI insights using retrieved transaction context")


# ---------------------------------------------------------
# Validate required session state
# ---------------------------------------------------------
if "rag_retrieved_data" not in st.session_state or "rag_user_question" not in st.session_state:
    st.warning("""
No retrieved RAG context found.

Please complete the earlier steps first:

1. RAG Data Preparation
2. RAG Semantic Search
""")
    st.stop()


retrieved_df = st.session_state["rag_retrieved_data"]
user_question = st.session_state["rag_user_question"]


# ---------------------------------------------------------
# Helper function: convert retrieved dataframe into prompt context
# ---------------------------------------------------------
def build_transaction_context(dataframe: pd.DataFrame) -> str:
    """
    Convert retrieved transactions into a compact text block
    for prompt grounding.

    This creates a readable, structured context for the LLM.
    """

    if dataframe.empty:
        return "No relevant transactions were retrieved."

    lines = []

    for _, row in dataframe.iterrows():
        line = (
            f"Date: {row.get('date', '')}, "
            f"Description: {row.get('description', '')}, "
            f"Amount: {row.get('amount', '')}, "
            f"Balance: {row.get('balance', '')}"
        )
        lines.append(line)

    return "\n".join(lines)


def generate_rag_response(question: str, context_text: str) -> str:
    """
    Generate grounded AI response using retrieved transactions only.

    The model is instructed to use the supplied context and avoid
    inventing unsupported facts.
    """

    system_prompt = """
You are a financial insights assistant.

Your job is to analyse financial transaction data and answer the user's question.

Important behaviour rules:
- Use only the retrieved transaction context provided.
- Do not make up facts that are not supported by the context.
- If the context is insufficient, say that clearly.
- Keep the answer practical, concise, and easy to understand.
- Where useful, mention patterns, possible spending categories, and observations.
- If the user asks for totals or patterns, reason only from the provided rows.
"""

    user_prompt = f"""
User question:
{question}

Retrieved transaction context:
{context_text}

Instructions:
Answer the user's question using only the retrieved transaction context above.
If the context is partial or insufficient, clearly mention that your answer is based only on the retrieved transactions.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )

    return {
        "answer": response.choices[0].message.content,
        "usage": response.usage
    }


# ---------------------------------------------------------
# Page explanation
# ---------------------------------------------------------
st.markdown("""
This page demonstrates the **generation layer** of the RAG pipeline.

At this stage:

- the user question has already been captured
- semantic search has already retrieved relevant transactions
- only those retrieved rows are added to the prompt
- the language model generates a grounded answer

This is different from sending the full dataset to the model.
It improves relevance, reduces prompt size, and makes the design
more scalable for enterprise-style use cases.
""")


# ---------------------------------------------------------
# Show user question
# ---------------------------------------------------------
st.markdown("---")
st.header("User question")
st.write(user_question)


# ---------------------------------------------------------
# Show retrieved context
# ---------------------------------------------------------
st.markdown("---")
st.header("Retrieved grounding context")
st.dataframe(retrieved_df)


# ---------------------------------------------------------
# Build FULL PROMPT
# ---------------------------------------------------------

context_text = build_transaction_context(retrieved_df)

full_prompt = f"""
SYSTEM ROLE:
You are a financial assistant AI.
Answer questions about transaction behaviour.

USER QUESTION:
{user_question}

RETRIEVED TRANSACTION CONTEXT:
{context_text}

INSTRUCTIONS:
Only use the transactions above.
If information is incomplete, clearly state assumptions.
Do not fabricate data.
Explain calculations clearly.
"""

with st.expander("View FULL prompt sent to the model"):
    st.code(full_prompt, language="text")


# ---------------------------------------------------------
# Generate response
# ---------------------------------------------------------
st.markdown("---")
st.header("Generate AI response")

if st.button("Generate grounded response"):
    with st.spinner("Generating AI response..."):
        try:
            result = generate_rag_response(user_question, context_text)

            st.session_state["rag_final_answer"] = result["answer"]
            st.session_state["rag_token_usage"] = result["usage"]
        except Exception as e:
            st.error(f"AI response generation failed: {e}")
            st.stop()


# ---------------------------------------------------------
# Display final response
# ---------------------------------------------------------
if "rag_final_answer" in st.session_state:
    st.markdown("---")
    st.header("Grounded AI response")
    st.write(st.session_state["rag_final_answer"])

    st.markdown("---")

    st.info(f"""
    Token usage (RAG optimised)

    Prompt tokens: {st.session_state["rag_token_usage"].prompt_tokens} |
    Completion tokens: {st.session_state["rag_token_usage"].completion_tokens} |
    Total tokens: {st.session_state["rag_token_usage"].total_tokens}
    """)


# ---------------------------------------------------------
# Architecture explanation
# ---------------------------------------------------------
st.markdown("---")
st.header("What happens in this step")

st.code(
    """
Step 1
Take the user question captured in the search step

Step 2
Take the retrieved transactions from the retrieval step

Step 3
Convert retrieved rows into structured prompt context

Step 4
Send question + retrieved context to the LLM

Step 5
Generate grounded financial insight response

Step 6
Display final answer to the user
    """,
    language="text"
)


# ---------------------------------------------------------
# Why this matters
# ---------------------------------------------------------
st.markdown("---")
st.info("""
Architecture value of this step:

- the LLM is grounded using retrieved context
- full dataset does not need to be sent every time
- prompt size is smaller and more targeted
- design is more scalable than naive prompting
- retrieval and generation remain separate concerns

This is the key value of Retrieval Augmented Generation (RAG).
""")


# ---------------------------------------------------------
# Portfolio positioning
# ---------------------------------------------------------
st.markdown("---")
st.success("""
Portfolio positioning:

This page demonstrates how a Solution Architect can combine:

- deterministic preprocessing
- embeddings
- vector retrieval
- prompt augmentation
- grounded response generation

into a modular AI-enabled application design.
""")