from fastapi import APIRouter

router = APIRouter()

cases = [
    {
        "case_id": "wage-delay-001",
        "title": "임금 체불 사례",
        "description": "근로자가 퇴직 후 3개월간 임금을 받지 못한 사례",
        "legal_basis": "근로기준법 제36조",
        "outcome": "사용자는 퇴직일로부터 14일 이내에 임금을 지급해야 함"
    }
]

@router.get("/{case_id}")
def get_case(case_id: str):
    for case in cases:
        if case["case_id"] == case_id:
            return case
    return {"error": "해당 사례 없음"}
