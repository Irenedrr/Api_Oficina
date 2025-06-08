from fastapi import APIRouter, Depends
from typing import List, Dict
from fastapi import Query
from app.services.mensaje_service import MensajeService
from app.services.usuario_service import UsuarioService
from app.schemas.mensaje import MensajeCreate, MensajeUpdate, MensajeResponse

router = APIRouter(prefix="/mensajes", tags=["Mensajes"])

@router.post("/", response_model=MensajeResponse)
def create_mensaje(mensaje: MensajeCreate, service: MensajeService = Depends()):
    return service.create(mensaje)

@router.get("/", response_model=list[MensajeResponse])
def read_mensajes(service: MensajeService = Depends()):
    return service.get_all()

@router.get("/{id}", response_model=MensajeResponse)
def read_mensaje(id: int, service: MensajeService = Depends()):
    return service.get_by_id(id)

@router.patch("/{id}", response_model=MensajeResponse)
def update_mensaje(id: int, mensaje_data: MensajeUpdate, service: MensajeService = Depends()):
    return service.update(id, mensaje_data)

@router.get("/chat/", response_model=List[MensajeResponse])
def obtener_conversacion(
    usuario_a: int = Query(..., description="ID de un usuario"),
    usuario_b: int = Query(..., description="ID del otro usuario"),
    service: MensajeService = Depends()
):
    return service.get_conversacion(usuario_a, usuario_b)

@router.get("/{id}/mensajes", response_model=Dict[str, List[MensajeResponse]])
def mensajes_usuario(id: int, service: UsuarioService = Depends()):
    usuario = service.get_by_id(id)
    return {
        "enviados": usuario.mensajes_enviados,
        "recibidos": usuario.mensajes_recibidos
    }

@router.delete("/{id}", response_model=dict)
def delete_mensaje(id: int, service: MensajeService = Depends()):
    return service.delete(id)
