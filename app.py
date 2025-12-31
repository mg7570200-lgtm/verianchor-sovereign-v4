import streamlit as st
from openai import OpenAI
import os

# 1. إعدادات الهوية
st.set_page_config(page_title="VeriAnchor Sovereign", page_icon="🛡️")
st.title("🛡️ VeriAnchor: iAM-Sovereign")
st.caption("Patent Pending: EG/P/2025/1660 | Official Secure Portal")

# 2. سحب المفاتيح (من الملف اللي إنت لسه عامله بنجاح)
try:
    OPENAI_KEY = st.secrets["OPENAI_API_KEY"]
    ACCESS_TOKEN = st.secrets["ACCESS_TOKEN"]
except Exception:
    st.error("❌ المفاتيح غير مفعلة في secrets.toml")
    st.stop()

# 3. بوابة الدخول
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    pwd = st.text_input("كود المرور السيادي (iAM):", type="password")
    if st.button("تفعيل البروتوكول"):
        if pwd == ACCESS_TOKEN:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("❌ الكود غير صحيح")
    st.stop()

# 4. محرك الدردشة (بيشتغل بعد الباسورد)
st.success("✅ أهلاً بك يا سيادة الـ CEO مصطفى جمال")
client = OpenAI(api_key=OPENAI_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("أصدر أوامرك للنظام..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # طلب الرد من OpenAI
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "أنت i-AM 1660، النظام السيادي لمصطفى جمال."},
                      *st.session_state.messages]
        )
        reply = response.choices[0].message.content
        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
