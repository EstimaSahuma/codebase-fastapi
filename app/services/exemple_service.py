from app.repositories.exemple_repository import ExampleRepository
from app.core.database import SessionLocal

class ExampleService:
    def __init__(self):
        self.db = SessionLocal()
        self.example_repo = ExampleRepository(self.db)

    def get_example(self, example_id: int):
        return self.example_repo.get_example(example_id)

    def create_example(self, name: str, description: str):
        return self.example_repo.create_example(name, description)
