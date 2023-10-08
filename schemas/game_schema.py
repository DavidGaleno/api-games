from pydantic import BaseModel as SchemaBaseModel
from typing import Optional
from datetime import date

class GameSchema(SchemaBaseModel):
    name: str
    genre: str
    franchise: str
    release_date: date
    developer: str
    publisher: str

    class Config:
        from_attributes = True
