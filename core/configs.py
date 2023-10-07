from typing import List
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'mysql+pymysql://root:ipe@2023@localhost:3306/games_database_api'
    DB_BASE_MODEL: str = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()

