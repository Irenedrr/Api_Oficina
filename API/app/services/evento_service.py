from sqlmodel import Session, select
from fastapi import Depends, HTTPException
from typing import List
from app.models.evento import Evento
from app.schemas.evento import EventoCreate, EventoResponse, EventoUpdate
from app.db.session import get_session
from app.models.usuario import Usuario

class EventoService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, evento_data: EventoCreate) -> EventoResponse:
        participantes_ids = evento_data.participantes or []
        evento_dict = evento_data.model_dump(exclude={"participantes"})
        evento = Evento(**evento_dict)

        if participantes_ids:
            usuarios = self.session.exec(
                select(Usuario).where(Usuario.id.in_(participantes_ids))
            ).all()

            if len(usuarios) != len(participantes_ids):
                raise HTTPException(status_code=400, detail="Uno o más participantes no existen")

            evento.participantes = usuarios

        self.session.add(evento)
        self.session.commit()
        self.session.refresh(evento)
        return EventoResponse(**evento.model_dump(), participantes=[p.id for p in evento.participantes])



    def get_all(self) -> List[EventoResponse]:
        eventos = self.session.exec(select(Evento)).all()
        for evento in eventos:
            self.session.refresh(evento, attribute_names=["participantes"])
        return [
        EventoResponse(**evento.model_dump(), participantes=[p.id for p in evento.participantes])
        for evento in eventos
    ]

def get_by_id(self, id: int) -> EventoResponse:  
        evento = self.session.get(Evento, id)
        if not evento:
            raise HTTPException(status_code=404, detail="Evento no encontrado")
        self.session.refresh(evento, attribute_names=["participantes"])
        return EventoResponse(**evento.model_dump(), participantes=[p.id for p in evento.participantes])

def update(self, id: int, evento_data: EventoUpdate) -> EventoResponse:
        evento = self.session.get(Evento, id)
        if not evento:
            raise HTTPException(status_code=404, detail="Evento no encontrado")

        evento_dict = evento_data.model_dump(exclude_unset=True)
        for key, value in evento_dict.items():
            setattr(evento, key, value)

        self.session.add(evento)
        self.session.commit()
        self.session.refresh(evento)
        self.session.refresh(evento, attribute_names=["participantes"])  

        return EventoResponse(**evento.model_dump(), participantes=evento.participantes)


def delete(self, id: int):
        evento = self.session.get(Evento, id)
        if not evento:
            raise HTTPException(status_code=404, detail="Evento no encontrado")
        self.session.delete(evento)
        self.session.commit()
        return {"message": "Evento eliminado exitosamente"}
