import streamlit as st
from openai import OpenAI
import os

# عنوان النظام
st.set_page_config(page_title="i-AM 1660", page_icon="🛡️")
st.title("🛡️ i-AM 1660 System")
st.markdown("---")

# ربط المفتاح اللي إنت حطيته في Secrets
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل القديمة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# خانة الكتابة
if prompt := st.chat_input("تحدث مع النظام يا مصطفى..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # رد الذكاء الاصطناعي
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "أنت i-AM 1660، النظام الذكي لمصطفى جمال. ردودك قوية وبالعربية."},
                *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            ]
        )
        reply = response.choices[0].message.content
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
