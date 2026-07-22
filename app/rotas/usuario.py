from fastapi import APIRouter

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)


@router.get("/")
async def listar_usuarios():
    return {
        "mensagem": "Lista de usuários"
    }