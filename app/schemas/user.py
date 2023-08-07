from pydantic import BaseModel

class TokenData(BaseModel):
    username: str

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class User(BaseModel):
    username: str
    hashed_password: str

class UserInDB(User):
    id: int
