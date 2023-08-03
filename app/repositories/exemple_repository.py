from sqlalchemy.orm import Session
from app.models.exemple import Example

class ExampleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_example(self, example_id: int):
        return self.db.query(Example).filter(Example.id == example_id).first()

    def create_example(self, name: str, description: str):
        example = Example(name=name, description=description)
        self.db.add(example)
        self.db.commit()
        self.db.refresh(example)
        return example
