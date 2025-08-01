import streamlit as st
import pandas as pd

df= pd.read_csv(r'data\sample.csv', dtype='int')

st.write('---')
st.markdown("st.dataframe()")
st.dataframe(df)

st.divider()

st.markdown("**st.write()**")
st.write(df)

st.write('___')

st.markdown("#### ***st.table()***")
st.table(df)

st.write('---')

st.metric(label="Expenses", value=900, delta=20, delta_color="inverse")