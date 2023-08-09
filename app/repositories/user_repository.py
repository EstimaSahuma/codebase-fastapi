from sqlalchemy.orm import Session
#from app.schemas.user import UserBase
from app.utils.auth import get_password_hash
from app.models.user import User

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
    
    def getByUsername(self, username):
        return self.db.query(User).filter(User.username == username).first()
