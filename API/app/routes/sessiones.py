# app/routes/sessiones.py
from fastapi import APIRouter
from typing import Optional
from app.schemas.usuario import UsuarioActivo

router = APIRouter(prefix="/sessiones", tags=["Sesión activa temporal"])

usuario_activo: Optional[UsuarioActivo] = None

@router.post("/login")
def establecer_usuario_activo(datos: UsuarioActivo):
    global usuario_activo
    usuario_activo = datos
    return {"mensaje": "Usuario activo registrado", **datos.dict()}

@router.get("/activo")
def obtener_usuario_activo():
    if usuario_activo is None:
        return {"usuario_id": None}
    return usuario_activo
