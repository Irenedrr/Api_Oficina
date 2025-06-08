from sqlmodel import create_engine, Session
from app.core.config import config

if config.database_type == "postgres":
    database_url = (
        f"postgresql://{config.postgres_user}:{config.postgres_password}"
        f"@{config.postgres_host}:{config.postgres_port}/{config.postgres_db}"
    )
else:
    database_url = "sqlite:///./database.db"

engine = create_engine(database_url, echo=config.debug)

def get_session():
    with Session(engine) as session:
        yield session
