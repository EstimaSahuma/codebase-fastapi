from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.exemple_service import ExampleService
from app.core.database import SessionLocal

router = APIRouter()
example_service = ExampleService()

@router.get("/examples/{example_id}")
def byId(example_id: int, db: Session = Depends(SessionLocal)):
    return example_service.byId(example_id)

@router.get("/examples")
def getAll(db: Session = Depends(SessionLocal)):
    return "All thing OK..." # example_service.getAll()

@router.post("/examples/")
def create_example(name: str, description: str, db: Session = Depends(SessionLocal)):
    return example_service.create_example(name, description)
