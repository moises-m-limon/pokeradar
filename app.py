import streamlit as st

# Title of the app
st.title("PokeRadar")
st.text('By Moises Limon')

# Read the HTML file
html_file_path = "map/map.html"  # Replace with your file path
with open(html_file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Render the HTML in Streamlit
st.components.v1.html(html_content, height=500, scrolling=True)
