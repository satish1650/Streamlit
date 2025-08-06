import streamlit as st 

# Initialize state
if 'count' not in st.session_state:
    st.session_state.count= 0

# Button to increment
if st.button("Increment Count"):
    st.session_state.count += 1

# Display the current count
st.write(f"Current Count: {st.session_state.count}")