from fastapi import FastAPI
from app.routes import usuarios, eventos, roles,mensajes
from sqlmodel import SQLModel
from app.db.session import engine

# Importar las rutas de la oficina virtual
from app.routes import usuarios, roles, mensajes, eventos

app = FastAPI(title="Oficina Virtual API")

# Incluir las rutas
app.include_router(usuarios.router)
app.include_router(roles.router)
app.include_router(mensajes.router)
app.include_router(eventos.router)

# Crear tablas en la base de datos
def init_db():
    SQLModel.metadata.create_all(engine)

init_db()
