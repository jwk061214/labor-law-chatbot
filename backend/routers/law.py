from fastapi import APIRouter

router = APIRouter()

laws = {
    "wage": {"title": "임금", "content": "임금은 매월 1회 이상...", "reference": "근로기준법 제43조"},
    "contract": {"title": "근로계약", "content": "근로계약은 반드시 서면으로...", "reference": "근로기준법 제17조"},
    "vacation": {"title": "휴가", "content": "근로자는 1년에 15일...", "reference": "근로기준법 제60조"},
}

@router.get("/{topic}")
def get_law(topic: str):
    return laws.get(topic, {"title": topic, "content": "해당 주제 없음", "reference": None})
