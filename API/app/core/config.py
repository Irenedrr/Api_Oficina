from pydantic_settings import BaseSettings

class Config(BaseSettings):
    database_type: str
    debug: bool = False
    database_url: str = ""
    api_base_url: str = ""
    frontend_url: str = ""

    class Config:
        env_file = ".env"

config = Config()
