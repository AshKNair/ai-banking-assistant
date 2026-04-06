import streamlit as st
import matplotlib.pyplot as plt
from security import check_access

check_access()

st.title("Spending Insights")

st.markdown("""
This chart shows the top spending merchants based on transaction data.
Higher bars indicate higher total spend.
""")


if "expenses_df" not in st.session_state:

    st.warning("Run Single AI Call or AI Chat first.")
    st.stop()


df = st.session_state.expenses_df.copy()

df["abs_amount"] = df["amount"].abs()


merchant_spend = (

    df.groupby("description")["abs_amount"]

    .sum()

    .sort_values(ascending=True)

    .tail(10)

)


fig, ax = plt.subplots(figsize=(8,5))


merchant_spend.plot(

    kind="barh",

    ax=ax

)


ax.set_title("Top Spending Merchants")

ax.set_xlabel("Total Spend")

ax.set_ylabel("Merchant")


st.pyplot(fig, use_container_width=True)