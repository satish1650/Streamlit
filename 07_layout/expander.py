import streamlit as st

# with st.expander("See more details"):
#     st.write("Here are more details you can reveal.")

with st.expander("Fill this form"):
    name= st.text_input("Name")
    age= st.number_input("Age", min_value=0)
    st.write(f"Hello, {name}. You are {age} years old.")