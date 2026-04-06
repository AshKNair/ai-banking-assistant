import streamlit as st
from security import check_access

check_access()

st.title("AI Capabilities Demonstrated")

st.markdown("""
This portfolio project demonstrates practical AI integration patterns
applied to a financial insights use case.

Architecture evolution demonstrated in this solution:

• Deterministic pipeline augmented with AI  
• Conversational orchestration using session memory  
• Retrieval Augmented Generation (RAG) for grounded AI responses  

The focus is on real-world enterprise applicability rather than experimental complexity.
""")

st.markdown("---")

st.subheader("AI Capabilities Implemented")

implemented = {

"Prompt Engineering with structured context":
"Designing structured instructions to guide AI behaviour consistently. Example: defining role, context data and expected output style.",

"Deterministic pipeline feeding AI":
"Traditional logic prepares structured financial data before sending to AI. Example: filtering debit transactions before analysis.",

"Role-based AI behaviour design":
"AI behaviour controlled by defining a role. Example: instructing AI to act as a banking assistant.",

"Instruction-controlled responses":
"User selects response style which changes AI output format. Example: concise summary vs detailed analysis.",

"Single-turn AI analysis workflow":
"One-time AI request analysing uploaded financial dataset.",

"Conversational AI orchestration":
"AI chat interface enabling follow-up questions based on same dataset.",

"Session-based context memory":
"Application remembers uploaded data and previous context within the session.",

"Structured dataset grounding":
"AI responses grounded using structured transaction dataset rather than generic responses.",

"Reusable prompt templates":
"Consistent prompt structure reused across interactions.",

"Human-in-the-loop refinement":
"User refines questions iteratively to improve AI output quality.",

"Financial behaviour interpretation":
"AI identifies spending patterns and insights from transaction history.",

"Evolution from single-call to chat AI":
"Architecture demonstrates progression from one-time AI call to conversational AI system.",

"Retrieval Augmented Generation (RAG)":
"System retrieves only relevant transactions before sending prompt to LLM, improving accuracy and reducing token usage.",

"Vector embeddings for semantic search":
"Transaction descriptions converted into embeddings enabling similarity-based retrieval (e.g. Uber ≈ Taxi).",

"Semantic search architecture":
"User questions converted to embeddings and matched against stored vectors to retrieve relevant financial records.",

"Token optimisation strategy":
"Reduced token usage by limiting context to only relevant retrieved transactions rather than entire dataset.",

"Explainable AI grounding":
"Application shows retrieved context and prompt input, improving transparency and trust in AI responses.",

"Separation of retrieval and generation layers":
"Architecture demonstrates modular separation between vector search and LLM response generation.",

"Hybrid deterministic + AI workflow":
"Business logic controls what data is sent to AI, improving reliability and reducing hallucination risk."

}


cols = st.columns(3)

for i, (skill, tip) in enumerate(implemented.items()):

    cols[i % 3].markdown(f"""
    <div title="{tip}"
    style="
        border:1px solid #4CAF50;
        background-color:#f8fff8;
        padding:12px;
        border-radius:10px;
        margin-bottom:12px;
        font-size:14px;
        cursor:help;
    ">
    ✅ {skill}
    </div>
    """, unsafe_allow_html=True)



st.markdown("---")

st.subheader("Planned AI Enhancements")

planned = {

"AI-powered document ingestion":
"Ability to upload documents (PDF, text) and convert them into AI-readable format.",

"PDF bank statement parsing":
"Extract transaction data automatically from uploaded bank statement PDFs.",

"Multi-file financial comparison":
"Compare spending behaviour across multiple uploaded financial files.",

"AI anomaly detection patterns":
"AI identifies unusual or abnormal spending behaviour based on context.",

"Multi-model evaluation":
"Comparing outputs from different AI models to assess strengths and differences.",

"Expanded conversational memory":
"Enhancing chat assistant to remember longer context across interactions.",

"Semantic financial categorisation":
"AI automatically groups transactions into categories based on meaning instead of keywords.",

"Cloud-hosted vector database":
"Replace in-memory vector store with enterprise-grade vector DB (Azure AI Search, Pinecone, pgvector).",

"Secure enterprise data ingestion":
"Integration with enterprise data sources via APIs or secure storage services.",

"LLM guardrails and policy enforcement":
"Apply structured safety controls for enterprise-grade AI usage.",

"Cost monitoring and token analytics dashboard":
"Track token usage trends for cost optimisation and governance.",

"Evaluation framework for prompt performance":
"Systematically assess response quality using defined evaluation metrics."

}


cols2 = st.columns(3)

for i, (skill, tip) in enumerate(planned.items()):

    cols2[i % 3].markdown(f"""
    <div title="{tip}"
    style="
        border:1px solid #7b61ff;
        background-color:#f6f4ff;
        padding:12px;
        border-radius:10px;
        margin-bottom:12px;
        font-size:14px;
        cursor:help;
    ">
    🔜 {skill}
    </div>
    """, unsafe_allow_html=True)



st.markdown("---")

st.info("""

Hover over each capability to view explanation and examples.

This portfolio project demonstrates applied AI architecture patterns
relevant to enterprise solution design roles.

Focus areas:

• reliable AI integration patterns  
• grounded AI decision flows  
• explainable prompt design  
• token-efficient architecture  
• modular AI orchestration  

Future enhancements will prioritise enterprise scalability patterns.

""")