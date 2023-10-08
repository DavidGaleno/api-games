from core.configs import settings
from sqlalchemy import Column, Integer, String, DateTime, Text

class GenreModel(settings.DBBASEMODEL):
    __tablename__ = 'genres'
    id: int = Column(Integer,nullable=False,primary_key=True)
    name: str = Column(String(50),nullable=False)

class FranchiseModel(settings.DBBASEMODEL):
    __tablename__ = 'franchises'
    id: int = Column(Integer,nullable=False,primary_key=True)
    name: str = Column(String(50),nullable=False)

class DevelopersModel(settings.DBBASEMODEL):
    __tablename__ = 'developers'
    id: int = Column(Integer,nullable=False,primary_key=True)
    name: str = Column(String(50),nullable=False)

class PublishersModel(settings.DBBASEMODEL):
    __tablename__ = 'publishers'
    id: int = Column(Integer,nullable=False,primary_key=True)
    name: str = Column(String(50),nullable=False)