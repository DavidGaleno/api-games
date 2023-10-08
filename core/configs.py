from typing import ClassVar
from pydantic_settings import BaseSettings  
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:ipe%402023@localhost:5432/games_database_api'
    DBBASEMODEL: ClassVar = declarative_base() 

    class Config:
        case_sensitive = True

settings = Settings()