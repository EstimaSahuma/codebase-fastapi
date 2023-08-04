from app.repositories.exemple_repository import ExampleRepository
from app.core.database import SessionLocal

class ExampleService:
    def __init__(self):
        self.db = SessionLocal()
        self.example_repo = ExampleRepository(self.db)

    def byId(self, example_id: int):
        return self.example_repo.byId(example_id)
    
    def getAll(self):
        return self.example_repo.getAll()

    def create_example(self, name: str, description: str):
        return self.example_repo.create_example(name, description)
