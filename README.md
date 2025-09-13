# ⚖️ Labor Law Assistant

노동법 관련 문서를 조회하고 Q&A 챗봇으로 상담할 수 있는 서비스입니다.  
👉 2025 캡스톤 디자인 프로젝트  

---

## 🛠️ Tech Stack
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python"/>
  <img src="https://img.shields.io/badge/FastAPI-0.95-green?logo=fastapi"/>
  <img src="https://img.shields.io/badge/Streamlit-1.26-FF4B4B?logo=streamlit"/>
  <img src="https://img.shields.io/badge/Firebase-Database-orange?logo=firebase"/>
  <img src="https://img.shields.io/badge/LangChain-LLM-yellow?logo=openai"/>
</p>

- **Backend** : FastAPI  
- **Frontend** : Streamlit  
- **Database** : Firebase  
- **AI/LLM** : LangChain  

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
