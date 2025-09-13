from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.qa_service import get_answer

router = APIRouter()

class Question(BaseModel):
    text: str

@router.post("/ask")
def ask_question(q: Question):
    return get_answer(q.text)
