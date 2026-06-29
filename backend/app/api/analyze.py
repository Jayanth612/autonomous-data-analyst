from fastapi import APIRouter
from app.services.data_analysis import analyze_sales

router = APIRouter()


@router.get("/analyze")
def analyze():
    return analyze_sales()