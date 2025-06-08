from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Rol(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str

    usuarios: List["Usuario"] = Relationship(back_populates="rol")