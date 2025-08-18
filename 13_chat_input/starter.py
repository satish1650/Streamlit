import streamlit as st

user_input = st.chat_input(placeholder="Please enter input here...")
if user_input:
    print(st.write(f"Your input is \n", {user_input}))
