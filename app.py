import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="VeriAnchor Sovereign", page_icon="🛡️")

# سحب المفاتيح
api_key = os.environ.get("OPENAI_API_KEY")
access_token = os.environ.get("ACCESS_TOKEN")

st.title("🛡️ i-AM 1660")

# التأكد من وجود المفتاح في النظام
if not api_key:
    st.error("المفتاح ناقص! تأكد من إضافة OPENAI_API_KEY في السيكرتس")
    st.stop()

client = OpenAI(api_key=api_key)

# ... باقي كود الشات اللي بعتهولك فوق
