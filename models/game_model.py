from pydantic import BaseModel

from typing import List
from pydantic import BaseModel,validator

from core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime, Text,ForeignKey
import datetime

class GameModel(settings.DBBASEMODEL):
    __tablename__ = 'games'

    id: int = Column(Integer,primary_key=True,autoincrement=True)
    name: str = Column(String(50),nullable=False)
    genre: str = Column(String(50),nullable=False)
    franchise: str = Column(String(50),nullable=False)
    release_date: datetime.date = Column(DateTime,nullable=False,default=datetime.datetime.utcnow)
    developer: str = Column(String(50),nullable=False)
    publisher: str = Column(String(50),nullable=False)

    @validator('name')
    def name_validate(cls,value):
        value = value.lower()
        if len(value) == 0:
            raise ValueError('Insira pelo menos uma letra')
        return value



    