import streamlit as st

option = st.sidebar.selectbox("Choose view", ["Overview", "Details"])

tab1, tab2 = st.tabs(["📊 Table", "📈 Graph"])

with tab1:
    st.write(f"Table view for {option}")
with tab2:
    st.write(f"Graph view for {option}")
