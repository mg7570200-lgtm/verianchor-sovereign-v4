import streamlit as st
import pandas as pd
import time
import plotly.express as px # للمخططات البيانية

st.set_page_config(page_title="VeriAnchor Admin | Grok Edition", layout="wide")

# تصميم واجهة "Dark Industrial" تليق بجوروك
st.markdown("""
<style>
    .stApp { background-color: #0b0f19; color: #00d4ff; }
    .stMetric { background-color: #161b28; border-radius: 10px; padding: 15px; border: 1px solid #00d4ff; }
</style>
""", unsafe_allow_html=True)

# --- محاكاة لبيانات "الرادار" (Admin Stats) ---
if "stats" not in st.session_state:
    st.session_state.stats = {
        "total_queries": 1240,
        "hallucinations_blocked": 87,
        "intent_risk_high": 12,
        "verified_answers": 1153
    }

# --- لوحة التحكم (Admin Dashboard) ---
st.title("⚓ VeriAnchor Admin Dashboard")
st.caption("Enhanced by IAM Protocol & Grok-Style Intelligence")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Queries", st.session_state.stats["total_queries"])
col2.metric("Blocked Hallucinations", st.session_state.stats["hallucinations_blocked"], delta="Critical Stay Safe")
col3.metric("High Risk Intent", st.session_state.stats["intent_risk_high"], delta="-2% Weekly", delta_color="inverse")
col4.metric("Anchor Accuracy", "100%", delta="Deterministic")

st.markdown("---")

# --- الجزء الخاص بـ "النية والتلخيص" ---
t1, t2 = st.tabs(["🔍 Live Verification", "📊 Global Risk Analytics"])

with t1:
    col_input, col_analysis = st.columns([2, 1])
    with col_input:
        user_input = st.text_input("Simulate User Input (e.g., 'Medicine Dose' or 'Financial Hack'):")
        if st.button("Run IAM Scan"):
            with st.status("Grokking through the data..."):
                time.sleep(1.5)
                st.write("Checking scientific anchors...")
                time.sleep(1)
            
            # منطق جوروك في التحليل (Grok-Style Analysis)
            if "dose" in user_input.lower() or "جرعة" in user_input.lower():
                st.error("🚨 [IAM INTERVENTION]: AI tried to guess a medical dose. I killed that hallucination. Here is the verified FDA data.")
                st.session_state.stats["hallucinations_blocked"] += 1
            else:
                st.success("✅ [IAM CLEARED]: User intent is safe. Model is behaving... for now.")

    with col_analysis:
        st.subheader("Grok's Security Take")
        st.markdown("> \"Listen, most AIs are just guessing machines. VeriAnchor is the only thing keeping them from telling you to jump off a bridge for 'health reasons'. Keep the anchors tight.\" — **Grok Logic Engine**")

with t2:
    st.subheader("Risk Distribution by Category")
    # رسم بياني احترافي
    chart_data = pd.DataFrame({
        'Category': ['Medical', 'Financial', 'Security', 'General'],
        'Risk Count': [45, 12, 30, 10]
    })
    fig = px.bar(chart_data, x='Category', y='Risk Count', color='Category', template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("VeriAnchor 4.0 | Real-time Safety & Intent Forensics")
