from app.repositories.user_repository import UserRepository
from app.core.database import SessionLocal

class UserService:
    def __init__(self):
        self.db = SessionLocal()
        self.user_repo = UserRepository(self.db)

    def signup(self, user_data):
        return self.user_repo.signup(user_data)
    
    def getByUsername(self, username):
        return self.user_repo.getByUsername(username)
