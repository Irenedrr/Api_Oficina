from fastapi import APIRouter, Depends
from app.models.usuario import Usuario 
from fastapi import HTTPException  
from fastapi.security import OAuth2PasswordRequestForm
from app.autenticacion.seguridad_jwt import crear_token
from sqlmodel import Session, select
from app.db.session import get_session
from app.services.usuario_service import UsuarioService
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioResponse)
def create_usuario(usuario: UsuarioCreate, service: UsuarioService = Depends()):
    return service.create(usuario)

@router.get("/", response_model=list[UsuarioResponse])
def read_usuarios(service: UsuarioService = Depends()):
    return service.get_all()

@router.get("/{id}", response_model=UsuarioResponse)
def read_usuario(id: int, service: UsuarioService = Depends()):
    return service.get_by_id(id)

@router.post("/actualizar/{id}", response_model=UsuarioResponse)
def update_usuario_post(id: int, usuario_data: UsuarioUpdate, service: UsuarioService = Depends()):
    return service.update(id, usuario_data)


@router.delete("/{id}", response_model=dict)
def delete_usuario(id: int, service: UsuarioService = Depends()):
    return service.delete(id)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    usuario = session.exec(select(Usuario).where(Usuario.email == form_data.username)).first()
    if not usuario or usuario.contrasena != form_data.password:
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos")
    
    token = crear_token({"sub": str(usuario.id)})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/registro", response_model=UsuarioResponse)
def registrar(usuario_data: UsuarioCreate, session: Session = Depends(get_session)):
    usuario_existente = session.exec(select(Usuario).where(Usuario.email == usuario_data.email)).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    nuevo_usuario = Usuario(**usuario_data.model_dump())
    session.add(nuevo_usuario)
    session.commit()
    session.refresh(nuevo_usuario)

    token = crear_token({"sub": str(nuevo_usuario.id)})
    return nuevo_usuario

@router.get("/config_juego/{usuario_id}")
def obtener_config_juego(usuario_id: int, session: Session = Depends(get_session)):
    usuario = session.exec(select(Usuario).where(Usuario.id == usuario_id)).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return {
        "nombre": usuario.nombre.strip(),
        "avatar": usuario.personaje,
        "oficina": usuario.oficina
    }