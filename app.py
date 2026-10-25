import streamlit as st
import pandas as pd
import datetime

# ==========================================
# 1. PAGE CONFIG & CUSTOM CSS (EXACT MATCH TO SCREENSHOTS)
# ==========================================
st.set_page_config(
    page_title="The Souled Store | Official Fandom Merchandise",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS matching TSS UI/UX, Trust Banner, and Aesthetics
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background-color: #FFFFFF;
        color: #111111;
    }
    
    /* Top Header Bar */
    .tss-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 20px;
        border-bottom: 1px solid #EAEAEA;
        background-color: #FFFFFF;
    }
    
    .tss-logo {
        font-size: 26px;
        font-weight: 800;
        color: #E2231A;
        letter-spacing: -0.5px;
    }
    
    .tss-nav-link {
        font-weight: 700;
        font-size: 14px;
        color: #111111;
        margin-right: 25px;
        text-transform: uppercase;
        text-decoration: none;
    }
    
    /* Trust Strip (Icy Blue Banner from Screenshot) */
    .trust-strip {
        background-color: #E6F4F8;
        padding: 14px 10px;
        border-radius: 4px;
        margin-top: 15px;
        margin-bottom: 25px;
    }
    
    .trust-item {
        text-align: center;
        font-size: 13px;
        font-weight: 600;
        color: #1A2B32;
    }
    
    /* Section Headers */
    .section-header {
        text-align: center;
        font-size: 22px;
        font-weight: 800;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin: 25px 0px 15px 0px;
        color: #111111;
    }
    
    .sub-category-bar {
        text-align: center;
        font-size: 14px;
        font-weight: 600;
        letter-spacing: 2px;
        color: #444444;
        margin-bottom: 25px;
    }
    
    /* Product Card Styling */
    .product-card {
        border: 1px solid #EAEAEA;
        border-radius: 8px;
        padding: 12px;
        background-color: #FFFFFF;
        transition: transform 0.2s;
    }
    .product-card:hover {
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    }
    
    .fit-badge {
        background-color: #111111;
        color: #FFFFFF;
        font-size: 10px;
        font-weight: 700;
        padding: 3px 8px;
        border-radius: 2px;
        text-transform: uppercase;
    }
    
    .price-text {
        font-size: 16px;
        font-weight: 700;
        color: #111111;
    }
    
    .strike-price {
        text-decoration: line-through;
        color: #888888;
        font-size: 13px;
        margin-left: 6px;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #E2231A;
        color: white;
        font-weight: 700;
        border-radius: 4px;
        border: none;
        padding: 8px 16px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #C11B13;
        color: white;
    }
    
    /* Nudge & Alert Box */
    .prepaid-nudge {
        background-color: #E6F9F0;
        border: 1px solid #10B981;
        padding: 12px;
        border-radius: 6px;
        color: #065F46;
        font-weight: 600;
        margin-top: 10px;
    }
    
    .cod-warning {
        background-color: #FFFBEB;
        border: 1px solid #F59E0B;
        padding: 12px;
        border-radius: 6px;
        color: #92400E;
        font-weight: 600;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SESSION STATE MANAGEMENT
# ==========================================
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'underdog_member' not in st.session_state:
    st.session_state.underdog_member = False
if 'selected_ip' not in st.session_state:
    st.session_state.selected_ip = "All Fandoms"
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Store Front"
if 'fit_view' not in st.session_state:
    st.session_state.fit_view = "Relaxed Oversized"

# ==========================================
# 3. MOCK DATA: PRODUCTS & IP HUBS
# ==========================================
PRODUCTS = [
    {
        "id": 1,
        "name": "Batman: Gotham Knight Oversized Tee",
        "ip": "DC Gotham",
        "price": 1299,
        "mrp": 1799,
        "fit": "Oversized",
        "img_regular": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=600&q=80",
        "img_oversized": "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?w=600&q=80",
        "tag": "NEW DROP"
    },
    {
        "id": 2,
        "name": "Venom: Rise of Symbiote Heavyweight Tee",
        "ip": "Marvel Universe",
        "price": 1199,
        "mrp": 1599,
        "fit": "Super Oversized",
        "img_regular": "https://images.unsplash.com/photo-1583743814966-8936f5b7be1A?w=600&q=80",
        "img_oversized": "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=600&q=80",
        "tag": "MEMBER EXCLUSIVE"
    },
    {
        "id": 3,
        "name": "Supergirl: Truth & Justice Graphic Tee",
        "ip": "DC Gotham",
        "price": 999,
        "mrp": 1399,
        "fit": "Fitted",
        "img_regular": "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?w=600&q=80",
        "img_oversized": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=600&q=80",
        "tag": "LIMITED PIECES"
    },
    {
        "id": 4,
        "name": "Naruto Shippuden: Akatsuki Cloud Oversized Tee",
        "ip": "Anime Zone",
        "price": 1299,
        "mrp": 1699,
        "fit": "Oversized",
        "img_regular": "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=600&q=80",
        "img_oversized": "https://images.unsplash.com/photo-1583743814966-8936f5b7be1A?w=600&q=80",
        "tag": "BESTSELLER"
    },
    {
        "id": 5,
        "name": "FC Barcelona 1899 Heritage Polo",
        "ip": "Sports / FCB",
        "price": 1499,
        "mrp": 1999,
        "fit": "Regular",
        "img_regular": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=600&q=80",
        "img_oversized": "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?w=600&q=80",
        "tag": "OFFICIAL MERCH"
    }
]

# ==========================================
# 4. TOP NAVBAR & NAVIGATION
# ==========================================
# Brand Header
st.markdown("""
<div class="tss-header">
    <div class="tss-logo">👻 The Souled Store</div>
    <div>
        <span class="tss-nav-link">MEN</span>
        <span class="tss-nav-link">WOMEN</span>
        <span class="tss-nav-link">SNEAKERS</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar Routing & Controls
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?w=300&q=80", caption="REVAMP PROTOTYPE")
    st.title("⚡ Revamp Navigation")
    
    page_choice = st.radio(
        "Select Page View:",
        ["1. Fandom Store & IP Hub", "2. Smart Sizing PDP", "3. Cart & RTO Shield Checkout"]
    )
    
    st.divider()
    st.subheader("🛒 Cart Drawer Summary")
    st.write(f"**Items in Cart:** {len(st.session_state.cart)}")
    if st.session_state.underdog_member:
        st.success("👑 Underdog Club Member Active")
    else:
        st.info("💡 Underdog Club Not Added")

# ==========================================
# REVAMP MODULE 1: FANDOM-FIRST & IP NAVIGATION
# ==========================================
if page_choice == "1. Fandom Store & IP Hub":
    
    # 🌟 FEATURE 1: IP HUB SELECTOR (TOP BAR FILTER)
    st.write(" ")
    st.markdown("### 🍿 EXPLORE BY FANDOM WORLD (IP HUBS)")
    ip_cols = st.columns(5)
    
    ip_list = ["All Fandoms", "DC Gotham", "Marvel Universe", "Anime Zone", "Sports / FCB"]
    
    for i, ip_name in enumerate(ip_list):
        if ip_cols[i].button(f"✨ {ip_name}", key=f"ip_{i}"):
            st.session_state.selected_ip = ip_name

    st.markdown(f"**Active Ad-Landing View:** `{st.session_state.selected_ip}`")
    st.divider()
    
    # Trust Strip from Screenshot
    st.markdown("""
    <div class="trust-strip">
        <div style="display: flex; justify-content: space-around; align-items: center;">
            <div class="trust-item">📲 <b>10% Cashback</b><br><span style="font-size:11px; color:#555;">on all App orders</span></div>
            <div class="trust-item">🔄 <b>30 Days Easy Returns</b><br><span style="font-size:11px; color:#555;">& Exchanges</span></div>
            <div class="trust-item">🚚 <b>Free & Fast Shipping</b><br><span style="font-size:11px; color:#555;">On orders above ₹999</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Section Header (Screenshot Aesthetic)
    st.markdown('<div class="section-header">EXPLORE MERCHANDISE</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-category-bar">OVERSIZED | RELAXED | FITTED</div>', unsafe_allow_html=True)
    
    # Product Grid Display
    filtered_products = PRODUCTS if st.session_state.selected_ip == "All Fandoms" else [p for p in PRODUCTS if p['ip'] == st.session_state.selected_ip]
    
    grid_cols = st.columns(3)
    for idx, prod in enumerate(filtered_products):
        with grid_cols[idx % 3]:
            st.image(prod['img_regular'], use_container_width=True)
            st.markdown(f"<span class='fit-badge'>{prod['fit']}</span> <span style='font-size:11px; color:#E2231A; font-weight:700;'>{prod['tag']}</span>", unsafe_allow_html=True)
            st.markdown(f"**{prod['name']}**")
            st.markdown(f"<span class='price-text'>₹{prod['price']}</span> <span class='strike-price'>₹{prod['mrp']}</span>", unsafe_allow_html=True)
            
            if st.button(f"View Product & Fit Engine", key=f"prod_btn_{prod['id']}"):
                st.session_state.selected_product = prod
                st.info("Navigate to '2. Smart Sizing PDP' in the sidebar to test fit engine!")

# ==========================================
# REVAMP MODULE 2: INTERACTIVE "SMART SIZING" ENGINE
# ==========================================
elif page_choice == "2. Smart Sizing PDP":
    
    prod = st.session_state.get('selected_product', PRODUCTS[0])
    
    st.markdown(f"## 👕 {prod['name']}")
    st.caption(f"Category: {prod['ip']} | Tag: {prod['tag']}")
    
    pdp_col1, pdp_col2 = st.columns([1, 1])
    
    with pdp_col1:
        # Fit Visualizer Toggle (Regular vs Super Oversized Fit View)
        st.markdown("#### 👁️ Fit Visualizer Toggle")
        fit_toggle = st.radio(
            "Select Fit Expectation Model View:",
            ["Regular Standard Fit View", "Super Oversized Dropped-Shoulder View"],
            horizontal=True
        )
        
        img_to_show = prod['img_oversized'] if "Oversized" in fit_toggle else prod['img_regular']
        st.image(img_to_show, caption=f"Displaying: {fit_toggle}", use_container_width=True)
    
    with pdp_col2:
        st.markdown(f"<span class='price-text' style='font-size:24px;'>₹{prod['price']}</span> <span class='strike-price' style='font-size:16px;'>₹{prod['mrp']}</span>", unsafe_allow_html=True)
        st.write("Inclusive of all taxes")
        
        st.divider()
        st.markdown("### 🧮 Smart Height & Weight Fit Calculator")
        st.write("Avoid return hassles! Find your perfect fit based on 500+ verified buyers.")
        
        # 2-Slider Sizing Tool
        height = st.slider("Select your Height (cm):", min_value=150, max_value=200, value=175, step=1)
        weight = st.slider("Select your Weight (kg):", min_value=45, max_value=120, value=74, step=1)
        
        # Sizing Algorithm Logic
        bmi = weight / ((height/100) ** 2)
        if height > 180 and weight > 80:
            rec_size = "XL"
            fit_note = "XL gives you the ideal relaxed oversized drop."
        elif height > 170 and weight > 65:
            rec_size = "L"
            fit_note = "L delivers standard streetwear proportions."
        elif height > 160 and weight > 55:
            rec_size = "M"
            fit_note = "M provides a clean, comfortable fit."
        else:
            rec_size = "S"
            fit_note = "S fits snugly to your frame."
            
        st.success(f"🎯 **Recommended Size: {rec_size}** ({fit_note})")
        
        selected_size = st.selectbox("Confirm Size to Add:", ["S", "M", "L", "XL", "XXL"], index=["S", "M", "L", "XL", "XXL"].index(rec_size))
        
        st.write(" ")
        if st.button("🛒 ADD TO CART", key="add_to_cart_btn"):
            cart_item = {
                "name": prod['name'],
                "price": prod['price'],
                "size": selected_size,
                "fit": prod['fit']
            }
            st.session_state.cart.append(cart_item)
            st.toast(f"Added {prod['name']} (Size {selected_size}) to Cart!", icon="✅")

# ==========================================
# REVAMP MODULE 3 & 4: SMART CHECKOUT, RTO SHIELD & LOYALTY
# ==========================================
elif page_choice == "3. Cart & RTO Shield Checkout":
    
    st.markdown("## 🛒 Shopping Cart & RTO-Shield Checkout")
    
    if len(st.session_state.cart) == 0:
        st.warning("Your cart is currently empty! Add items from the PDP or Store view.")
        st.session_state.cart.append({"name": PRODUCTS[0]['name'], "price": PRODUCTS[0]['price'], "size": "L", "fit": "Oversized"})
        st.rerun()
        
    cart_col, checkout_col = st.columns([1.2, 1])
    
    with cart_col:
        st.markdown("### 📦 Cart Items")
        subtotal = 0
        for i, item in enumerate(st.session_state.cart):
            st.markdown(f"**{i+1}. {item['name']}**")
            st.caption(f"Size: {item['size']} | Fit: {item['fit']}")
            st.write(f"Price: **₹{item['price']}**")
            subtotal += item['price']
            st.divider()
            
        # 🌟 FEATURE 4: 1-CLICK UNDERDOG CLUB LOYALTY INTEGRATION
        st.markdown("### 👑 Underdog Club Membership")
        loyalty_toggle = st.checkbox(
            "Add 1-Year Underdog Club Membership for ₹199 (Unlock ₹350 instant savings today!)",
            value=st.session_state.underdog_member
        )
        st.session_state.underdog_member = loyalty_toggle
        
        membership_fee = 199 if st.session_state.underdog_member else 0
        member_discount = 350 if st.session_state.underdog_member else 0
        
    with checkout_col:
        st.markdown("### 💳 Payment & RTO Shield")
        
        # 🌟 FEATURE 3: DYNAMIC PREPAID INCENTIVE & TRANSPARENT BREAKDOWN
        payment_method = st.radio(
            "Choose Payment Mode:",
            ["Prepaid UPI / Credit Card (Recommended)", "Cash on Delivery (COD)"]
        )
        
        prepaid_discount = 100 if "Prepaid" in payment_method else 0
        cod_surcharge = 50 if "COD" in payment_method else 0
        
        if "Prepaid" in payment_method:
            st.markdown("""
            <div class="prepaid-nudge">
                🎉 <b>PREPAID SAVINGS:</b> You save ₹100 instantly + earn 50 Underdog Loyalty Coins!
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="cod-warning">
                ⚠️ <b>COD SURCHARGE:</b> ₹50 handling & fraud verification fee added. Switch to UPI to save ₹150 overall!
            </div>
            """, unsafe_allow_html=True)
            
        st.write(" ")
        st.markdown("#### 📑 Order Summary")
        st.write(f"Bag Subtotal: **₹{subtotal}**")
        if membership_fee > 0:
            st.write(f"Underdog Membership: **+₹{membership_fee}**")
        if member_discount > 0:
            st.write(f"Underdog Instant Discount: **-₹{member_discount}**")
        if prepaid_discount > 0:
            st.write(f"Prepaid UPI Discount: **-₹{prepaid_discount}**")
        if cod_surcharge > 0:
            st.write(f"COD Verification Surcharge: **+₹{cod_surcharge}**")
            
        final_total = subtotal + membership_fee - member_discount - prepaid_discount + cod_surcharge
        st.markdown(f"### **Final Total: ₹{max(0, final_total)}**")
        
        if st.button("🚀 PLACE ORDER NOW"):
            st.balloons()
            st.success("Order Placed Successfully! RTO Risk Screened & Intent Verified.")