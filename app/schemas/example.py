from pydantic import BaseModel
from typing import List

class ExampleBase(BaseModel):
    name: str
    description: str

class ExampleCreate(ExampleBase):
    pass

class Example(ExampleBase):
    id: int 

    class Config:
        orm_mode = True

class ExampleList(BaseModel):
    data: List[Example]
    