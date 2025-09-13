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

## 📊 주요 기능 (Features)

- 🤖 **Chatbot** : 노동법 Q&A 대화형 상담  
- 📑 **Law Search** : 주제별 법령 검색 (임금, 근로계약, 휴가 등)  
- 📂 **Case Examples** : 실제 판례/사례 데이터 조회  
- 📊 **Statistics** : 가장 많이 질문된 키워드 통계 시각화  
- ℹ️ **About** : 프로젝트 및 팀 소개  

---

## 👥 Team

| 이름 | 역할 | 담당 |
|------|------|------|
| **강지우** | Backend | FastAPI, DB 연동 |
| Team Member A | Frontend | Streamlit UI/UX |
| Team Member B | AI | LangChain & LLM |

---

## 📌 향후 발전 방향
- 다국어 지원 (영어/중국어/베트남어 등)  
- 실제 판례 데이터셋 확장  
- 사용자별 맞춤형 상담 기능  
