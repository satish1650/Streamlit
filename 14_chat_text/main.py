import streamlit as st

# Basic usage
name = st.text_input("Enter your name:")

# Use entered value
if name:
    st.write(f"Hello, {name}! 👋")

# With a placeholder and password type
password = st.text_input("Enter password:", type="password", placeholder="••••••")
