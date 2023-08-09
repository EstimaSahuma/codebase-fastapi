from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends
from pydantic import ValidationError
from app.schemas.user import TokenData
from datetime import datetime, timedelta
import jwt
from app.core.database import SessionLocal
from app.core.config import pwd_context
from app.schemas.user import UserLogin
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
db = SessionLocal()

def authenticate_user(username: str, password: str):
    print("=========================")
    # user = UserLogin(username=_username, password=get_password_hash(password))
    #user =0
    user = db.query(User).filter(User.username == username).first()

    print(user.hashed_password)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "your-secret-key", algorithm="HS256")
    return encoded_jwt

def get_user_by_username(username: str):
    # Replace this with actual database query to retrieve user by username
    return User(username=username, hashed_password=pwd_context.hash("password"))

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, "your-secret-key", algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except jwt.ExpiredSignatureError:
        raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception
    user = get_user_by_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)
    
""" def authenticate_user(_username: str, _password: str):
        # Fetch the user from the database using the provided username
        # (database handling code goes here, use a database ORM like SQLAlchemy)
        user = UserInDB(_username, _password)
        if not user:
            return None
        if not verify_password(user.password, user.hashed_password):
            return None
        return user """
