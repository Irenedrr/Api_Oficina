from sqlmodel import Session, select
from fastapi import Depends, HTTPException
from app.models.mensaje import Mensaje
from app.schemas.mensaje import MensajeCreate, MensajeResponse, MensajeUpdate
from app.db.session import get_session
from sqlalchemy import or_, and_

class MensajeService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, mensaje_data: MensajeCreate) -> MensajeResponse:
        mensaje = Mensaje(**mensaje_data.model_dump())
        self.session.add(mensaje)
        self.session.commit()
        self.session.refresh(mensaje)
        return MensajeResponse(**mensaje.model_dump())

    def get_all(self):
        return self.session.exec(select(Mensaje)).all()

    def get_by_id(self, id: int):
        mensaje = self.session.get(Mensaje, id)
        if not mensaje:
            raise HTTPException(status_code=404, detail="Mensaje no encontrado")
        return mensaje

    def update(self, id: int, mensaje_data: MensajeUpdate) -> Mensaje:
        mensaje = self.session.get(Mensaje, id)
        if not mensaje:
            raise HTTPException(status_code=404, detail="Mensaje no encontrado")

        mensaje_dict = mensaje_data.model_dump(exclude_unset=True)
        for key, value in mensaje_dict.items():
            setattr(mensaje, key, value)

        self.session.add(mensaje)
        self.session.commit()
        self.session.refresh(mensaje)
        return mensaje
    
    def get_conversacion(self, usuario_a_id: int, usuario_b_id: int):
        stmt = select(Mensaje).where(
        or_(
            and_(Mensaje.emisor_id == usuario_a_id, Mensaje.receptor_id == usuario_b_id),
            and_(Mensaje.emisor_id == usuario_b_id, Mensaje.receptor_id == usuario_a_id)
        )
    ).order_by(Mensaje.fecha)

        return self.session.exec(stmt).all()

    def delete(self, id: int):
        mensaje = self.session.get(Mensaje, id)
        if not mensaje:
            raise HTTPException(status_code=404, detail="Mensaje no encontrado")
        self.session.delete(mensaje)
        self.session.commit()
        return {"message": "Mensaje eliminado exitosamente"}
