import streamlit as st
from openai import OpenAI
import os

# 1. إعداد الهوية السيادية
st.set_page_config(page_title="VeriAnchor Sovereign", page_icon="🛡️")
st.title("🛡️ VeriAnchor: iAM-Sovereign")
st.caption("Patent Pending: EG/P/2025/1660 | Official Secure Portal")

# 2. سحب المفاتيح من الملف اللي إنت لسه عامله (secrets.toml)
# البرنامج هيقرأهم أوتوماتيكياً من st.secrets
try:
    OPENAI_KEY = st.secrets["OPENAI_API_KEY"]
    ACCESS_TOKEN = st.secrets["ACCESS_TOKEN"]
except:
    st.error("❌ المفاتيح غير موجودة في secrets.toml")
    st.stop()

# 3. بوابة الدخول
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    pwd = st.text_input("أدخل كود المرور السيادي للوصول:", type="password")
    if st.button("تفعيل البروتوكول"):
        if pwd == ACCESS_TOKEN:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ كود المرor غير صحيح.")
    st.stop()

# 4. تشغيل محرك الذكاء (بعد تسجيل الدخول)
st.success("✅ مرحباً بك يا سيادة الـ CEO مصطفى جمال. النظام تحت أمرك.")
client = OpenAI(api_key=OPENAI_KEY)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("أصدر أوامرك للنظام..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "أنت i-AM 1660، النظام السيادي الذكي لمصطفى جمال. ردودك قوية وتقنية."},
                      *st.session_state.messages]
        )
        reply = response.choices[0].message.content
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
