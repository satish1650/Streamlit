import streamlit as st

# Sidebar title
st.sidebar.title("Sidebar Title")

# Sidebar widget
name= st.sidebar.text_input("Enter your name")
age= st.sidebar.slider("Select your age", 0, 100)

# Display in main area
st.write(f"Hello, {name}. You are {age} years old.")

# There are two ways to use it:
# 1. Direct call
# option= st.sidebar.selectbox("Choose one", ["A", "B", "C"])

# 2. Using with block
# with st.sidebar:
#     st.write("Settings")
#     value = st.slider("Pick a value", 0, 100)

# if value:    
#     st.write(f"You selected: {value}")

# with st.sidebar:
#     st.write("Settings")
#     value = st.slider("Pick a value", 0, 100)
    
#     if value:    
#         st.write(f"You selected: {value}")
