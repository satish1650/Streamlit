import streamlit as st
import pandas as pd

data= pd.DataFrame(
    {
        "Name": ["Alice", "Bob", "Charlie"],
         "Age": [25, 30, 35],
         "Score": [88, 92, 95]
    }
)

st.dataframe(data)

# This makes it responsive and fills the page width.
st.dataframe(data, use_container_width=True)

# This highlights the max value in each column.
styled= data.style.highlight_max(axis=0)
st.dataframe(styled)