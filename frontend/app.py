import streamlit as st
import requests

st.title("⚖️ Labor Law Assistant Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("노동법 관련 질문을 입력하세요..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    res = requests.post("http://127.0.0.1:8000/ask", json={"text": prompt})
    answer = res.json()["answer"]

    st.session_state["messages"].append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)
