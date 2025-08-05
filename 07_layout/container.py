import streamlit as st

with st.container():
    st.write("This is inside the container")
    st.line_chart([1, 2, 3])

st.divider()

# Dynamic Update Example

container = st.container()

container.write("This is initial content.")

if st.button("Update container"):
    container.write("This was added after clicking the button.")
