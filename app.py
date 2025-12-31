import streamlit as st
from openai import OpenAI
import os

# هدايا البداية
st.set_page_config(page_title="VeriAnchor Sovereign", page_icon="🛡️")
st.title("🛡️ i-AM 1660")

# جلب المفاتيح من السيكرتس
API_KEY = os.environ.get("OPENAI_API_KEY")
PASS = os.environ.get("ACCESS_TOKEN")

if not API_KEY:
    st.error("⚠️ المفتاح ناقص في السيكرتس!")
    st.stop()

# تسجيل الدخول
if "logged" not in st.session_state:
    st.session_state.logged = False

if not st.session_state.logged:
    entry = st.text_input("كود المرور:", type="password")
    if st.button("دخول"):
        if entry == PASS:
            st.session_state.logged = True
            st.rerun()
        else:
            st.error("الكود غلط")
    st.stop()

# تشغيل الشات
client = OpenAI(api_key=API_KEY)
if "msgs" not in st.session_state:
    st.session_state.msgs = []

for m in st.session_state.msgs:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("تحدث مع النظام..."):
    st.session_state.msgs.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    with st.chat_message("assistant"):
        res = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "أنت i-AM 1660 نظام مصطفى جمال."}, *st.session_state.msgs]
        )
        ans = res.choices[0].message.content
        st.markdown(ans)
        st.session_state.msgs.append({"role": "assistant", "content": ans})
