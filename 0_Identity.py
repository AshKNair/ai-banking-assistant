import streamlit as st

ACCESS_CODE = "demo"

def check_access():

    if "access_granted" not in st.session_state:
        st.session_state.access_granted = False

    if not st.session_state.access_granted:

        st.set_page_config(layout="centered")

        st.title("AI Powered Personal Finance Insights")

        password = st.text_input(
            "Enter access code:",
            type="password"
        )

        if st.button("Enter Demo"):

            if password == ACCESS_CODE:

                st.session_state.access_granted = True
                st.rerun()

            else:

                st.error("Incorrect code")

        st.stop()

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

    # clear everything from session
    for key in list(st.session_state.keys()):
        del st.session_state[key]

    st.rerun()