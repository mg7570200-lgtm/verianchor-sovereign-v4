import os
import streamlit as st
import google.generativeai as genai

# اسحب المفاتيح من نظام Replit Secrets مباشرة
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

# التأكد من وجود المفتاح قبل التشغيل
if GEMINI_KEY:
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("❌ مفتاح GEMINI_API_KEY غير موجود في Secrets")

# عند التحقق من كلمة السر
if password == ACCESS_TOKEN:
    st.success("✅ تم التفعيل")
