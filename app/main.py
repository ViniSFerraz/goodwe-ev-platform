from fastapi import FastAPI

app = FastAPI(
    title = "EV Platform API",
    description = "Challenge GoodWe, grupo 4",
    version = "1.0.0",
)

@app.get("/")
async def health_check():
    return {"status": "Ok"}