import streamlit as st

# Set page layout to wide and title
st.set_page_config(page_title="BIO-DRIVE // Next-Gen HMI", layout="wide")

# Injecting aggressive, premium automotive styling (Dark mode, Neon accents, glowing cards)
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@500;700&display=swap" rel="stylesheet">
    
    <style>
    /* Main Background Overrides */
    .stApp {
        background-color: #060913 !important;
        color: #e2e8f0;
        font-family: 'Rajdhani', sans-serif;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #0b1120 !important;
        border-right: 1px solid #1e293b;
    }
    
    /* Title Styling */
    .title-text {
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        letter-spacing: 3px;
        text-align: center;
        background: linear-gradient(45deg, #00f0ff, #ff007f);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    
    /* Custom Telemetry Card Styling */
    .metric-box {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .metric-box:hover {
        transform: translateY(-2px);
    }
    
    /* Dynamic AI Status Layout */
    .status-banner {
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 30px;
        font-family: 'Orbitron', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# App Headers
st.markdown('<h1 class="title-text">BIO-DRIVE : COCKPIT OS</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#64748b; font-family:\'Orbitron\'; font-size:11px; letter-spacing:2px; margin-bottom:40px;">AI-ADAPTIVE HUMAN-MACHINE INTERFACE // UX RESEARCH PROTOTYPE</p>', unsafe_allow_html=True)

# Sidebar Control Panel
st.sidebar.markdown('<h2 style="font-family:\'Orbitron\'; font-size:18px; color:#00f0ff; letter-spacing:1px;">🎛️ BIOMETRIC SIMULATION</h2>', unsafe_allow_html=True)
st.sidebar.markdown('<p style="color:#64748b; font-size:13px;">Adjust inputs to simulate driver physical state.</p>', unsafe_allow_html=True)

heart_rate = st.sidebar.slider("Driver Heart Rate (BPM)", 60, 180, 75)
speed = st.sidebar.slider("Vehicle Speed (MPH)", 0, 240, 65)
g_force = st.sidebar.slider("Lateral Force (G)", 0.0, 5.2, 0.9, step=0.1)

# AI Logic Processing Matrix
if heart_rate > 130:
    driver_state = "🚨 EMERGENCY: STRESS MITIGATION ACTIVATED"
    accent_color = "#ff0055"
    glow_shadow = "rgba(255, 0, 85, 0.2)"
    ai_directive = "CRITICAL COGNITIVE OVERLOAD. Minimizing HMI surface area by 70% to reduce visual panic. Shifting ambient cockpit lighting to 430nm calming green. Maximizing cluster typeface geometry (+30%) for instant glance legibility. Muting all non-tactical notifications."
elif heart_rate >= 95 or speed > 130:
    driver_state = "🏁 STATE: TARGET FOCUS / TRACK MODE"
    accent_color = "#00f0ff"
    glow_shadow = "rgba(0, 240, 255, 0.2)"
    ai_directive = "HIGH VIGILANCE DETECTED. Reconfiguring interface for dynamic racing telemetry. Projecting shift-point vectors onto primary HUD plane. De-prioritizing secondary media, climate, and map assets. Steering feedback stiffened by 15%."
else:
    driver_state = "🚙 STATE: OPTIMAL / COMFORT CRUISING"
    accent_color = "#00ff66"
    glow_shadow = "rgba(0, 255, 102, 0.2)"
    ai_directive = "BIOMETRIC BASELINE STABLE. Activating full ambient infotainment layer. Displaying media carousels, detailed route terrain mapping, and cabin comfort controls. System operating in highly contextual predictive assistance mode."

# Render Dynamic Status Banner
st.markdown(f"""
    <div class="status-banner" style="background: rgba({int(accent_color[1:3],16)}, {int(accent_color[3:5],16)}, {int(accent_color[5:7],16)}, 0.05); border: 1px solid {accent_color}; box-shadow: 0 0 20px {glow_shadow};">
        <h3 style="color: {accent_color}; margin: 0 0 10px 0; font-size: 16px; letter-spacing:1px;">{driver_state}</h3>
        <p style="color: #94a3b8; font-family: 'Rajdhani'; font-size: 16px; margin: 0; line-height: 1.5;"><b>AI Core Directive:</b> {ai_directive}</p>
    </div>
    """, unsafe_allow_html=True)

# Telemetry HUD Grid Layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="metric-box" style="border-top: 3px solid {accent_color};">
            <p style="font-family: 'Orbitron'; font-size: 12px; color: #64748b; letter-spacing: 1px; margin:0;">BIOMETRIC FEED</p>
            <p style="font-family: 'Orbitron'; font-size: 42px; font-weight: 900; color: #ffffff; margin: 10px 0 5px 0;">{heart_rate} <span style="font-size:16px; color:{accent_color}; font-weight:400;">BPM</span></p>
            <p style="font-size: 12px; color: #475569; margin:0;">Source: Steering Wheel ECG Mesh</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-box" style="border-top: 3px solid {accent_color};">
            <p style="font-family: 'Orbitron'; font-size: 12px; color: #64748b; letter-spacing: 1px; margin:0;">CAN-BUS VELOCITY</p>
            <p style="font-family: 'Orbitron'; font-size: 42px; font-weight: 900; color: #ffffff; margin: 10px 0 5px 0;">{speed} <span style="font-size:16px; color:{accent_color}; font-weight:400;">MPH</span></p>
            <p style="font-size: 12px; color: #475569; margin:0;">Source: Active Drivetrain Telemetry</p>
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-box" style="border-top: 3px solid {accent_color};">
            <p style="font-family: 'Orbitron'; font-size: 12px; color: #64748b; letter-spacing: 1px; margin:0;">LATERAL FORCE</p>
            <p style="font-family: 'Orbitron'; font-size: 42px; font-weight: 900; color: #ffffff; margin: 10px 0 5px 0;">{g_force:.1f} <span style="font-size:16px; color:{accent_color}; font-weight:400;">G</span></p>
            <p style="font-size: 12px; color: #475569; margin:0;">Source: IMU Digital Inertial Sensor</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("⚙️ **UX Evaluation Matrix:** This interactive architecture validates how multi-modal sensor arrays can feed a predictive vehicle environment. By mapping physiological driver stress markers against mechanical velocity parameters, the system eliminates UI latency and drastically drops visual distraction metrics during critical driving events.")
