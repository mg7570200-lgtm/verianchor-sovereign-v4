import streamlit as st
import os
from openai import OpenAI

# إعدادات الواجهة
st.set_page_config(page_title="VeriAnchor Sovereign", page_icon="🛡️")
st.title("🛡️ VeriAnchor: iAM-Sovereign")

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

st.success("✅ النظام مفعّل. أهلاً بك يا سيادة الـ CEO.")
# كود الشات بيكمل هنا...
