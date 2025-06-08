from fastapi import APIRouter, Depends
from typing import List
from app.services.evento_service import EventoService
from app.schemas.evento import EventoCreate, EventoUpdate, EventoResponse
from app.services.usuario_service import UsuarioService


router = APIRouter(prefix="/eventos", tags=["Eventos"])

@router.post("/", response_model=EventoResponse)
def create_evento(evento: EventoCreate, service: EventoService = Depends()):
    return service.create(evento)

@router.get("/", response_model=list[EventoResponse])
def read_eventos(service: EventoService = Depends()):
    return service.get_all()

@router.get("/{id}", response_model=EventoResponse)
def read_evento(id: int, service: EventoService = Depends()):
    return service.get_by_id(id)

@router.get("/{id}/eventos", response_model=List[EventoResponse])
def eventos_usuario(id: int, service: UsuarioService = Depends(), evento_service: EventoService = Depends()):
    usuario = service.get_by_id(id)
    return [
        EventoResponse(**evento.model_dump(), participantes=[p.id for p in evento.participantes])
        for evento in usuario.eventos
    ]



@router.patch("/{id}", response_model=EventoResponse)
def update_evento(id: int, evento_data: EventoUpdate, service: EventoService = Depends()):
    return service.update(id, evento_data)

@router.delete("/{id}", response_model=dict)
def delete_evento(id: int, service: EventoService = Depends()):
    return service.delete(id)
