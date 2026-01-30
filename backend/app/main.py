from fastapi import FastAPI

app = FastAPI(title="KK_TRADERS")

@app.get("/")
def home():
    return {"message": "KK_TRADERS backend is running"}
