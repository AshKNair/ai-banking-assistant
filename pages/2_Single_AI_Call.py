import streamlit as st
import pandas as pd
from security import check_access

check_access()

st.title("DEMO - SINGLE AI CALL")

# -------------------------
# FILE UPLOAD
# -------------------------

st.subheader("Upload financial dataset")

st.info("""
Upload a CSV file with columns:

date, amount, description, balance

Example:
2024-01-01, -25.40, Uber, 1200.50
""")

uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)


# store file in session
if uploaded_file is not None:

    st.session_state.uploaded_file = uploaded_file


# ensure file exists
if "uploaded_file" not in st.session_state:

    st.warning("Please upload a CSV file to continue.")
    st.stop()


# reset pointer before reading
st.session_state.uploaded_file.seek(0)

df = pd.read_csv(
    st.session_state.uploaded_file,
    header=None
)


df.columns = ["date", "amount", "description", "balance"]

df["amount"] = df["amount"].astype(float)

expenses_df = df[df["amount"] < 0]


# -------------------------
# CALCULATE TOTALS
# -------------------------

total_rows = len(df)

expense_rows = len(expenses_df)

total_spend = expenses_df["amount"].abs().sum()


# -------------------------
# SHOW SUMMARY
# -------------------------

st.markdown("### Dataset Summary")

st.info(f"""
Dataset loaded successfully

Total rows in file: {total_rows}

Expense transactions used: {expense_rows}

Total spending detected: ${total_spend:,.2f}
""")


# -------------------------
# STORE FOR OTHER PAGES
# -------------------------

transactions = expenses_df.to_dict(orient="records")

transaction_summary = "\n".join(

    [

        f"{row['date']} | {row['description']} | ${abs(row['amount'])}"

        for row in transactions

    ]

)

st.session_state.transaction_summary = transaction_summary

st.session_state.expenses_df = expenses_df

st.session_state.total_spend = total_spend


# -------------------------
# USER QUESTION
# -------------------------

user_input = st.text_input(
    "Ask about your finances"
)


instruction_option = st.selectbox(

    "Select response style",

    [

        "Concise summary",

        "Detailed analysis",

        "Savings advice",

        "Spending insights",

        "Risk alerts"

    ]

)


# -------------------------
# RUN AI
# -------------------------

if st.button("Run AI"):

    st.session_state.user_input = user_input

    st.session_state.instruction_option = instruction_option

    st.success("Input captured. Navigate to SINGLE AI RESPONSE page.")