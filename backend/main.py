from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Labor Law Chatbot")

class Question(BaseModel):
    text: str

@app.post("/ask")
def ask_question(q: Question):
    answers = {
        "임금": "임금은 매월 1회 이상, 일정한 날짜에 지급해야 합니다.",
        "근로계약": "근로계약은 반드시 서면으로 작성해야 합니다.",
        "휴가": "근로자는 1년에 15일 이상의 유급휴가를 가질 권리가 있습니다."
    }
    for key, ans in answers.items():
        if key in q.text:
            return {"answer": ans}
    return {"answer": "관련 법률 문서를 찾을 수 없습니다."}
