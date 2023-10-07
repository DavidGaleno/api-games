import datetime
from pydantic import BaseModel

from typing import List
class Game(BaseModel):

    name: str
    genre: List[str]
    franchise: str
    release_date: datetime.date
    developer: str
    publisher: str


    