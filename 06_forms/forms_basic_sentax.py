import streamlit as st

with st.form("my_form"):
    name= st.text_input("Enter your name")
    age= st.number_input("Enter your age", min_value=0, max_value=120)

    # Submit button (must be inside the form)
    submitted= st.form_submit_button("Submit")

if submitted:
    st.write(f"Hello {name}, you are {age} years old!")

st.divider()

import streamlit as st

with st.form("my_form2", clear_on_submit=True):
    name= st.text_input("Enter your name")
    age= st.number_input("Enter your age", min_value=0, max_value=120)

    # Submit button (must be inside the form)
    submitted= st.form_submit_button("Submit")

if submitted:
    st.write(f"Hello {name}, you are {age} years old!")