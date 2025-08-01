import streamlit as st

# Give your app a title
st.title("My Streamlit App")
st.title("Your title")
st.markdown('# My Title')

# Header
st.header("Main header")
st.header("Data Overview")

# Subheader
st.subheader("This is a subheader")
st.subheader("Top Products This Month")

# Preformatted text
st.text("Some text")
st.text("Hello Streamlit")
st.text("Hello, World!\nThis is plain text.")


# Markdown
st.markdown("Markdown")
st.markdown("This is markdown **text**")
st.markdown("# Header1")
st.markdown("## Header2")
st.markdown("### Header3")
st.markdown("#### Header4")
st.markdown("##### Header5")
st.markdown("###### Header6")
st.markdown("####### Header7")
st.markdown("# Hello, World!")
st.markdown("**Bold text**, *italic text*, and [a link](https://streamlit.io)")
st.markdown("__Bold text__")
st.markdown("___Italic text___")
st.markdown("***Italic text***")
st.markdown("[streamlit documentation](https://docs.streamlit.io/)")

# Caption
st.caption("This is caption")
st.caption("Data updated as of July 2025")

# Example Usage
st.title("📈 Sales Dashboard")
st.header("Quarterly Revenue")
st.subheader("Q2 - 2025")

# Some chart or data here...
st.caption("Chart generated from internal sales system - Region: APAC")


# Code block
st.code("""
import pandas as pd
pd.read_csv(my_csv_file)
""")

st.code("print('Hello, Streamlit!')", language='python')

st.code("print('Hello, Java!')", language='Java')

# LaTeX
st.latex("x=2*2")
st.latex("x=2^2, 4*5, 2^6")

st.latex(r"E = mc^2")

# Examples-1

# Einstein's mass–energy equivalence
st.latex(r"E = mc^2")

# Quadratic formula
st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")

# Matrix
st.latex(r"""
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
""")

# Examples-2
a = 5
b = 3
st.latex(fr"x = {a} + {b}")

# Divider
st.divider()
st.text("Text above divider")
st.divider()
st.text("Text below divider")
st.divider()

st.title("📊 Dashboard")

st.header("🔹 Sales Summary")
st.write("Here are the sales numbers for Q2.")

st.divider()  # Adds a horizontal line

st.header("🔹 Customer Feedback")
st.write("Here’s what customers are saying.")

st.markdown("---")
st.write("We are using markdown('---') instead of st.divider()")
st.markdown("---")

# Write
st.write("Some text")
st.write("**This is bold**") # Interpreted as markdown
st.write({"Name": "Satish",
          "Age": 32}) # Displays dictionary
st.write(42) # Displays number