import streamlit as st
import google.generativeai as genai
import os

# --- 1. إعدادات الهوية والواجهة ---
st.set_page_config(page_title="VeriAnchor Sovereign", page_icon="🛡️", layout="centered")

# تنسيق CSS لجعل الواجهة احترافية
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #000; color: white; }
    .stTextInput>div>div>input { border-radius: 5px; }
    </style>
    """, unsafe_allow_value=True)

st.title("🛡️ VeriAnchor: iAM-Sovereign")
st.caption("Patent Pending: EG/P/2025/1660 | Official Secure Portal")
st.write(f"مرحباً بك يا سيادة الـ CEO مصطفى جمال")
st.markdown("---")

# --- 2. جلب المفاتيح من ريبليت (Secrets) ---
# تأكد إنك ضايف GEMINI_API_KEY و ACCESS_TOKEN في علامة القفل
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

# --- 3. التحقق من النظام ---
if not GEMINI_KEY:
    st.error("❌ خطأ تقني: مفتاح API غير مفعّل. يرجى إضافته في Secrets باسم GEMINI_API_KEY")
    st.stop()

# إعداد نموذج الذكاء الاصطناعي
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 4. بوابة العبور الأمنية ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.subheader("🔐 تسجيل الدخول للنظام السيادي")
    user_password = st.text_input("أدخل كود المرور (ACCESS_TOKEN):", type="password")
    if st.button("تفعيل البروتوكول"):
        if user_password == ACCESS_TOKEN:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("⚠️ كود المرور غير صحيح. الوصول مرفوض.")
    st.stop()

# --- 5. نظام الدردشة (بعد تسجيل الدخول) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# منطقة الإدخال
if prompt := st.chat_input("أصدر أوامرك للنظام يا مصطفى..."):
    # إضافة رسالة المستخدم
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # توليد رد الذكاء الاصطناعي
    with st.chat_message("assistant"):
        with st.spinner("جاري المعالجة السيادية..."):
            try:
                # إرسال السياق للنظام
                full_prompt = f"أنت i-AM 1660، النظام السيادي لمصطفى جمال. ردودك ذكية، تقنية، وباللغة العربية. المستخدم هو مخترك النظام نفسه: {prompt}"
                response = model.generate_content(full_prompt)
                reply = response.text
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error(f"حدث خطأ في الاتصال: {e}")

# زر لمسح المحادثة
if st.sidebar.button("مسح سجل العمليات"):
    st.session_state.messages = []
    st.rerun()
