import streamlit as st
import requests

# 페이지 기본 설정
st.set_page_config(page_title="Labor Law Assistant", page_icon="⚖️", layout="wide")

# 세션 상태 초기화 (대화 저장)
if "chat_messages" not in st.session_state:
    st.session_state["chat_messages"] = []

# 사이드바 메뉴
menu = st.sidebar.radio(
    "📌 기능 선택",
    ["Chatbot", "Law Search", "Case Examples", "Statistics", "About"]
)

BASE_URL = "http://127.0.0.1:8000"  # FastAPI 서버 주소

# -------------------------------
# 1. Chatbot
# -------------------------------
# --- Chatbot Section ---
if menu == "Chatbot":
    st.markdown("<h2 style='text-align: center;'>🤖 Labor Law Chatbot</h2>", unsafe_allow_html=True)
    st.caption("노동법 관련 질문을 입력하면 규정을 알려드립니다.")

    # 말풍선 스타일 CSS
    st.markdown("""
        <style>
        .chat-bubble-user {
            background-color: #d1e7ff;
            padding: 10px;
            border-radius: 15px;
            margin: 5px;
            text-align: right;
        }
        .chat-bubble-bot {
            background-color: #f1f0f0;
            padding: 10px;
            border-radius: 15px;
            margin: 5px;
            text-align: left;
        }
        </style>
    """, unsafe_allow_html=True)

    # 대화 출력
    for msg in st.session_state["chat_messages"]:
        if msg["role"] == "user":
            st.markdown(f"<div class='chat-bubble-user'>🙋‍♂️ {msg['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-bubble-bot'>⚖️ {msg['content']}</div>", unsafe_allow_html=True)

    # 입력창
    if prompt := st.chat_input("질문을 입력하세요..."):
        st.session_state["chat_messages"].append({"role": "user", "content": prompt})
        st.markdown(f"<div class='chat-bubble-user'>🙋‍♂️ {prompt}</div>", unsafe_allow_html=True)

        try:
            res = requests.post(f"{BASE_URL}/chat/ask", json={"text": prompt})
            data = res.json()
            answer = data.get("answer", "⚠️ 서버 응답 없음")
        except Exception:
            answer = "⚠️ 서버와 연결할 수 없습니다."

        st.session_state["chat_messages"].append({"role": "assistant", "content": answer})
        st.markdown(f"<div class='chat-bubble-bot'>⚖️ {answer}</div>", unsafe_allow_html=True)


# -------------------------------
# 2. Law Search
# -------------------------------
elif menu == "Law Search":
    st.markdown("## 📑 법률 조회")
    st.write("주제를 선택하면 관련 규정을 확인할 수 있습니다.")

    col1, col2, col3 = st.columns(3)

    if col1.button("임금"):
        res = requests.get(f"{BASE_URL}/law/wage").json()
        st.success(f"**{res['title']}**\n\n{res['content']}\n\n📖 {res['reference']}")

    if col2.button("근로계약"):
        res = requests.get(f"{BASE_URL}/law/contract").json()
        st.success(f"**{res['title']}**\n\n{res['content']}\n\n📖 {res['reference']}")

    if col3.button("휴가"):
        res = requests.get(f"{BASE_URL}/law/vacation").json()
        st.success(f"**{res['title']}**\n\n{res['content']}\n\n📖 {res['reference']}")

# -------------------------------
# 3. Case Examples
# -------------------------------
elif menu == "Case Examples":
    st.markdown("## 📂 사례 조회")
    st.write("사례 ID를 입력하세요 (예: wage-delay-001)")

    case_id = st.text_input("사례 ID 입력", placeholder="예: wage-delay-001")
    if st.button("사례 조회"):
        res = requests.get(f"{BASE_URL}/cases/{case_id}").json()

        if "error" in res:
            st.error("❌ 해당 사례가 없습니다. 다른 ID를 입력해보세요.")
        else:
            st.success(f"**{res['title']}**")
            st.write(res["description"])
            st.markdown(f"📖 관련 법조항: *{res['legal_basis']}*")
            st.info(f"📌 판결/결과: {res['outcome']}")

# -------------------------------
# 4. Statistics
# -------------------------------
elif menu == "Statistics":
    st.markdown("## 📊 질문 통계")

    try:
        res = requests.get(f"{BASE_URL}/stats/top-questions")
        data = res.json()

        # 데이터프레임 변환
        import pandas as pd
        import altair as alt
        df = pd.DataFrame(data["top_questions"])

        # 표 보기
        st.dataframe(df)

        # 그래프
        chart = alt.Chart(df).mark_bar(color="steelblue").encode(
            x=alt.X("question", sort=None, title="질문"),
            y=alt.Y("count", title="횟수")
        ).properties(width=600, height=400)

        st.altair_chart(chart, use_container_width=True)

    except Exception:
        st.error("⚠️ 통계 데이터를 불러올 수 없습니다.")


# -------------------------------
# 5. About
# -------------------------------
elif menu == "About":
    st.markdown("## ℹ️ About")

    try:
        res = requests.get(f"{BASE_URL}/about/")
        data = res.json()

        st.subheader("서비스 정보")
        st.write(f"**서비스명:** {data['service']}")
        st.write(f"**버전:** {data['version']}")

        st.subheader("팀원")
        for member in data["team"]:
            st.write(f"- {member}")

        st.subheader("기술 스택")
        st.markdown(", ".join(data["tech_stack"]))

    except Exception:
        st.error("⚠️ 서버와 연결할 수 없습니다.")

import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000"

if st.button("🔌 API 연결 확인"):
    try:
        res = requests.get(f"{BASE_URL}/ping")
        st.success(f"연결 성공 ✅ : {res.json()}")
    except Exception as e:
        st.error(f"연결 실패 ❌ : {e}")
