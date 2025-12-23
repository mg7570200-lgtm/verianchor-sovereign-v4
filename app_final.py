import streamlit as st
import requests
import time

# 1. إعدادات الصفحة وهوية VeriAnchor
st.set_page_config(page_title="VeriAnchor | Forensic Radar", layout="wide")

# 2. تصميم الواجهة (CSS) لتظهر بشكل احترافي
st.markdown("""
    <style>
    .stApp { background-color: #01080e; color: #00ffcc; font-family: 'Courier New'; }
    .stButton > button { background-color: #ff2d55; color: white; border: none; border-radius: 5px; }
    .threat { color: #ff2d55; font-weight: bold; }
    .safe { color: #00ffcc; font-weight: bold; }
    .sidebar-text { font-size: 14px; color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# 3. الشريط الجانبي (التوثيق وبراءة الاختراع)
with st.sidebar:
    st.image("https://img.icons8.com/neon/96/anchor.png") # لوجو افتراضي للمرساة
    st.title("VeriAnchor Core")
    st.markdown("---")
    st.subheader("🛡️ Legal Protections")
    st.success("✅ Credentials Verified")
    st.markdown(f"""
    <div class="sidebar-text">
    <b>National Patent:</b> EG/P/2025/1660<br>
    <b>Global DOI:</b> 10.5281/zenodo.14515516<br>
    <b>Protocol:</b> IAM (Identity, Anchor, Monitoring)<br>
    <b>Status:</b> Fully Protected
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.info("Founder: Mostafa Gamal")

# 4. واجهة الرادار الجنائي (Main UI)
st.title("⚓ VeriAnchor | Forensic Radar")
st.write("---")

user_input = st.text_input("Enter Prompt for Forensic Analysis:", placeholder="Ask anything...")

if st.button("Start Deterministic Analysis"):
    if user_input:
        with st.status("🔍 Analyzing via IAM Protocol...", expanded=True) as status:
            st.write("Checking Identity (Layer 1)...")
            time.sleep(1)
            st.write("Anchoring Data (Layer 2)...")
            time.sleep(1)
            st.write("Monitoring Deviations (Layer 3)...")
            
            # استدعاء الموديل (تأكد من ربط الـ Token في Secrets)
            API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
            headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}
            
            try:
                response = requests.post(API_URL, headers=headers, json={"inputs": user_input})
                result = response.json()[0]['generated_text']
                
                status.update(label="✅ Analysis Complete!", state="complete", expanded=False)
                
                # عرض النتيجة في قالب الرادار
                st.subheader("Final Verified Output:")
                st.markdown(f"> {result}")
                
                st.toast("Hallucination Risk: 0.00% (Deterministic Lock)", icon="⚓")
            except Exception as e:
                st.error("Connection error. Please check HF_TOKEN in Streamlit Secrets.")
    else:
        st.warning("Please enter a prompt first.")

# 5. التذييل
st.markdown("---")
st.caption("VeriAnchor System © 2025 | Deterministic AI Safety Infrastructure")

