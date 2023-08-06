from sqlalchemy.orm import Session
from app.models.exemple import Example

class ExampleRepository:
    def __init__(self, db: Session):
        self.db = db

    def byId(self, example_id: int):
        return self.db.query(Example).filter(Example.id == example_id).first()
    
    def getAll(self):
        return self.db.query(Example).all()

    def create_example(self, example_data):
            example = Example(**example_data)
            self.db.add(example)
            self.db.commit()
            self.db.refresh(example)
            return example
