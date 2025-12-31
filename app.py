import streamlit as st
from openai import OpenAI
import os

# إعدادات الهوية
st.set_page_config(page_title="VeriAnchor Sovereign", page_icon="🛡️")
st.title("🛡️ VeriAnchor: iAM-Sovereign")
st.caption("Patent Pending: EG/P/2025/1660 | Official Secure Portal")

# سحب المفاتيح
OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

# بوابة الدخول
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    pwd = st.text_input("كود المرور السيادي:", type="password")
    if st.button("دخول"):
        if pwd == ACCESS_TOKEN:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("❌ الكود خطأ")
    st.stop()

# تشغيل الشات بمفتاحك
client = OpenAI(api_key=OPENAI_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("أصدر أوامرك..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "أنت i-AM 1660، النظام السيادي لمصطفى جمال."},
                  *st.session_state.messages]
    )
    reply = response.choices[0].message.content
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
