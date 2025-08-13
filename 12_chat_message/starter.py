import streamlit as st

st.title("Simple Chat Example")

# # st.chat_message() without with
# st.chat_message("User")
# st.write("How are you?")
# st.chat_message("assistant")
# st.write("I'm doing great! How can I help you today?")

# # st.chat_message() using with
# # User message bubble
with st.chat_message("user"):
    st.write("Hello, How are you?")

# Assistant message bubble
with st.chat_message("assistant"):
    st.write("I'm doing great! How can I help you today?")

# User message bubble
with st.chat_message("user"):
    st.write("Hello, What is Streamlit?")

# Assistant message bubble
with st.chat_message("assistant"):
    st.write("""Streamlit is an open-source Python library that simplifies the creation and sharing of custom web applications for machine learning and data science. It enables users to transform Python scripts into interactive web apps with minimal code, eliminating the need for extensive knowledge of web development technologies like HTML, CSS, or JavaScript.""")