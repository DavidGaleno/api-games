import datetime
from pydantic import BaseModel

from typing import List
from pydantic import BaseModel,validator
class Game(BaseModel):

    name: str 
    genre: List[str]
    franchise: str
    release_date: datetime.date
    developer: str
    publisher: str

    @validator('name')
    def name_validate(cls,value):
        value = value.lower()
        if len(value) == 0:
            raise ValueError('Insira pelo menos uma letra')
        return value



    