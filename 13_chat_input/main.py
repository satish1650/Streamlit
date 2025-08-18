import streamlit as st

if user_input := st.chat_input(placeholder="Please enter input here..."):
    print(st.write(f"Your input is \n", {user_input}))
