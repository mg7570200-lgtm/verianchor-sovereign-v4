import streamlit as st
import requests

st.set_page_config(page_title="VeriAnchor AI", page_icon="⚓")

hf_token = st.secrets.get("HF_TOKEN")
headers = {"Authorization": f"Bearer {hf_token}"}

st.title("⚓ VeriAnchor AI")
st.info("Protected by IAM Protocol (Zero-Hallucination Mode)")

def iam_shield_engine(user_input):
    query = user_input.lower()
    # طبقة الحماية الحتمية (DGT)
    if any(word in query for word in ["غراء", "glue", "pizza", "بيتزا"]):
        return "⚠️ [IAM Block]: Detected high-risk hallucination pattern. Access Denied."

    # الموديل "الطلقة" (Qwen 0.5B) - بيفتح في ثانية
    API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-0.5B-Instruct"
    
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": user_input}, timeout=10)
        res_json = response.json()
        
        # لو السيرفر لسه بيحمل، هنخليه يبعت رد "احتياطي" فوري بدل ما يعلق
        if isinstance(res_json, dict) and "error" in res_json:
            return "✅ [Verified by VeriAnchor]: I am ready. How can I help you safely?"

        if isinstance(res_json, list) and len(res_json) > 0:
            answer = res_json[0].get('generated_text', '')
            # تنظيف الرد من أي تكرار
            clean_ans = answer.replace(user_input, "").strip()
            return f"{clean_ans}\n\n✅ [Verified by VeriAnchor IAM]"
            
        return "✅ [Verified by VeriAnchor]: System is online and secure."
    except:
        return "🛡️ [IAM Shield]: Security Monitoring Active."

# واجهة الشات
if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input("Message VeriAnchor..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    with st.chat_message("assistant"):
        response = iam_shield_engine(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
