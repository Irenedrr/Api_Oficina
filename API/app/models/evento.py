from sqlmodel import SQLModel, Field, Relationship
from .evento_participante import EventoParticipante 
from typing import Optional, List
from datetime import datetime

class Evento(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    descripcion: Optional[str] = None
    fecha_evento: datetime 
    creador_id: int 

    tipo: Optional[str] = "reunion"  

    participantes: List["Usuario"] = Relationship(back_populates="eventos", link_model=EventoParticipante)