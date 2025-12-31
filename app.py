import streamlit as st
from openai import OpenAI
import os

# الهوية
st.set_page_config(page_title="VeriAnchor Sovereign", page_icon="🛡️")
st.title("🛡️ VeriAnchor: iAM-Sovereign")

# سحب المفاتيح (بما إنك عملت ملف secrets.toml بنجاح)
try:
    OPENAI_KEY = st.secrets["OPENAI_API_KEY"]
    ACCESS_TOKEN = st.secrets["ACCESS_TOKEN"]
except:
    st.error("❌ المفاتيح غير مفعلة في secrets.toml")
    st.stop()

# بوابة الدخول
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    pwd = st.text_input("كود المرور السيادي:", type="password")
    if st.button("تفعيل البروتوكول"):
        if pwd == ACCESS_TOKEN:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("❌ الكود خطأ")
    st.stop()

# الشات
st.success("✅ مرحباً يا سيادة الـ CEO")
client = OpenAI(api_key=OPENAI_KEY)
if "msgs" not in st.session_state:
    st.session_state.msgs = []

for m in st.session_state.msgs:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("أصدر أوامرك..."):
    st.session_state.msgs.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "أنت i-AM 1660"}, *st.session_state.msgs]
    )
    reply = response.choices[0].message.content
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.msgs.append({"role": "assistant", "content": reply})
