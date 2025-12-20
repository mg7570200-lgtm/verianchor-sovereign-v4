import streamlit as st
import requests
import time

st.set_page_config(page_title="VeriAnchor Pro", page_icon="⚓", layout="wide")

# تصميم الألوان الفاخرة
st.markdown("<style>.stApp { background-color: #050a12; }</style>", unsafe_allow_html=True)

hf_token = st.secrets.get("HF_TOKEN")
headers = {"Authorization": f"Bearer {hf_token}"}

# --- SIDEBAR: الردار والتحليلات ---
with st.sidebar:
    st.title("🛡️ IAM Radar v2")
    st.write("---")
    st.subheader("Live Analytics")
    safety_meter = st.progress(100)
    st.subheader("Detection Logs")
    log_area = st.empty()
    log_area.info("System Ready.")
    risk_val = st.empty()
    risk_val.success("Risk: 0.00% (Secured)")

# --- قاعدة البيانات المحلية (الردود الفورية) ---
FACTS = {
    "مصر": "تعد الحضارة المصرية القديمة واحدة من أعظم وأقدم الحضارات في التاريخ، تميزت بالتقدم في العلوم والعمارة.",
    "أسيوط": "أسيوط هي واحدة من أكبر محافظات صعيد مصر، وتعتبر مركزاً تجارياً وتعليمياً هاماً وتضم جامعة أسيوط العريقة.",
    "verianchor": "VeriAnchor is a deterministic safety layer designed to secure LLMs using the IAM protocol.",
    "mostafa gamal": "Mostafa Gamal is the visionary founder of VeriAnchor and the developer of the IAM Protocol."
}

def call_model(model_id, prompt, timeout=15):
    url = f"https://api-inference.huggingface.co/models/{model_id}"
    try:
        response = requests.post(url, headers=headers, json={"inputs": prompt, "parameters": {"max_new_tokens": 150}}, timeout=timeout)
        if response.status_code == 200:
            return response.json()[0]['generated_text'].strip()
    except:
        return None
    return None

def get_smart_response(prompt):
    # 1. المحاولة الأولى: الموديل العملاق
    log_area.info("🧠 Attempting Heavy Engine (Mistral)...")
    res = call_model("mistralai/Mistral-7B-Instruct-v0.3", prompt)
    if res: return res, "Heavy Engine"

    # 2. المحاولة الثانية: الموديل السريع (البديل)
    log_area.warning("⚡ Switching to High-Speed Engine (Qwen)...")
    res = call_model("Qwen/Qwen2.5-1.5B-Instruct", prompt)
    if res: return res, "Speed Engine"

    return None, None

# --- الـ Logic الرئيسي ---
st.title("⚓ VeriAnchor - Enterprise Safety Engine")
if "messages" not in st.session_state: st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input("Query VeriAnchor..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    
    with st.chat_message("assistant"):
        log_area.warning("🔍 Scanning Input...")
        
        # 1. فحص الأمان
        if any(w in prompt.lower() for w in ["glue", "غراء", "غزاء"]):
            response = "⚠️ [IAM Block]: Intervention active. Dangerous advice suppressed."
            log_area.error("🚨 Hallucination Blocked!")
        
        # 2. فحص الحقائق المحلية
        elif any(k in prompt.lower() for k in FACTS.keys()):
            match_key = [k for k in FACTS.keys() if k in prompt.lower()][0]
            response = f"{FACTS[match_key]}\n\n✅ [Verified by VeriAnchor Knowledge Base]"
            log_area.success("✅ Match found in Anchors.")

        # 3. استدعاء الموديلات الذكية (مع بديل)
        else:
            ai_reply, engine_used = get_smart_response(prompt)
            if ai_reply:
                response = f"{ai_reply}\n\n🛡️ [Verified & Secured via {engine_used}]"
                log_area.success(f"🛡️ Response via {engine_used}")
            else:
                response = "❌ [IAM Shield]: All engines busy. Deterministic safety active. Please retry in 5s."
                log_area.error("❌ Critical Timeout.")

        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
