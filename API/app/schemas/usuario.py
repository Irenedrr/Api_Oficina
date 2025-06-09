from sqlmodel import SQLModel
from typing import Optional,List
from app.schemas.evento import EventoResponse
from pydantic import BaseModel

    
class UsuarioCreate(SQLModel):
    nombre: str
    email: str
    contrasena: str
    rol_id: int
    imagen_url: Optional[str] = None
    personaje: str
    oficina: str
    estado: Optional[str] = "conectado"
    


class UsuarioResponse(UsuarioCreate):
    id: int
    

class UsuarioUpdate(SQLModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    contrasena: Optional[str] = None
    rol_id: Optional[int] = None
    imagen_url: Optional[str] = None
    personaje: Optional[str] = None
    oficina: Optional[str] = None
    estado: Optional[str] = None

class UsuarioActivo(BaseModel):
    usuario_id: int
    nombre: str
    personaje: str
    oficina: str
