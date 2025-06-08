from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, status
from typing import Optional

CLAVE_SECRETA = "clave_secreta_super_segura"
ALGORITMO = "HS256"
TIEMPO_EXPIRACION = 60  # minutos

def crear_token(datos: dict) -> str:
    datos_a_codificar = datos.copy()
    expiracion = datetime.utcnow() + timedelta(minutes=TIEMPO_EXPIRACION)
    datos_a_codificar.update({"exp": expiracion})
    return jwt.encode(datos_a_codificar, CLAVE_SECRETA, algorithm=ALGORITMO)

def verificar_token(token: str) -> Optional[dict]:
    try:
        datos = jwt.decode(token, CLAVE_SECRETA, algorithms=[ALGORITMO])
        return datos
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
