import streamlit as st
import os

st.title("Environment Variables Viewer")

st.write("Below are the environment variables available to this app:")

env_vars = dict(os.environ)

# Option to search for a specific variable
search_key = st.text_input("Search Environment Variable")

if search_key:
    filtered_vars = {k: v for k, v in env_vars.items() if search_key.lower() in k.lower()}
else:
    filtered_vars = env_vars

# Display variables
for key, value in filtered_vars.items():
    st.text(f"{key} = {value}")
