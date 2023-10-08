import datetime
from pydantic import BaseModel

from typing import List
from pydantic import BaseModel,validator

from core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime, Text,ForeignKey
from datetime import datetime

class GameModel(settings.DBBASEMODEL):
    __tablename__ = 'games'

    id: int = Column(Integer,primary_key=True,autoincrement=True, nullable=False)
    name: str = Column(String(50),nullable=False)
    genre: int = Column(Integer,ForeignKey("genres.id"),nullable=False)
    franchise: int = Column(Integer, ForeignKey("franchises.id"), nullable=False)
    release_date: datetime.date = Column(DateTime,nullable=False,default=datetime.utcnow)
    developer: int = Column(Integer,ForeignKey("developers.id"),nullable=False)
    publisher: int = Column(Integer,ForeignKey("publishers.id"),nullable=False)

    @validator('name')
    def name_validate(cls,value):
        value = value.lower()
        if len(value) == 0:
            raise ValueError('Insira pelo menos uma letra')
        return value



    