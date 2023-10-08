from pydantic import BaseModel as SchemaBaseModel
from typing import Optional,List
from datetime import datetime

class GameSchema(SchemaBaseModel):
    id: Optional[int]
    name: str
    genre: List[str]
    franchise: List[str]
    release_date: datetime.date
    developer: str
    publisher: str

    class Config:
        orm_mode = True