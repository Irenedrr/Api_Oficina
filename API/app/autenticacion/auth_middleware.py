from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
from app.autenticacion.seguridad_jwt import verificar_token
from app.db.session import engine
from app.models.usuario import Usuario
from sqlmodel import select, Session
from starlette.responses import JSONResponse

RUTAS_PUBLICAS = {
    ("POST", "/usuarios/"),
    ("GET", "/usuarios/"),
    ("POST", "/usuarios/jwt_login"),
    ("POST", "/usuarios/login"),
    ("POST", "/usuarios/registro"),
}

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        metodo = request.method
        ruta = request.url.path
        print(f"Ruta solicitada: {ruta}, Método: {metodo}")
        # Permitir rutas públicas específicas con método
        if (metodo, ruta) in RUTAS_PUBLICAS:
            return await call_next(request)
        print(f"auth header: {request.headers.get('Authorization')}")
        print(request.headers)
        # Obtener token del encabezado Authorization
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Token no proporcionado")

        token = auth_header.split(" ")[1]

        try:
            datos = verificar_token(token)
        except JWTError:
            raise HTTPException(status_code=401, detail="Token inválido o expirado")

        # Cargar el usuario desde la base de datos
        with Session(engine) as db:
            usuario = db.exec(select(Usuario).where(Usuario.id == int(datos["sub"]))).first()
            if not usuario:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")

        # Pasar al siguiente middleware o endpoint
        return await call_next(request)