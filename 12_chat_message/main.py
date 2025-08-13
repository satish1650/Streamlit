import streamlit as st

st.title("🤖 Simple Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input box
if prompt := st.chat_input("Type your message"):
    # Append user's message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

# Generate bot reply (dummy here)
response = f"You said: {prompt}"
st.session_state.messages.append({"role": "assistant", "content": response})
with st.chat_message("assistant"):
    st.markdown(response)