import streamlit as st
import nltk
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))
from utils.styles import apply_theme

st.set_page_config(
    page_title="Medbot",
    page_icon="🏥",
    layout="wide"
)

@st.cache_resource
def setup_nltk():
    nltk.download('pUnkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('punkt_tab',quiet=True)
setup_nltk()

apply_theme()
st.markdown("""
<div style="text-align: center; padding: 50px 20px 30px 20px; background: linear-gradient(180deg, rgba(77,182,172,0.08) 0%, transparent 100%);">
    <div style="width: 90px; height: 90px; background: white; border-radius: 50%; margin: auto; display: flex; align-items: center; justify-content: center; font-size: 50px; box-shadow: 0 8px 24px rgba(77,182,172,0.25);">💗</div>
    <h1 style="margin-top: 16px; font-size: 2.8rem; font-weight: 800; color: #2E4A47 !important;">MedBot</h1>
    <p style="color: #7FA39C !important; font-size: 1.1rem; max-width: 400px; margin: auto;">
        Your Personal Healthcare Companion
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

side_left, col1, divider, col2, side_right = st.columns([1, 3, 0.5, 3, 1])

with col1:
    st.markdown("### What does MedBot do?")
    st.markdown("""
    MedBot analyses your symptoms using
    Natural Language Processing and Machine
    Learning to suggest possible conditions
    and recommend precautions.""")
with col2:
    st.markdown("### How to use it:")
    st.markdown("""
    1. **Chat**:- describe your symptoms in plain English
    2. **Disease info**:- explore all 30 diseases
    3. **Model info**:- understand how MedBot works""")

st.divider()

side_left, col1, col2, col3, col4, side_right = st.columns([1.5, 2, 2, 2, 2, 1.5])
col1.metric("Disease","41")
col2.metric("Symptoms","132")
col3.metric("Accuracy","95%+")
col4.metric("Model","Random Forest")

st.divider()

st.markdown("""
<div style="
    text-align: center;
    padding: 24px;
    background: white;
    border-radius: 16px;
    box-shadow: 0 2px 12px 
        rgba(77,182,172,0.12);
    margin-top: 10px;
">
    <p style="
        color: #2E4A47;
        font-size: 1.05rem;
        margin: 0 0 8px 0;
        font-weight: 600;
    ">
        Use the sidebar to navigate
    </p>
    <p style="color: #7FA39C; margin: 0">
        Start with 
        <strong style="color:#4DB6AC">
            Chat
        </strong> 
        to describe your symptoms
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;margin-top:20px">
<p style="color:#888;font-size:0.8rem">
⚠️ MedBot is for educational purposes
only does not constitute medical
advice. Always consult a qualified
doctor for medical concerns,
</p>
</div> """,unsafe_allow_html=True)