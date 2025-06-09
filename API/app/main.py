from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 👈 Importa CORS
from app.routes import usuarios, eventos, roles, mensajes, sessiones
from sqlmodel import SQLModel
from app.db.session import engine

app = FastAPI(title="Oficina Virtual API")

# 🟢 Habilitar CORS (¡esto es lo que permite llamadas desde Godot!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O reemplaza con ["http://localhost:8080"] para más seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers correctamente
app.include_router(usuarios.router)
app.include_router(roles.router)
app.include_router(mensajes.router)
app.include_router(eventos.router)
app.include_router(sessiones.router)

def init_db():
    SQLModel.metadata.create_all(engine)

init_db()
