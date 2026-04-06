import streamlit as st
import pandas as pd
from security import check_access

check_access()

st.title("AI Execution Architecture")

st.markdown("""
This page illustrates how AI is integrated into the solution using two architectural patterns:

• Single interaction AI call  
• Conversational AI assistant  

The comparison shows how systems evolve from simple AI augmentation to context-aware AI copilots.
""")


# -------------------------
# SINGLE AI CALL
# -------------------------

st.markdown("## Pattern 1 — Single AI Call")

single_ai_table = [

    ["User submits query", "UI Layer", "No"],

    ["Load CSV financial data", "Data Layer", "No"],

    ["Aggregate spending", "Service Layer", "No"],

    ["Generate graphs", "Analytics Layer", "No"],

    ["Construct prompt with business context",
     "AI Integration Layer",
     "Yes"],

    ["Call OpenAI API",
     "External AI Service",
     "Yes"],

    ["Receive AI response",
     "Integration Layer",
     "Yes"],

    ["Format insights",
     "Service Layer",
     "No"],

    ["Display results",
     "UI Layer",
     "No"]

]

df_single = pd.DataFrame(

    single_ai_table,

    columns=["Step", "Component", "Uses AI"]

)


def highlight_ai(row):

    if row["Uses AI"] == "Yes":

        return ["background-color:#ffe6e6"] * 3

    return [""] * 3


st.dataframe(

    df_single.style.apply(highlight_ai, axis=1),

    use_container_width=True

)

st.markdown("---")

# -------------------------
# CONVERSATIONAL AI
# -------------------------

st.markdown("## Pattern 2 — Conversational AI Assistant")

chat_ai_table = [

    ["User enters message",
     "Chat UI",
     "No"],

    ["Store message in session memory",
     "Conversation Layer",
     "No"],

    ["Load financial transactions",
     "Data Layer",
     "No"],

    ["Aggregate spending data",
     "Service Layer",
     "No"],

    ["Construct prompt with conversation history",
     "AI Orchestration Layer",
     "Yes"],

    ["Send request to OpenAI",
     "External AI Service",
     "Yes"],

    ["Receive AI response",
     "AI Integration Layer",
     "Yes"],

    ["Store assistant response in memory",
     "Conversation Layer",
     "No"],

    ["Display chat response",
     "UI Layer",
     "No"]

]


df_chat = pd.DataFrame(

    chat_ai_table,

    columns=["Step", "Component", "Uses AI"]

)


st.dataframe(

    df_chat.style.apply(highlight_ai, axis=1),

    use_container_width=True

)