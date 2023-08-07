from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.utils.auth import authenticate_user, create_access_token, get_current_user
from app.schemas.user import TokenData, UserInDB, User, UserCreate
from app.services.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.post("/token", response_model=TokenData)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token_expires = timedelta(hours=1)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me/", response_model=User)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

router.post("/signup", response_model=UserInDB)
async def signup(user: UserCreate):
    return user_service.signup(user)
