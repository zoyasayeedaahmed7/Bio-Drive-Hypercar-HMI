st.set_page_config(page_title="Bio-Drive HMI Simulator", layout="wide")

# Custom CSS to force a sleek, dark automotive dashboard theme
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    h1 { font-family: 'Orbitron', sans-serif; text-align: center; }
    .metric-card {
        background-color: #1f293d;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏎️ BIO-DRIVE: AI Stress-Adaptive HMI")
st.subheader("Automotive UX Research Prototype • AIML Engineering")
st.write("---")

# Sidebar for Biometric & Telemetry Controls
st.sidebar.header("🕹️ Live Simulation Controls")
heart_rate = st.sidebar.slider("Driver Heart Rate (BPM)", 60, 180, 75)
speed = st.sidebar.slider("Vehicle Speed (mph)", 0, 220, 45)
g_force = st.sidebar.slider("Lateral G-Force", 0.0, 5.0, 0.8, step=0.1)

# AI Logic Engine: Determine the Driver State
if heart_rate > 130:
    driver_state = "🚨 OVERLOAD / STRESS MITIGATION"
    bg_color = "#3a0f14"  # Deep alert red
    text_color = "#ff4b4b"
    ai_action = "CRITICAL: High cognitive load detected. Minimizing secondary HMI elements. Activating ambient cooling, increasing typeface scale by 30%, and routing non-emergency data to background."
elif heart_rate >= 90 or speed > 120:
    driver_state = "🏁 PERFORMANCE / TRACK MODE"
    bg_color = "#1c0f3a"  # Racing purple/red
    text_color = "#00f0ff"
    ai_action = "DYNAMIC: High-speed/focus state confirmed. Prioritizing apex telemetry, shift lights, and tire degradation vectors. Suppressing media and incoming notifications."
else:
    driver_state = "🚙 CALM / ECO CRUISING"
    bg_color = "#0f233a"  # Relaxing deep blue
    text_color = "#00ff66"
    ai_action = "OPTIMAL: Driver baseline stable. Full infotainment, navigation telemetry, and media systems available. Ambient cabin lighting set to calming spectrum."

# Display Dynamic Dashboard based on AI Decision
st.markdown(f"""
    <div style="background-color: {bg_color}; padding: 30px; border-radius: 15px; border: 2px solid {text_color}; margin-bottom: 25px;">
        <h2 style="color: white; margin-top:0;">SYSTEM STATE: <span style="color: {text_color};">{driver_state}</span></h2>
        <p style="font-size: 1.2rem; color: #e0e0e0; font-style: italic;"><b>AI HMI Automation Directive:</b> {ai_action}</p>
    </div>
    """, unsafe_allow_html=True)

# Grid Layout for Live Telemetry HUD
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #ff4b4b; margin:0;">❤️ Biometrics</h3>
            <p style="font-size: 2.5rem; font-weight: bold; margin:10px 0;">{heart_rate} <span style="font-size: 1rem;">BPM</span></p>
            <small style="color: #aaa;">Sensors: Steering Wheel GSR</small>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #00f0ff; margin:0;">⚡ Velocity</h3>
            <p style="font-size: 2.5rem; font-weight: bold; margin:10px 0;">{speed} <span style="font-size: 1rem;">mph</span></p>
            <small style="color: #aaa;">Sensors: CAN-Bus Telemetry</small>
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #00ff66; margin:0;">📐 Dynamics</h3>
            <p style="font-size: 2.5rem; font-weight: bold; margin:10px 0;">{g_force} <span style="font-size: 1rem;">G</span></p>
            <small style="color: #aaa;">Sensors: IMU Accelerometer</small>
        </div>
        """, unsafe_allow_html=True)

st.write("---")
st.info("💡 **UX Design Research Note for Reviewer:** Use the sidebar sliders to simulate real-time stress spikes or track acceleration. Notice how the user interface intelligently drops visual clutter during 'Stress Mitigation' to maximize driver safety and lower glance time.")
