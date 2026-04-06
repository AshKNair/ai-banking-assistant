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
"Architecture demonstrates progression from one-time AI call to conversational AI system."

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

"Retrieval Augmented Generation (RAG)":
"AI retrieves only relevant financial records before generating answer. Improves accuracy and reduces prompt size.",

"Vector embeddings for semantic search":
"Text converted into numerical vectors enabling meaning-based search. Example: Uber ride and Taxi trip recognised as similar.",

"AI-powered document ingestion":
"Ability to upload documents (PDF, text) and convert them into AI-readable format.",

"PDF bank statement parsing":
"Extract transaction data automatically from uploaded bank statement PDFs.",

"Multi-file financial comparison":
"Compare spending behaviour across multiple uploaded financial files.",

"AI anomaly detection patterns":
"AI identifies unusual or abnormal spending behaviour based on context.",

"Prompt optimisation experiments":
"Experimenting with different prompt structures to improve AI accuracy and consistency.",

"Domain-tuned financial reasoning":
"Refining prompts specifically for financial analysis scenarios.",

"Hybrid deterministic + AI decisions":
"Combining traditional business rules with AI-based reasoning.",

"Multi-model evaluation":
"Comparing outputs from different AI models to assess strengths and differences.",

"Expanded conversational memory":
"Enhancing chat assistant to remember longer context across interactions.",

"Semantic financial categorisation":
"AI automatically groups transactions into categories based on meaning instead of keywords."

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

This is an evolving AI portfolio project focused specifically on applied AI patterns
relevant to Solution Architecture roles.

Enhancements will continue to prioritise practical enterprise use cases.

""")