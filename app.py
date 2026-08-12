import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Arbiter Dashboard", layout="wide")

# Read and render your HTML dashboard
with open("frontend/arbiter_dashboard.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=1000, scrolling=True)
