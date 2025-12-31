import streamlit as st
from openai import OpenAI
import os

# إعدادات الواجهة
st.set_page_config(page_title="i-AM 1660", page_icon="🛡️")
st.title("🛡️ i-AM 1660 System")
st.markdown("---")

# ربط المفتاح من السيكرتس
api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# إدخال الرسائل
if prompt := st.chat_input("تحدث مع نظام i-AM 1660..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "أنت i-AM 1660، النظام السيادي لمصطفى جمال. ردودك قوية، ذكية، وباللهجة المصرية أو العربية الفصحى حسب الطلب."},
                    *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                ]
            )
            reply = response.choices[0].message.content
            st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        st.error(f"فيه مشكلة في المفتاح أو الرصيد: {e}")
