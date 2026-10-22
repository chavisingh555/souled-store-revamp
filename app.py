import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="The Souled Store | Revamped Experience & Analytics",
    page_icon="👕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM LIGHT THEME & BRAND TYPOGRAPHY CSS
# ==========================================
st.markdown("""
    <style>
    /* Google Font Import */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800;900&display=swap');

    html, body, [class*="css"], .stApp {
        font-family: 'Poppins', sans-serif !important;
        background-color: #F8F9FA !important;
        color: #1A1A24 !important;
    }

    /* Brand Headers */
    .brand-header {
        font-size: 38px;
        font-weight: 900;
        color: #E2231A;
        text-align: center;
        letter-spacing: 2px;
        margin-top: -10px;
        text-transform: uppercase;
    }
    .sub-title {
        font-size: 15px;
        color: #555566;
        text-align: center;
        margin-bottom: 25px;
        font-weight: 600;
        letter-spacing: 1px;
    }

    /* Ad Banner Card */
    .ad-banner {
        background: linear-gradient(135deg, #181824 0%, #2D2D3F 100%);
        color: #ffffff !important;
        padding: 22px;
        border-radius: 12px;
        border-left: 6px solid #E2231A;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }

    /* Pricing & Badges */
    .price-tag {
        font-size: 24px;
        font-weight: 800;
        color: #E2231A;
        margin-top: 5px;
    }
    .badge-rto {
        background-color: #E8F5E9;
        color: #2E7D32;
        border: 1px solid #A5D6A7;
        padding: 6px 12px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 13px;
        display: inline-block;
    }

    /* Custom Buttons */
    .stButton>button {
        background-color: #E2231A !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        border: none !important;
        padding: 10px 18px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        background-color: #C11B13 !important;
        box-shadow: 0 4px 12px rgba(226, 35, 26, 0.3) !important;
    }

    /* Metric Card Styling */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E0E0E8 !important;
        border-radius: 10px !important;
        padding: 12px !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.02) !important;
    }

    /* Tabs Override */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #EAEAEA;
        border-radius: 8px 8px 0 0;
        color: #333333;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #E2231A !important;
        color: #FFFFFF !important;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE INITIALIZATION
# ==========================================
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'pincode' not in st.session_state:
    st.session_state.pincode = "831001"
if 'user_collection' not in st.session_state:
    st.session_state.user_collection = ["Batman: Dark Knight Tee", "Gryffindor Hoodie", "Barcelona Rug"]
if 'cod_verified' not in st.session_state:
    st.session_state.cod_verified = False

# ==========================================
# AUTHENTIC FANDOM PRODUCT IMAGE URLS
# ==========================================
IMG_BATMAN_TEE = "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?w=600&auto=format&fit=crop&q=80"
IMG_SUPERGIRL_TEE = "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=600&auto=format&fit=crop&q=80"
IMG_BARCELONA_RUG = "https://padloom.com/cdn/shop/files/FCBarcelonaMapRug.jpg?v=1700000000&width=600"
IMG_HARRY_POTTER = "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=600&auto=format&fit=crop&q=80"

# ==========================================
# SIDEBAR NAVIGATION & APP PERK BANNER
# ==========================================
st.sidebar.markdown("<h2 style='color:#E2231A; font-weight:900; margin-bottom:0;'>THE SOULED STORE</h2>", unsafe_allow_html=True)
st.sidebar.caption("Digital Strategy & Analytics Prototype")
st.sidebar.divider()

page = st.sidebar.radio(
    "Select Prototype Page:",
    [
        "1. Ad-Matched Fandom Hub (ToFu/MoFu)",
        "2. Smart Product Page & Fit Engine",
        "3. Frictionless Checkout & RTO Shield",
        "4. Fan Closet & Analytics Dashboard"
    ]
)

st.sidebar.divider()
st.sidebar.markdown("""
<div style="background-color: #FFF3CD; padding:14px; border-radius:10px; border:1px solid #FFEBAA;">
    <span style="color:#856404; font-weight:bold; font-size:14px;">📲 App Exclusive Perk</span><br/>
    <span style="color:#333333; font-size:13px;">Get <b>10% Cashback</b> on every app order!</span><br/>
    <small style="color:#666666;">Scan QR code or use deep link</small>
</div>
""", unsafe_allow_html=True)
st.sidebar.image("https://api.qrserver.com/v1/create-qr-code/?size=120x120&data=https://thesouledstore.com/app", width=120)

# ==============================================================================
# PAGE 1: AD-MATCHED FANDOM HUB (ToFu -> MoFu Drop Landing)
# ==============================================================================
if page == "1. Ad-Matched Fandom Hub (ToFu/MoFu)":
    st.markdown('<div class="brand-header">THE SOULED STORE</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Ad-To-Landing Page Experience Engine</div>', unsafe_allow_html=True)

    st.subheader("🎯 Simulate Meta Ad Campaign Source")
    ad_source = st.selectbox(
        "Select the Meta Ad Creative the customer clicked on:",
        [
            "🦇 Batman: 'Your Batman Era Starts Here' Ad Drop",
            "💖 Supergirl / Powerpuff Girls: 'Official Drop' Ad",
            "⚽ FC Barcelona: 'Bring Your Fandom Home' Rugs Ad",
            "📍 Jamshedpur / Muzaffarpur Flagship Store Launch Ad"
        ]
    )

    st.divider()

    # Dynamic Ad-Matched Banner
    if "Batman" in ad_source:
        st.markdown("""
        <div class="ad-banner">
            <h2 style="color:#FFD700; margin:0;">🦇 YOUR BATMAN ERA STARTS HERE</h2>
            <p style="color:#E0E0E0; margin-top:5px;">Official DC Comics Licensed Drop | Oversized Graphic Tees, Hoodies & Caps</p>
        </div>
        """, unsafe_allow_html=True)
    elif "Supergirl" in ad_source:
        st.markdown("""
        <div class="ad-banner" style="border-left-color: #FF69B4;">
            <h2 style="color:#FF69B4; margin:0;">💖 UNLEASH YOUR SUPERHERO ERA</h2>
            <p style="color:#E0E0E0; margin-top:5px;">Official Supergirl & Cartoon Network Y2K Nostalgia Drop</p>
        </div>
        """, unsafe_allow_html=True)
    elif "Barcelona" in ad_source:
        st.markdown("""
        <div class="ad-banner" style="border-left-color: #388E3C;">
            <h2 style="color:#81C784; margin:0;">⚽ BRING YOUR FANDOM HOME: FC BARCELONA</h2>
            <p style="color:#E0E0E0; margin-top:5px;">Official Culér Home Decor, Custom Rugs & Matchday Apparel</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="ad-banner" style="border-left-color: #0288D1;">
            <h2 style="color:#81D4FA; margin:0;">📍 NOW OPEN IN JAMSHEDPUR & MUZAFFARPUR!</h2>
            <p style="color:#E0E0E0; margin-top:5px;">Experience online-to-store pick up or visit our newest flagship stores.</p>
        </div>
        """, unsafe_allow_html=True)

    col_loc1, col_loc2 = st.columns([3, 1])
    with col_loc1:
        st.success("📍 **Omnichannel Check:** Near Jamshedpur (Main Road) Flagship Store. 1-Hour Pickup available!")
    with col_loc2:
        st.button("🏬 Reserve to Try in Store")

    st.divider()

    # Drop Countdown
    st.subheader("⏱️ Limited Edition Drop Countdown")
    col_cd1, col_cd2 = st.columns([3, 1])
    with col_cd1:
        st.info("🔥 **Next Drop:** Marvel 'Secret Wars' Metallic Oversized Tee drops in **02 Days : 14 Hours : 35 Mins**")
    with col_cd2:
        if st.button("🔔 Notify Me on App"):
            st.toast("Subscribed! Push notification alert scheduled.")

    st.subheader("🛍️ Curated Products Matching Your Ad Hook")
    pcol1, pcol2, pcol3 = st.columns(3)

    with pcol1:
        st.image(IMG_BATMAN_TEE, width="stretch")
        st.markdown("### **Batman: Gotham Knight Tee**")
        st.markdown("<span class='price-tag'>₹1,299</span>", unsafe_allow_html=True)
        st.caption("🔥 Runs Large (78% of buyers sized down)")

    with pcol2:
        st.image(IMG_SUPERGIRL_TEE, width="stretch")
        st.markdown("### **Supergirl: Official Graphic Tee**")
        st.markdown("<span class='price-tag'>₹1,199</span>", unsafe_allow_html=True)
        st.caption("✨ Official DC Licensed Drop")

    with pcol3:
        st.image(IMG_HARRY_POTTER, width="stretch")
        st.markdown("### **Harry Potter: Hogwarts Oversized Tee**")
        st.markdown("<span class='price-tag'>₹1,399</span>", unsafe_allow_html=True)
        st.caption("⚡ 10% Cashback on App Purchase")


# ==============================================================================
# PAGE 2: SMART PRODUCT PAGE & FIT ENGINE
# ==============================================================================
elif page == "2. Smart Product Page & Fit Engine":
    st.header("👕 Batman: Gotham Knight Oversized T-Shirt")
    st.caption("Official DC Comics Licensee | Product ID: TSS-BTM-2026")

    col_img, col_main = st.columns([1, 1])

    with col_img:
        st.image(IMG_BATMAN_TEE, width="stretch")
        
        st.subheader("📸 Fan Photo Wall ('Wear It Like Me')")
        p_col1, p_col2 = st.columns(2)
        p_col1.info("👤 **Rohan (178 cm, 72 kg)**\n'Bought Size M. Perfect oversized drop shoulder fit!'")
        p_col2.info("👤 **Ananya (165 cm, 55 kg)**\n'Bought Size S. Oversized look is super cozy.'")

    with col_main:
        st.markdown("### ₹1,299 <span style='text-decoration:line-through; color:#777; font-size:16px;'>₹1,999</span> <span style='color:#28A745; font-size:18px;'>(35% OFF)</span>", unsafe_allow_html=True)
        st.markdown("<span class='badge-rto'>🏷️ Fit Badge: Runs Large (78% of buyers sized down)</span>", unsafe_allow_html=True)

        st.divider()

        st.subheader("📍 Pincode Serviceability & Delivery Estimate")
        pincode_in = st.text_input("Enter Pincode:", value=st.session_state.pincode)
        if pincode_in:
            st.session_state.pincode = pincode_in
            delivery_date = (datetime.now() + timedelta(days=3)).strftime('%A, %b %d')
            st.success(f"🚚 Estimated Delivery by **{delivery_date}** to Pincode **{pincode_in}**")

        st.divider()

        st.subheader("📏 Smart Fit Recommender")
        fit_tab1, fit_tab2 = st.tabs(["🧍 Body Build Slider", "👕 Compare With A Tee You Own"])

        with fit_tab1:
            height = st.slider("Select Height (cm)", 150, 200, 175)
            weight = st.slider("Select Weight (kg)", 45, 110, 72)
            fit_pref = st.radio("Fit Preference:", ["Regular Fit", "Relaxed Oversized Fit"], horizontal=True)

            if weight < 60: rec_size = "S" if fit_pref == "Regular Fit" else "M"