import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="VeriAnchor Sovereign", page_icon="🛡️")
st.title("🛡️ VeriAnchor: iAM-Sovereign")

# سحب المفاتيح من ملف secrets اللي إنت عملته
try:
    OPENAI_KEY = st.secrets["OPENAI_API_KEY"]
    ACCESS_TOKEN = st.secrets["ACCESS_TOKEN"]
except:
    st.error("❌ المفاتيح (Secrets) مش واصلة للسيستم")
    st.stop()

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

st.success("✅ أهلاً بك يا سيادة الـ CEO مصطفى جمال. النظام جاهز.")
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
    
    res = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "أنت i-AM 1660، النظام السيادي لمصطفى جمال."}, *st.session_state.messages]
    )
    reply = res.choices[0].message.content
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
