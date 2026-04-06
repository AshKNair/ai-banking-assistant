import streamlit as st
from openai import OpenAI
from security import check_access

check_access()

st.title("DEMO - SINGLE AI RESPONSE")


if "transaction_summary" not in st.session_state:

    st.warning("Please upload dataset and run SINGLE AI CALL first.")
    st.stop()


client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

instruction_map = {

    "Concise summary":
    "Provide a short and clear summary of the user's spending.",

    "Detailed analysis":
    "Provide detailed financial analysis including patterns and observations.",

    "Savings advice":
    "Suggest practical ways the user can reduce spending and save money.",

    "Spending insights":
    "Identify spending behaviour patterns and highlight key categories.",

    "Risk alerts":
    "Identify any unusual or potentially risky spending behaviour."
}


prompt = f"""
You are a helpful banking assistant.

Total calculated spending:
${st.session_state.total_spend:,.2f}

User question:
{st.session_state.user_input}

Customer transaction data:
{st.session_state.transaction_summary}

Instruction:
{instruction_map[st.session_state.instruction_option]}

"""


st.markdown(
    "<h4 style='color:#4CAF50;'>Prompt sent to AI</h4>",
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="
        border:1px solid #4CAF50;
        background-color:#f9fff9;
        padding:15px;
        border-radius:8px;
        height:400px;
        overflow-y:auto;
        font-family: monospace;
        font-size:13px;
        white-space: pre-wrap;
    ">
    {prompt}
    </div>
    """,
    unsafe_allow_html=True
)


st.subheader("AI Answer")

with st.spinner("Generating financial insights..."):

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[

            {

                "role":"user",

                "content":prompt

            }

        ]

    )

answer = response.choices[0].message.content

st.write(answer)


# -------------------------
# token usage display
# -------------------------
st.markdown("---")

st.info(f"""
Token usage

Prompt tokens: {response.usage.prompt_tokens} |
Completion tokens: {response.usage.completion_tokens} |
Total tokens: {response.usage.total_tokens}
""")