# ⚖️ Labor Law Assistant

노동법 관련 문서를 조회하고 Q&A 챗봇으로 상담할 수 있는 서비스입니다.  
👉 2025 캡스톤 디자인 프로젝트  

---

## 🛠 Tech Stack
- 🚀 FastAPI (백엔드 API)
- 🎨 Streamlit (프론트엔드 UI)
- 🔥 Firebase (DB)
- 🧠 LangChain (LLM 연동)
- 🐙 GitHub (협업 & 버전관리)

---

## 📸 Screenshots
| Chatbot | Law Search | Statistics |
|---------|------------|------------|
| ![chatbot](./images/chatbot.png) | ![law](./images/law.png) | ![stats](./images/stats.png) |

---

## 🚀 실행 방법
```bash
# 백엔드 실행
cd backend
uvicorn main:app --reload

# 프론트 실행
cd frontend
streamlit run app.py
