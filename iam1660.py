import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="i-AM 1660", page_icon="🛡️")
st.title("🛡️ i-AM 1660 System")

# سحب المفتاح
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("تحدث مع نظامك يا مصطفى..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "أنت i-AM 1660، النظام الذكي لمصطفى جمال."},
                *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            ]
        )
        reply = response.choices[0].message.content
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
