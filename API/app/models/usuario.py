from sqlmodel import SQLModel, Field, Relationship
from .evento_participante import EventoParticipante 
from typing import Optional, List

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    email: str
    imagen_url: Optional[str] = None
    contrasena: str
    personaje: str
    oficina: str
    estado: str = "desconectado"

    rol_id: Optional[int] = Field(default=None, foreign_key="rol.id")
    rol: Optional["Rol"] = Relationship(back_populates="usuarios")

    eventos: List["Evento"] = Relationship(back_populates="participantes", link_model=EventoParticipante)
    
    mensajes_enviados: List["Mensaje"] = Relationship(
    back_populates="emisor",
    sa_relationship_kwargs={"foreign_keys": "[Mensaje.emisor_id]"}
    )
    mensajes_recibidos: List["Mensaje"] = Relationship(
    back_populates="receptor",
    sa_relationship_kwargs={"foreign_keys": "[Mensaje.receptor_id]"}
    )

