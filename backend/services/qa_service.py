def get_answer(user_text: str) -> dict:
    answers = {
        "임금": {"answer": "임금은 매월 1회 이상, 일정한 날짜에 지급해야 합니다.", "source": "근로기준법 제43조"},
        "근로계약": {"answer": "근로계약은 반드시 서면으로 작성해야 합니다.", "source": "근로기준법 제17조"},
        "휴가": {"answer": "근로자는 1년에 15일 이상의 유급휴가를 가질 권리가 있습니다.", "source": "근로기준법 제60조"}
    }
    for key, ans in answers.items():
        if key in user_text:
            return ans
    return {"answer": "관련 문서를 찾을 수 없습니다.", "source": None}
