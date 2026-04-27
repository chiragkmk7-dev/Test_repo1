import streamlit as st
import os

# ------------------------
# Simple Login Mechanism
# ------------------------
def login():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":  # change as needed
            st.session_state["logged_in"] = True
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials")

# ------------------------
# Main App
# ------------------------
def main_app():
    st.title("Environment Variables Viewer")

    env_vars = dict(os.environ)

    search_key = st.text_input("Search Environment Variable")

    if search_key:
        env_vars = {k: v for k, v in env_vars.items() if search_key.lower() in k.lower()}

    for key, value in env_vars.items():
        val_lower = value.lower()

        if val_lower == "true":
            st.markdown(f"<p style='color:green'><b>{key}</b> = {value}</p>", unsafe_allow_html=True)
        elif val_lower == "false":
            st.markdown(f"<p style='color:red'><b>{key}</b> = {value}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p><b>{key}</b> = {value}</p>", unsafe_allow_html=True)

# ------------------------
# App Flow Control
# ------------------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
else:
    main_app()
