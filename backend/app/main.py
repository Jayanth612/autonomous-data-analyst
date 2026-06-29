from fastapi import FastAPI
from app.api.upload import router
from app.api.summary import router as summary_router

app = FastAPI()

app.include_router(router)
app.include_router(summary_router)

@app.get("/")
def home():
    return {
        "message": "Autonomous Data Analyst API is running!"
    }