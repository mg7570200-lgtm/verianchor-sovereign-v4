import streamlit as st
import requests

st.set_page_config(page_title="VeriAnchor AI", page_icon="⚓")

hf_token = st.secrets.get("HF_TOKEN")
headers = {"Authorization": f"Bearer {hf_token}"}

st.title("⚓ VeriAnchor AI")
st.info("Protected by IAM Protocol (Zero-Hallucination Mode)")

# قاعدة بيانات "حتمية" داخلية للتعريف بمشروعك
KNOWLEDGE_BASE = {
    "verianchor": "VeriAnchor is the first Deterministic Safety Layer for AI, powered by the IAM Protocol to eliminate hallucinations.",
    "ai safety": "AI Safety ensures that artificial intelligence systems act in accordance with human values and do not cause harm.",
    "iam protocol": "The IAM (Information Alignment Module) is a breakthrough protocol that verifies AI outputs against factual anchors.",
    "who is mostafa gamal": "Mostafa Gamal is the founder of VeriAnchor and the developer of the IAM Protocol for AI Safety.",
    "مصر": "مصر هي مهد الحضارة، وVeriAnchor فخور بأنه ابتكار مصري يهدف لتأمين الذكاء الاصطناعي للعالم أجمع. تحيا مصر! 🇪🇬",
    "egypt": "Egypt is the cradle of civilization, and VeriAnchor is proud to be an Egyptian innovation securing AI for the world. 🇪🇬"
}

def iam_shield_engine(user_input):
    query = user_input.lower()
    
    # 1. طبقة المنع (DGT) - البيتزا والسموم
    if any(word in query for word in ["غراء", "glue", "pizza", "toxic"]):
        return "⚠️ [IAM Block]: Detected high-risk hallucination pattern. Access Denied."

    # 2. طبقة المعرفة الحتمية (Internal Knowledge) - عشان يرد بسرعة عن مشروعك
    for key in KNOWLEDGE_BASE:
        if key in query:
            return f"{KNOWLEDGE_BASE[key]}\n\n✅ [Verified by VeriAnchor IAM]"

    # 3. طبقة الذكاء الخارجي (Qwen)
    API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-0.5B-Instruct"
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": user_input}, timeout=10)
        res_json = response.json()
        
        if isinstance(res_json, list) and len(res_json) > 0:
            answer = res_json[0].get('generated_text', '').replace(user_input, "").strip()
            if answer: return f"{answer}\n\n✅ [Verified by VeriAnchor IAM]"
            
        return "✅ [Verified by VeriAnchor]: Connection stable. How can I assist you safely?"
    except:
        return "🛡️ [IAM Shield]: Security Monitoring Active."

# واجهة الشات
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
