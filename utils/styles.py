import streamlit as st

def apply_theme():
    st.markdown("""
    <style>

    /* ── Remove default padding ── */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
    }

    header[data-testid="stHeader"] {
        background: transparent;
        height: 0;
    }

    /* ── Main background ── */
    .stApp {
        background: #F0F7F4;
    }

    /* ── Headings ── */
    h1 {
        color: #2E4A47 !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px !important;
    }

    h2, h3 {
        color: #2E4A47 !important;
        font-weight: 600 !important;
    }

    /* ── Body text ── */
    p, li {
        color: #4A6B67 !important;
        line-height: 1.7 !important;
    }

    /* ── Metric cards ──
       Inspired by the dashboard cards 
       in the image */
    div[data-testid="metric-container"] {
        background: white;
        border: none;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 2px 12px 
            rgba(77,182,172,0.12);
    }

    div[data-testid="metric-container"]:hover {
        box-shadow: 0 4px 20px 
            rgba(77,182,172,0.25);
        transform: translateY(-2px);
        transition: all 0.2s;
    }

    div[data-testid="metric-container"] label {
        color: #7FA39C !important;
        font-size: 0.75rem !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
    }

    div[data-testid="stMetricValue"] {
        color: #2E4A47 !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
    }

    /* ── Sidebar ──
       Like the left panel in the image */
    section[data-testid="stSidebar"] {
        background: #E0F2EE !important;
        border-right: 1px solid 
            rgba(77,182,172,0.2);
    }

    section[data-testid="stSidebar"] 
    .stMarkdown p {
        color: #2E4A47 !important;
    }

    /* ── Buttons ── */
    .stButton button {
        background: #4DB6AC !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        padding: 0.5rem 1.5rem !important;
        box-shadow: 0 2px 8px 
            rgba(77,182,172,0.3) !important;
    }

    .stButton button:hover {
        background: #2E9E93 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 15px 
            rgba(77,182,172,0.4) !important;
    }

    /* ── Chat messages ──
       Like the card style in the image */
    div[data-testid="stChatMessage"] {
        background: white !important;
        border-radius: 16px !important;
        box-shadow: 0 2px 8px 
            rgba(77,182,172,0.08) !important;
        margin: 8px 0 !important;
    }

    /* ── Input fields ── */
    .stChatInputContainer {
        background: white !important;
        border: 2px solid 
            rgba(77,182,172,0.3) !important;
        border-radius: 16px !important;
    }

    .stChatInputContainer:focus-within {
        border-color: #4DB6AC !important;
        box-shadow: 0 0 0 3px 
            rgba(77,182,172,0.15) !important;
    }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] {
        background: white;
        border-radius: 12px;
        padding: 4px;
        box-shadow: 0 2px 8px 
            rgba(77,182,172,0.08);
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        color: #7FA39C !important;
        font-weight: 500;
    }

    .stTabs [aria-selected="true"] {
        background: #4DB6AC !important;
        color: white !important;
    }

    /* ── Divider ── */
    hr {
        border-color: rgba(77,182,172,0.2) 
            !important;
    }

    /* ── Select boxes ── */
    div[data-baseweb="select"] > div {
        background: white !important;
        border: 2px solid 
            rgba(77,182,172,0.2) !important;
        border-radius: 12px !important;
    }

    /* ── Info boxes ── */
    div[data-testid="stAlert"] {
        background: #E8F5F0 !important;
        border: 1px solid 
            rgba(77,182,172,0.3) !important;
        border-radius: 12px !important;
        color: #2E4A47 !important;
    }

    </style>
    """, unsafe_allow_html=True)