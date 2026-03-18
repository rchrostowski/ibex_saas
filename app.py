"""
IBEX — Root Entry Point
Streamlit requires this file in the repo root.
It boots the app and redirects to the landing page.
"""
import streamlit as st

st.set_page_config(
    page_title="IBEX — Precision Supplement Systems for D1 Athletes",
    page_icon="assets/ibex_logo.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.switch_page("pages/00_Home.py")
