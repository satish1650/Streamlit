import streamlit as st
import pandas as pd

# Button
primary_button= st.button(label="Primary", type="primary")
secondary_button= st.button(label="Secondary", type="secondary")

if primary_button:
    st.write("Primary button clicked!")

if secondary_button:
    st.write("Secondary button clicked!")

st.divider()

# Checkbox
checkbox= st.checkbox("Remember me")
if checkbox:
    st.write("I will remember you!")
else:
    st.write("I will forget you!")

st.divider()

# Radio Button
df= pd.read_csv("05_input_widgets-part1\data\sample.csv")

radio= st.radio("Choose a column to display", options=df.columns[1:], index=1, horizontal=True)
st.write(radio)

st.write("---")

# Selectbox
select= st.selectbox("Choose a column", options=df.columns[1:], index=0)
st.write(f"You selected: {select}")

st.write('___')

# Multiselect
multiselect= st.multiselect("Choose as many columns as you want", options=df.columns[1:], default=["col2"], max_selections=2)
st.write(multiselect)

st.divider()

# Slider
slider= st.slider("Pick a number", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
st.write(slider)

st.divider()

# Text Input
text_input= st.text_input("Enter your name", placeholder="Type here...")
if text_input:
    st.write(f"Your name is: {text_input}")

st.divider()

# Number input
num_input= st.number_input("Pick a number", min_value=0, max_value=10, value=0, step=1)
st.write(f"You picked {num_input}")

st.divider()

# Text Area
txt_area= st.text_area("What do you want to tell me?", height=250, placeholder="Write your message here...")
st.write(txt_area)