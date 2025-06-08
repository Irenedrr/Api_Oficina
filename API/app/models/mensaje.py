from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class Mensaje(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    contenido: str
    fecha: datetime = Field(default_factory=datetime.utcnow)

    emisor_id: int = Field(foreign_key="usuario.id")
    receptor_id: int = Field(foreign_key="usuario.id")

    emisor: Optional["Usuario"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[Mensaje.emisor_id]"},
        back_populates="mensajes_enviados"
    )
    receptor: Optional["Usuario"] = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[Mensaje.receptor_id]"},
        back_populates="mensajes_recibidos"
    )