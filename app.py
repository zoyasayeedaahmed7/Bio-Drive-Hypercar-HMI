import streamlit as st

# Set page layout to wide
st.set_page_config(page_title="BIO-DRIVE // Luxury HMI Concept", layout="wide")

# Sophisticated Luxury Styling with Cinematic Background and Serif Typography
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lora:wght@400;500;700&display=swap" rel="stylesheet">
    
    <style>
    /* Full Page Cinematic Car Background Overlay */
    .stApp {
        background: linear-gradient(rgba(10, 15, 30, 0.88), rgba(10, 15, 30, 0.94)), 
                    url("https://images.unsplash.com/photo-1617814076367-b759c7d7e738?auto=format&fit=crop&q=80&w=2000");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #f1f5f9;
        font-family: 'Lora', serif;
    }
    
    /* Elegant Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.85) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255,255,255,0.05);
    }
    
    /* Editorial Serif Title Styling */
    .luxury-title {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        color: #f8fafc;
        letter-spacing: 1px;
        margin-bottom: 0px;
    }
    
    /* Floating Glassmorphism Telemetry Cards */
    .metric-box {
        background: rgba(30, 41, 59, 0.45);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    /* Soft, Soothing Intelligent Notification Banner */
    .status-banner {
        border-radius: 16px;
        padding: 30px;
        margin-bottom: 35px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.15);
    }
    
    .status-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        font-weight: 700;
        margin-top: 0;
        margin-bottom: 12px;
        letter-spacing: 0.5px;
    }
    </style>
    """, unsafe_allow_html=True)

# App Editorial Header
st.markdown('<h1 class="luxury-title">Bio-Drive : Integrated OS</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#94a3b8; font-family:\'Lora\'; font-size:14px; font-style:italic; letter-spacing:1px; margin-bottom:50px;">A Study on Adaptive Contextual Interfaces & Driver State Optimization</p>', unsafe_allow_html=True)

# Sophisticated Sidebar Control Panel
st.sidebar.markdown('<h2 style="font-family:\'Playfair Display\'; font-size:22px; color:#f1f5f9; font-weight:700;">Biometric Inputs</h2>', unsafe_allow_html=True)
st.sidebar.markdown('<p style="color:#94a3b8; font-size:14px; font-style:italic;">Simulate pilot cognitive variations.</p>', unsafe_allow_html=True)

heart_rate = st.sidebar.slider("Driver Heart Rate (BPM)", 60, 180, 75)
speed = st.sidebar.slider("Vehicle Velocity (MPH)", 0, 240, 65)
g_force = st.sidebar.slider("Inertial Dynamics (G)", 0.0, 5.2, 0.9, step=0.1)

# Luxury Soothing Palette Logic (Warm Champagne, Sage Calm, Soft Rose Alert)
if heart_rate > 130:
    state_label = "System Directive: Restorative Comfort & Mitigation"
    accent_color = "#e2b6b6"  # Soft, soothing rose tint instead of harsh red
    bg_overlay = "rgba(226, 182, 182, 0.04)"
    border_style = "rgba(226, 182, 182, 0.3)"
    ai_directive = "Elevated biometric stress profile identified. Interface execution minimized by 65% to reduce visual complexity. Activating cabin active noise cancellation, initiating localized thermal reduction via seating grid, and transitioning display metrics to high-contrast, large-format serif typography."
elif heart_rate >= 95 or speed > 130:
    state_label = "System Directive: High-Performance Engagement Mode"
    accent_color = "#ebd5b3"  # Elegant Warm Champagne instead of electric blue
    bg_overlay = "rgba(235, 213, 179, 0.04)"
    border_style = "rgba(235, 213, 179, 0.3)"
    ai_directive = "High-velocity focus threshold achieved. Reconfiguring visual hierarchy to prioritize direct driving vectors, dynamic longitudinal forces, and apex pacing data. Suppressing non-essential media assets and environmental telemetry."
else:
    state_label = "System Directive: Balanced Cruising Environment"
    accent_color = "#b3ebd5"  # Relaxing, premium Sage Green
    bg_overlay = "rgba(179, 235, 213, 0.04)"
    border_style = "rgba(179, 235, 213, 0.3)"
    ai_directive = "Biometric baselines optimal. The full interface ecosystem is deployed. Comfort automation is active, presenting rich navigation mapping, ambient media selections, and holistic vehicle diagnostics tailored to the current route profile."

# Render Clean, Premium Status Banner
st.markdown(f"""
    <div class="status-banner" style="background: {bg_overlay}; border: 1px solid {border_style};">
        <div class="status-title" style="color: {accent_color};">{state_label}</div>
        <p style="color: #cbd5e1; font-family: 'Lora'; font-size: 15px; margin: 0; line-height: 1.6; font-style: italic;"><b>AI Automation Matrix:</b> {ai_directive}</p>
    </div>
    """, unsafe_allow_html=True)

# Telemetry Grid
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="metric-box">
            <p style="font-family: 'Playfair Display'; font-size: 14px; color: #94a3b8; letter-spacing: 0.5px; margin:0; font-style: italic;">Physiological Feed</p>
            <p style="font-family: 'Playfair Display'; font-size: 46px; font-weight: 400; color: #ffffff; margin: 15px 0 5px 0;">{heart_rate} <span style="font-size:16px; color:{accent_color}; font-family:'Lora';">BPM</span></p>
            <p style="font-size: 12px; color: #64748b; margin:0; font-family:'Lora';">Steering Integrated Sensor Arrays</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-box">
            <p style="font-family: 'Playfair Display'; font-size: 14px; color: #94a3b8; letter-spacing: 0.5px; margin:0; font-style: italic;">Velocity Matrix</p>
            <p style="font-family: 'Playfair Display'; font-size: 46px; font-weight: 400; color: #ffffff; margin: 15px 0 5px 0;">{speed} <span style="font-size:16px; color:{accent_color}; font-family:'Lora';">MPH</span></p>
            <p style="font-size: 12px; color: #64748b; margin:0; font-family:'Lora';">Internal CAN-Bus Telemetry</p>
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-box">
            <p style="font-family: 'Playfair Display'; font-size: 14px; color: #94a3b8; letter-spacing: 0.5px; margin:0; font-style: italic;">Inertial Forces</p>
            <p style="font-family: 'Playfair Display'; font-size: 46px; font-weight: 400; color: #ffffff; margin: 15px 0 5px 0;">{g_force:.1f} <span style="font-size:16px; color:{accent_color}; font-family:'Lora';">G</span></p>
            <p style="font-size: 12px; color: #64748b; margin:0; font-family:'Lora';">Digital Tri-Axis Accelerometer</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#475569; font-size:13px; font-style:italic;'>Designed for Aston Martin / Bentley Future Lab Research Case Study Portfolio</p>", unsafe_allow_html=True)
