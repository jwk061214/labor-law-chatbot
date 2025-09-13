from fastapi import FastAPI
from backend.routers import chatbot, law, cases, stats, about

app = FastAPI(
    title="Labor Law Assistant",
    description="노동법 관련 문서 조회 및 Q/A 챗봇 서비스",
    version="0.1.0"
)

# 라우터 등록
app.include_router(chatbot.router, prefix="/chat", tags=["Chatbot"])
app.include_router(law.router, prefix="/law", tags=["Law"])
app.include_router(cases.router, prefix="/cases", tags=["Cases"])
app.include_router(stats.router, prefix="/stats", tags=["Statistics"])
app.include_router(about.router, prefix="/about", tags=["About"])

@app.get("/ping")
def ping():
    return {"msg": "pong"}
