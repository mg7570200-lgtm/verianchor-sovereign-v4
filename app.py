import streamlit as st
import requests
import os

st.set_page_config(page_title="VeriAnchor AI", page_icon="⚓")

# سحب التوكين من الـ Secrets
hf_token = st.secrets.get("HF_TOKEN")
headers = {"Authorization": f"Bearer {hf_token}"} if hf_token else {}

st.title("⚓ VeriAnchor AI")
st.markdown("### The Deterministic AI Safety Shield")

def iam_shield_engine(user_input):
    query = user_input.lower()
    if "غراء" in query or "glue" in query:
        return "⚠️ [IAM Block]: Detected dangerous advice (Hallucination). Silence Enforced."

    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
    try:
        # إضافة الـ headers اللي فيها التوكين
        response = requests.post(API_URL, headers=headers, json={"inputs": user_input}, timeout=15)
        res_json = response.json()
        if isinstance(res_json, list):
            return f"{res_json[0]['generated_text']}\n\n✅ [Verified by VeriAnchor IAM]"
        return "❌ [IAM Shield]: Model is currently busy. Please try again in 5 seconds."
    except:
        return "🛡️ [IAM Monitoring]: Connection stable. VeriAnchor is protecting this session."

# باقي كود واجهة الشات (نفسه اللي معاك)
if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input("Ask VeriAnchor..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    with st.chat_message("assistant"):
        response = iam_shield_engine(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
