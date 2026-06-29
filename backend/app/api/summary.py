from fastapi import APIRouter
from app.services.data_loader import get_dataframe_summary

router = APIRouter()

@router.get("/summary")
def summary():
    return get_dataframe_summary()