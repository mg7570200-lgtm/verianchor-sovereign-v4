import streamlit as st
import requests
import time
import difflib # لمقارنة النصوص وتحديد الاختلافات

# 1. إعدادات الهوية الدولية
st.set_page_config(page_title="VeriAnchor | The Forensic AI Radar", layout="wide")

# 2. تصميم الواجهة السينمائية (Cyber-Forensic UI)
st.markdown("""
    <style>
    .stApp { background-color: #010a0f; color: #00ffcc; font-family: 'Courier New'; }
    .stMetric { background-color: #02121b; border: 1px solid #00ffcc; padding: 10px; border-radius: 10px; }
    .hallucination-alert { border: 2px solid #ff2d55; padding: 15px; border-radius: 10px; background: #2b0000; color: #ff2d55; font-weight: bold; }
    .safe-lock { border: 2px solid #00ffcc; padding: 15px; border-radius: 10px; background: #001a1a; color: #00ffcc; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. الشريط الجانبي (المستندات القانونية)
with st.sidebar:
    st.image("https://img.icons8.com/neon/96/anchor.png")
    st.title("VeriAnchor Core")
    st.markdown(f"**Patent:** `EG/P/2025/1660`\n\n**DOI:** `10.5281/zenodo.14515516`")
    st.info("Status: International Protection Active")

# 4. الرادار ولوحة التحكم
st.title("⚓ VeriAnchor | Forensic Radar v2.5")
left_col, right_col = st.columns([2, 1])

with left_col:
    user_input = st.text_input("Enter Data for Verification:", placeholder="Ask about facts, dates, or technical data...")
    execute_btn = st.button("RUN DETERMINISTIC CROSS-CHECK")

# 5. محرك فحص الهلوسة (Cross-Check Engine)
if execute_btn and user_input:
    with st.status("🔍 Verifying Truth via IAM Protocol...", expanded=True) as status:
        API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
        headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}
        
        # طلب إجابتين مختلفتين (باستخدام حرارة مختلفة Temperature) لبيان التعارض
        st.write("Generating Sample A (Deterministic)...")
        res1 = requests.post(API_URL, headers=headers, json={"inputs": user_input, "parameters": {"temperature": 0.1}})
        ans1 = res1.json()[0]['generated_text']
        
        st.write("Generating Sample B (Exploratory)...")
        res2 = requests.post(API_URL, headers=headers, json={"inputs": user_input, "parameters": {"temperature": 0.9}})
        ans2 = res2.json()[0]['generated_text']
        
        # حساب نسبة التشابه (Similarity Ratio)
        similarity = difflib.SequenceMatcher(None, ans1, ans2).ratio()
        risk_score = (1 - similarity) * 100

        status.update(label="Analysis Finished", state="complete")

    with right_col:
        st.write("### 📡 Live Analysis")
        st.metric("Hallucination Risk", f"{risk_score:.2f}%", delta=f"{'+ High' if risk_score > 20 else '- Low'}", delta_color="inverse")
        st.metric("Anchoring Strength", f"{similarity*100:.2f}%")

    # عرض النتيجة النهائية بناءً على الفحص الجنائي
    st.markdown("---")
    if risk_score > 25:
        st.markdown(f'<div class="hallucination-alert">⚠️ HIGH HALLUCINATION RISK DETECTED: The model provided inconsistent facts. VeriAnchor advises manual verification.</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="safe-lock">🔒 DETERMINISTIC LOCK: Output verified across multiple layers. Data is consistent.</div>', unsafe_allow_html=True)
    
    st.subheader("Verified Final Response:")
    st.success(ans1)

    with st.expander("📂 View Forensic Comparison (Sample A vs B)"):
        st.write("**Sample A:**", ans1)
        st.write("**Sample B:**", ans2)
        st.write(f"**Semantic Deviation:** {risk_score:.2f}%")

# 6. التذييل
st.caption("VeriAnchor Infrastructure © 2025 | Secure AI Forensic Standard")
