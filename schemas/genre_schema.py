from pydantic import BaseModel as SchemaBaseModel


class GenreSchema(SchemaBaseModel):
    name: str

    class Config:
        from_attributes = True
