from sqlmodel import SQLModel, Field

class EventoParticipante(SQLModel, table=True):  
    evento_id: int = Field(foreign_key="evento.id", primary_key=True)
    usuario_id: int = Field(foreign_key="usuario.id", primary_key=True)