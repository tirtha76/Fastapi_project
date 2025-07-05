from pydantic import BaseModel, Field
from typing import Optional

class ItemModel(BaseModel):
    title: str = Field(...)
    description: Optional[str] = Field(default="")

class ItemResponse(ItemModel):
    id: str
class DetailModel(BaseModel):
    location: str = Field(...)
    number: Optional[str|int] = Field(default="")
    ref_id : Optional[str] = Field(default="")

class DetailResponce(DetailModel):
    id:str