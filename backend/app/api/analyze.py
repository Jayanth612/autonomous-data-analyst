from fastapi import APIRouter
from app.models.query import QueryRequest
from app.services.data_analysis import analyze_question

router = APIRouter()

@router.post("/query")
def query(request: QueryRequest):
    return analyze_question(request.question)