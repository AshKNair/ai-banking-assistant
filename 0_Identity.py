import streamlit as st
from security import check_access


check_access()


st.set_page_config(layout="wide")

st.title("Identity")

st.success("Access granted")

st.write("Use the sidebar to explore the solution.")


# -------------------------
# SIGN OUT BUTTON
# -------------------------

st.markdown("---")

if st.button("Sign out / Switch user"):

    for key in list(st.session_state.keys()):
        del st.session_state[key]

    st.rerun()