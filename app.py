import streamlit as st
import google.generativeai as genai
import os

# --- 1. إعدادات الهوية ---
st.set_page_config(page_title="VeriAnchor Sovereign", page_icon="🛡️")

st.title("🛡️ VeriAnchor: iAM-Sovereign")
st.caption("Patent Pending: EG/P/2025/1660 | Official Secure Portal")

# --- 2. سحب المفاتيح بالطريقة المضمونة للشيل (OS) ---
# هنا غيرنا st.secrets لـ os.environ عشان المربع الوردي يختفي للأبد
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

# --- 3. التحقق التشغيلي ---
if not GEMINI_KEY:
    st.error("❌ النظام لم يجد مفتاح GEMINI_API_KEY. تأكد من وضعه في الـ Shell.")
    st.stop()

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 4. بوابة الدخول ---
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

# --- 5. الشات ---
st.success("✅ أهلاً بك يا سيادة الـ CEO مصطفى جمال")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("أصدر أوامرك..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = model.generate_content(f"أنت i-AM 1660، النظام الذكي لمصطفى جمال: {prompt}")
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.chat_history.append({"role": "assistant", "content": response.text})
