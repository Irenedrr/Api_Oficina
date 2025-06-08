from sqlmodel import SQLModel
from typing import Optional

class RolCreate(SQLModel):
    nombre: str

class RolResponse(RolCreate):
    id: int

class RolUpdate(SQLModel):
    nombre: Optional[str] = None
