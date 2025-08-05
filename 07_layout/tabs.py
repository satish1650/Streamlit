import streamlit as st

tab1, tab2 = st.tabs(["📊 Data", "📈 Chart"])

with tab1:
    st.write("Here is your data table.")
    st.dataframe({"A": [1, 2], "B": [3, 4]})

with tab2:
    st.write("Here is your chart.")
    st.line_chart([1, 2, 3, 4])
