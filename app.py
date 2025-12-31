import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="i-AM 1660", page_icon="🛡️")

# جلب البيانات من السيكرتس
API_KEY = os.environ.get("OPENAI_API_KEY")
PASS_CODE = os.environ.get("ACCESS_TOKEN")

st.title("🛡️ i-AM 1660 System")
st.caption("Official Secure Portal | Patent: 1660")

if not API_KEY:
    st.error("المفتاح ناقص في الـ Secrets!")
    st.stop()

if "logged" not in st.session_state:
    st.session_state.logged = False

if not st.session_state.logged:
    entry = st.text_input("كود المرور السيادي:", type="password")
    if st.button("دخول للنظام"):
        if entry == PASS_CODE:
            st.session_state.logged = True
            st.rerun()
        else:
            st.error("الكود خطأ")
    st.stop()

# الشات
client = OpenAI(api_key=API_KEY)
if "msgs" not in st.session_state:
    st.session_state.msgs = []

for m in st.session_state.msgs:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if p := st.chat_input("أصدر أوامرك..."):
    st.session_state.msgs.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.markdown(p)
    
    with st.chat_message("assistant"):
        res = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "أنت i-AM 1660، نظام سيادي لمصطفى جمال."}, *st.session_state.msgs]
        )
        ans = res.choices[0].message.content
        st.markdown(ans)
        st.session_state.msgs.append({"role": "assistant", "content": ans})
