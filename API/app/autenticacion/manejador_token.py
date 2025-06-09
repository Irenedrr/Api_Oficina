import select
from sqlmodel import Session, select
from app.models.usuario import Usuario 
from fastapi import Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from app.autenticacion.seguridad_jwt import verificar_token
from app.db.session import get_session

oauth2 = OAuth2PasswordBearer(tokenUrl="/usuarios/jwt_login")
RUTAS_PUBLICAS = {
    ("POST", "/usuarios/"),
    ("GET", "/usuarios/"),
    ("POST", "/usuarios/jwt_login"),
    ("POST", "/usuarios/login"),
    ("POST", "/usuarios/registro"),
}

def obtener_usuario_actual(request: Request, token: str = Depends(oauth2), session: Session = Depends(get_session)):
    metodo = request.method
    ruta = request.url.path
    print(f"Ruta solicitada: {ruta}, Método: {metodo}")
    if request.url.path in RUTAS_PUBLICAS:
        # Saltar autenticación para rutas públicas
        return None
    print(f"auth header: {request.headers.get('Authorization')}")
    print(request.headers)
    print(f"oauth2 token: {token}")
    print(f"oauth2 variable: {oauth2}")
    datos = verificar_token(token)
    if datos is None:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    usuario = session.exec(select(Usuario).where(Usuario.id == int(datos["sub"]))).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario
