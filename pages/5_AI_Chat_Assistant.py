import streamlit as st
import pandas as pd
from openai import OpenAI
from security import check_access

check_access()

st.title("AI Chat Assistant")






    

st.markdown("""
### Conversational AI Assistant Capability

<div style="
background-color:#fff4f4;
padding:18px;
border-radius:10px;
border-left:6px solid #cc0000;
font-size:16px;
">

<b>What this assistant demonstrates:</b>

1️⃣ <b>Context-aware financial reasoning</b><br>
The assistant analyses structured transaction data to generate insights on spending behaviour, patterns, and risks.


2️⃣ <b>Conversational interaction pattern</b><br>
Each question builds on prior responses within the session, simulating how enterprise AI copilots support exploratory analysis.


3️⃣ <b>Combination of deterministic analytics + AI reasoning</b><br>
Structured data preparation is performed programmatically, while the LLM provides interpretation and recommendations.


<b>Example questions:</b>

• what categories cost me the most<br>
• how can I reduce expenses<br>
• where am I overspending

</div>
""", unsafe_allow_html=True)



# -------------------------
# LOAD DATA
# -------------------------

if "expenses_df" in st.session_state:

    expenses_df = st.session_state.expenses_df.copy()

    data_source = "Uploaded file"

else:

    df = pd.read_csv("transactions.csv", header=None)

    df.columns = ["date", "amount", "description", "balance"]

    df["amount"] = df["amount"].astype(float)

    expenses_df = df[df["amount"] < 0].copy()

    data_source = "Demo dataset"

    # store so other pages can reuse
    st.session_state.expenses_df = expenses_df


# -------------------------
# SHOW DATA SUMMARY
# -------------------------

total_spend = expenses_df["amount"].abs().sum()

st.markdown("---")

st.info(f"""
Dataset currently in use: {data_source} | Transactions analysed: {len(expenses_df)} | Total spending detected: ${total_spend:,.2f}
""")





transactions = expenses_df.to_dict(orient="records")

transaction_summary = "\n".join(

    [

        f"{row['date']} | {row['description']} | ${abs(row['amount'])}"

        for row in transactions

    ]

)

st.session_state.chat_transaction_summary = transaction_summary







# -------------------------
# CHAT MEMORY
# -------------------------

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

if "chat_last_prompt" not in st.session_state:
    st.session_state.chat_last_prompt = ""

if "chat_last_answer" not in st.session_state:
    st.session_state.chat_last_answer = ""


# -------------------------
# RESPONSE STYLE
# -------------------------

st.markdown("---")

instruction_option = st.selectbox(

    "Response style",

    [
        "Concise summary",
        "Detailed analysis",
        "Savings advice",
        "Spending insights",
        "Risk alerts"
    ]

)

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

selected_instruction = instruction_map[instruction_option]


# -------------------------
# DISPLAY CHAT HISTORY
# -------------------------

for msg in st.session_state.chat_messages:

    with st.chat_message(msg["role"]):

        st.write(msg["content"])


# -------------------------
# CHAT INPUT
# -------------------------

user_question = st.chat_input(
    "Ask something about your finances"
)

if user_question:

    # show user message immediately

    st.session_state.chat_messages.append(

        {
            "role": "user",
            "content": user_question
        }

    )

    with st.chat_message("user"):

        st.write(user_question)


    # -------------------------
    # BUILD CONVERSATION CONTEXT
    # -------------------------

    conversation_history = ""

    for msg in st.session_state.chat_messages:

        conversation_history += (

            f"{msg['role']}: {msg['content']}\n"

        )


    # -------------------------
    # BUILD PROMPT
    # -------------------------

    prompt = f"""

You are a helpful banking assistant.

Conversation so far:
{conversation_history}

Customer transaction data:
{transaction_summary}

Instruction:
{selected_instruction}

Respond clearly and helpfully.
"""


    st.session_state.chat_last_prompt = prompt


    # -------------------------
    # CALL OPENAI
    # -------------------------

    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    response = client.chat.completions.create(

        model="gpt-4o-mini",

        messages=[

            {
                "role": "system",
                "content":
                "You are a helpful banking assistant."
            },

            {
                "role": "user",
                "content": prompt
            }

        ]

    )


    ai_answer = response.choices[0].message.content


    st.session_state.chat_last_answer = ai_answer


    st.session_state.chat_messages.append(

        {
            "role": "assistant",
            "content": ai_answer
        }

    )


    with st.chat_message("assistant"):

        st.write(ai_answer)


# -------------------------
# CLEAR CHAT BUTTON
# -------------------------

if st.button("Clear chat"):

    st.session_state.chat_messages = []

    st.session_state.chat_last_prompt = ""

    st.session_state.chat_last_answer = ""

    st.rerun()