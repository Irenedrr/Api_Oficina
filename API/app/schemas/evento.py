from sqlmodel import SQLModel
from typing import Optional,List
from datetime import datetime




class EventoCreate(SQLModel):
    titulo: str
    descripcion: Optional[str] = None
    creador_id: int
    fecha_evento: datetime 
    

    tipo: Optional[str] = "reunion"  

    participantes: Optional[List[int]] = []

class EventoResponse(EventoCreate):
    id: int
    participantes: List[int]

class EventoUpdate(SQLModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    fecha_evento: datetime 
