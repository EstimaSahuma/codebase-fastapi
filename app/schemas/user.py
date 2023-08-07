from pydantic import BaseModel

class TokenData(BaseModel):
    username: str

class UserBase(BaseModel):
    username: str
    hashed_password: str

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserInDB(UserBase):
    id: int
