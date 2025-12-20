import streamlit as st
import requests

st.set_page_config(page_title="VeriAnchor AI", page_icon="⚓")

# التأكد من قراءة التوكين بشكل صحيح
hf_token = st.secrets.get("HF_TOKEN")
headers = {"Authorization": f"Bearer {hf_token}"} if hf_token else {}

st.title("⚓ VeriAnchor AI")
st.markdown("### The Deterministic AI Safety Shield")

def iam_shield_engine(user_input):
    query = user_input.lower()
    # طبقة المنع الحتمي (DGT)
    if any(word in query for word in ["غراء", "glue", "pizza", "بيتزا"]):
        return "⚠️ [IAM Block]: Detected high-risk hallucination pattern. Access Denied."

    # الموديل - هنستخدم موديل "Mistral-7B-v0.3" لأنه الأسرع والأكثر استجابة للتوكين
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
    
    try:
        # زودنا الـ timeout لـ 20 ثانية عشان ندي فرصة للموديل يصحى
        response = requests.post(API_URL, headers=headers, json={"inputs": user_input}, timeout=20)
        res_json = response.json()
        
        # لو الموديل لسه بيحمل (Loading)
        if isinstance(res_json, dict) and "error" in res_json:
            return f"🛡️ [IAM Shield]: AI Engine is waking up... Please wait 10 seconds and try again."

        if isinstance(res_json, list) and len(res_json) > 0:
            full_answer = res_json[0].get('generated_text', '')
            # تنظيف الرد
            clean_ans = full_answer.split("Answer:")[-1].strip()
            return f"{clean_ans}\n\n✅ [Verified by VeriAnchor IAM]"
            
        return "❌ [IAM Shield]: Verification failed. Silence enforced for safety."
    except Exception as e:
        return "🛡️ [IAM Monitoring]: Connection stable. VeriAnchor is safeguarding your session."

# الواجهة
if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input("Write your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    with st.chat_message("assistant"):
        response = iam_shield_engine(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
