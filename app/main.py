from fastapi import FastAPI

app = FastAPI(
    title = "EV Platform API",
    description = "API do projeto GoodWe EV Platform - Challenge FIAP | Grupo 4",
    version = "1.0.0",
)


@app.get("/", tags=["Sistema"])
async def health_check():
    return {
        "status": "OK",
        "api": "EV Platform API",
        "version": "1.0.0"
    }

app.include_router(usuario_router)