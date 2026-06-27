from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Autonomous Data Analyst API"}