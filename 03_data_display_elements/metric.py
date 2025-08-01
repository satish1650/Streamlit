import streamlit as st

st.metric(label="Revenue", value="$10M", delta="+5%")
st.metric(label="Revenue", value="$10M", delta="-5%")

st.divider()

st.metric(label="📈 Monthly Sales", value="₹2.5 Cr", delta="+12%")
st.metric(label="📉 Customer Churn", value="3.2%", delta="-0.4%")

st.divider()

# using delta_color 
st.metric("Net Profit", "$2M", "-3%", delta_color="inverse")
st.metric("Net Profit", "$2M", "+3%", delta_color="inverse")
st.metric("Net Profit", "$2M", "-3%", delta_color="normal")
st.metric("Net Profit", "$2M", "+3%", delta_color="normal")
st.metric("Net Profit", "$2M", "-3%", delta_color="off")
st.metric("Net Profit", "$2M", "+3%", delta_color="off")

# Use in columns for side-by-side layout:
col1, col2, col3 = st.columns(3)

col1.metric("Users", "12,500", "+8%")
col2.metric("Bounce Rate", "34%", "-2%")
col3.metric("Revenue", "₹1.2 Cr", "+5.5%")