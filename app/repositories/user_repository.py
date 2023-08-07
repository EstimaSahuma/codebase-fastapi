from sqlalchemy.orm import Session
from app.schemas.user import User
from app.utils.auth import get_password_hash

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def signup(self, user_data):
        user = User(username=user_data.username,
                              hashed_password=get_password_hash(user_data.password))
        
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
