import streamlit as st

# Bold and italic text
st.markdown("Your *markdown* **content** here.")

st.markdown("This is **bold** and this is *italic*.")

st.markdown("This is **BOLD** and this is ***ITALIC***.")

st.markdown("You can also use `inline code` in your text.")

st.divider()

# Headings & Text Formatting
st.markdown("# H1 Heading")
st.markdown("## H2 Heading")
st.markdown("### H3 Heading")

st.markdown("**Bold Text** and *Italic Text*")

st.divider()

# List 
st.markdown("""
- Bullet 1
- Bullet 2
  - Sub-bullet

1. Numbered item
2. Another item
""")

st.divider()

# Links & Images
st.markdown("[Visit Google](https://www.google.com)")

st.markdown("![Streamlit Logo](https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png)")

st.divider()

# Inline Code & Code Blocks
st.markdown("Use `print()` to display output in Python.")

st.markdown("""
```python
def greet():
    print("Hello, Streamlit!")
""")

st.divider()        

# Emoji Support
st.markdown("### 🚀 This app is awesome!")

st.divider() 

# HTML Support (with caution)
st.markdown("""
<h3 style='color: green;'>Custom HTML Heading</h3>
<p style='font-size: 16px;'>This is a paragraph with <b>HTML bold</b>.</p>
""", unsafe_allow_html=True)

st.divider()
