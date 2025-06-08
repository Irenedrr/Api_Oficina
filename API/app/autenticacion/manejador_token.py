from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.autenticacion.seguridad_jwt import verificar_token

oauth2 = OAuth2PasswordBearer(tokenUrl="usuarios/login")

def obtener_usuario_actual(token: str = Depends(oauth2)):
    datos = verificar_token(token)
    if datos is None:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return datos
