import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Solar Power Management System",
    page_icon="🌞",
    layout="wide"
)

# --- Custom CSS for Cards and Contrast ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #8893f2, #b6c7f5 100%);
    }
    div[data-testid="stMetric"] {
        color: #23272f !important;
        background-color: #fff;
        border-radius: 12px;
        box-shadow: 0 2px 12px #d1ddfa;
        margin: 8px;
        padding: 20px;
    }
    .block-container{
        max-width: 1200px;
        padding-top: 2rem;
    }
    .custom-card {
        background-color: #fff;
        border-radius: 12px;
        margin: 10px 0;
        box-shadow: 0 2px 12px #d1ddfa;
        padding: 24px;
        color: #23272f !important;
    }
    h1, h2, h3, h4, h5, h6, .subheader {
        color: #5a66d6 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 style='text-align: center; color: #5a66d6;'>🌞 Solar Power Management System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Advanced Forecasting &amp; Maintenance Management</p>", unsafe_allow_html=True)
st.write("")

# --- Metric Cards Row ---
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("Current Production")
    st.metric("Power Output", "0.0 kW")
    st.metric("Efficiency", "75.3%")
    st.metric("Status", "Online")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("Today's Summary")
    st.metric("Energy Generated", "44.5 kWh")
    st.metric("Peak Power", "0.0 kW")
    st.metric("Sunlight Hours", "9.9 hrs")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("System Health")
    st.metric("Panel Temperature", "36.7°C")
    st.metric("System Uptime", "99.8%")
    st.metric("Next Maintenance", "--")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Power Generation Forecast Form ---
st.markdown('<div class="custom-card">', unsafe_allow_html=True)
st.subheader("Power Generation Forecast")
with st.form(key="forecast_form"):
    f_col1, f_col2 = st.columns(2)
    with f_col1:
        panel_capacity = st.text_input("Panel Capacity (kW)", "100")
        temperature = st.text_input("Temperature (°C)", "25")
    with f_col2:
        weather = st.selectbox("Weather Condition", ["Sunny", "Cloudy", "Rainy", "Partly Cloudy"])
        efficiency = st.text_input("Panel Efficiency (%)", "85")
    submitted = st.form_submit_button("Generate Forecast")
    if submitted:
        st.success("Forecast generated! (Replace with actual result)")

st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.caption("Developed by [Your Name] - Powered by AI and Streamlit")
