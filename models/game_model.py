
from pydantic import validator

from core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime, Text,ForeignKey
import datetime
from sqlalchemy.orm import relationship
from models.other_models import GenreModel,FranchiseModel,DevelopersModel,PublishersModel

class GameModel(settings.DBBASEMODEL):
    __tablename__ = 'games'

    id: int = Column(Integer,primary_key=True,autoincrement=True)
    name: str = Column(String(50),nullable=False)
    genre_id: int = Column(Integer,ForeignKey('genres.id'),nullable=False)
    franchise_id: int = Column(Integer,ForeignKey('franchises.id'),nullable=False)
    release_date: datetime.date = Column(DateTime,nullable=False,default=datetime.datetime.utcnow)
    developer_id: int = Column(Integer,ForeignKey('developers.id'),nullable=False)
    publisher_id: int = Column(Integer,ForeignKey('publishers.id'),nullable=False)
    genre =  relationship('GenreModel',backref='games')
    franchise = relationship('FranchiseModel',backref='games')
    developers = relationship('DevelopersModel',backref='games')
    publisher = relationship('PublishersModel',backref='games')

    @validator('name')
    def name_validate(cls,value):
        value = value.lower()
        if len(value) == 0:
            raise ValueError('Insira pelo menos uma letra')
        return value



    