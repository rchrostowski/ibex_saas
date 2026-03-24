
"""
IBEX — Root Entry Point
Streamlit requires this file in the repo root.
page_icon: uses ibex_logo.png if present, falls back to emoji.
"""
import streamlit as st
import os

favicon = "assets/ibex_logo.png" if os.path.exists("assets/ibex_logo.png") else "🐐"

st.set_page_config(
    page_title="IBEX — Supplement Intelligence for D1 Athletics",
    page_icon=favicon,
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.switch_page("pages/00_Home.py")
