from pydantic import BaseModel as SchemaBaseModel


class FranchiseSchema(SchemaBaseModel):
    name: str

    class Config:
        from_attributes = True
