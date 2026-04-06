import streamlit as st

ACCESS_CODE = "demo"

def check_access():

    if "access_granted" not in st.session_state:
        st.session_state.access_granted = False

    if not st.session_state.access_granted:

        st.title("SmartSpend AI – Restricted Demo")

        password = st.text_input(
            "Enter access code",
            type="password"
        )

        if st.button("Enter"):

            if password == ACCESS_CODE:

                st.session_state.access_granted = True
                st.rerun()

            else:

                st.error("Incorrect code")

        st.stop()