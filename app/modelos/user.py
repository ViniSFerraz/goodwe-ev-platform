from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    telefone: str
    birth_date: str
    address_l1: str
    address_l2: str
    