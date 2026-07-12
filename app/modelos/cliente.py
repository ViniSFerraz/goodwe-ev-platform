from pydantic import BaseModel

class Cliente(BaseModel):
    primeiro_nome: str
    sobre_nome: str
    email: str
    telefone: str
    
