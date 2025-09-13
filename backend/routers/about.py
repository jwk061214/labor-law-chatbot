from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_info():
    return {
        "service": "Labor Law Assistant",
        "version": "0.1.0",
        "team": ["Jiwoo Kang", "Team Members..."],
        "tech_stack": ["FastAPI", "Streamlit", "Firebase", "LangChain"]
    }
