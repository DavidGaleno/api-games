from datetime import date
from pydantic import BaseModel

class Game(BaseModel):

    name: str
    genre: int
    franchise: str
    release_date: date
    developer: str
    publisher: str

    def __init__(self,name,genre,franchise,release_date,developer,publisher):
        self.name = name
        self.genre = genre
        self.franchise = franchise
        self.release_date = release_date
        self.developer = developer
        self.publisher = publisher

    