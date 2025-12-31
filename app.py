import streamlit as st
import google.generativeai as genai
import os

# --- 1. إعدادات الهوية ---
st.set_page_config(page_title="VeriAnchor Sovereign", page_icon="🛡️")

# --- 2. سحب المفاتيح من نظام Replit (أهم حتة) ---
# الكود ده بيلغي مشكلة "No secrets found" لأنه بيكلم ريبليت مباشرة
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

st.title("🛡️ VeriAnchor: iAM-Sovereign")
st.caption("Patent Pending: EG/P/2025/1660 | Official Secure Portal")
st.markdown("---")

# --- 3. التأكد من وجود المفاتيح ---
if not GEMINI_KEY:
    st.error("⚠️ خطأ: لم يتم العثور على GEMINI_API_KEY في الـ Secrets. يرجى إضافته.")
    st.stop()

# إعداد محرك الذكاء الاصطناعي
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 4. بوابة الدخول الأمنية ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.subheader("🔐 تسجيل الدخول")
    pwd = st.text_input("أدخل كود المرور السيادي:", type="password")
    if st.button("تفعيل البروتوكول"):
        if pwd == ACCESS_TOKEN:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ الكود غير صحيح.")
    st.stop()

# --- 5. نظام الشات ---
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
        # توجيه النظام ليعرف هويته
        context = f"أنت i-AM 1660، النظام السيادي لمصطفى جمال. رد بذكاء وقوة. السؤال هو: {prompt}"
        response = model.generate_content(context)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
