from fastapi import APIRouter

router = APIRouter()

# 지금은 샘플 데이터 (나중에 SQL GROUP BY로 대체)
top_questions = [
    {"question": "임금 지급일?", "count": 12},
    {"question": "근로계약 의무?", "count": 8},
    {"question": "휴가 며칠?", "count": 6}
]

@router.get("/top-questions")
def get_stats():
    return {"top_questions": top_questions}
