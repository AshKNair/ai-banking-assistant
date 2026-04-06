import streamlit as st
from security import check_access

check_access()

header_col1, header_col2 = st.columns([1,2])

with header_col1:

    st.image("profile.png", width=160)

    st.markdown("""
**Ashwin Nair**  
Lead Solution Architect  
AI & Cloud Transformation
""")

with header_col2:

    st.title("AI Powered Personal Finance Insights")

    st.markdown("""
### Architectural Evolution Demonstrated in this Solution

<div style="
background-color:#fff4f4;
padding:18px;
border-radius:10px;
border-left:6px solid #cc0000;
font-size:16px;
">

<b>Evolution of AI integration patterns:</b>

1️⃣ <b>Deterministic pipeline augmented with AI</b><br>
A structured workflow where application logic prepares business context and calls an LLM once to generate insights.

<br>

2️⃣ <b>Conversational AI orchestration using session memory</b><br>
An extension of the same architecture into a chat-based assistant that maintains conversational context across multiple interactions.

<br>

This demonstrates how enterprise solutions evolve from simple AI augmentation into context-aware AI copilots.

</div>
""", unsafe_allow_html=True)
    

st.markdown("---")

st.write(
"""
This demo demonstrates:

• AI integration patterns  
• deterministic vs probabilistic logic  
• layered architecture  
• prompt engineering  
"""
)