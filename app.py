import streamlit as st
from openai import OpenAI
import os

# إعدادات الواجهة السيادية
st.set_page_config(page_title="VeriAnchor Sovereign", page_icon="🛡️")

# سحب المفاتيح (المفتاح الصح OpenAI)
api_key = os.environ.get("OPENAI_API_KEY")
access_token = os.environ.get("ACCESS_TOKEN")

st.title("🛡️ VeriAnchor: iAM-Sovereign")
st.caption("Patent Pending: 1660 | Powered by OpenAI")

# بوابة الدخول
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    pwd = st.text_input("كود المرور (ACCESS_TOKEN):", type="password")
    if st.button("دخول"):
        if pwd == access_token:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("الكود غلط يا مصطفى")
    st.stop()

# نظام الشات
client = OpenAI(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("أصدر أوامرك..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "أنت i-AM 1660، نظام سيادي ذكي لمصطفى جمال."}, 
                      *st.session_state.messages]
        )
        reply = response.choices[0].message.content
        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
