from sqlmodel import SQLModel
from typing import Optional
from datetime import datetime

class MensajeCreate(SQLModel):
    contenido: str
    emisor_id: int
    receptor_id: int
    fecha: Optional[datetime] = None

class MensajeResponse(MensajeCreate):
    id: int

class MensajeUpdate(SQLModel):
    contenido: Optional[str] = None
    receptor_id: Optional[int] = None
    fecha: Optional[datetime] = None
