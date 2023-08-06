from fastapi import APIRouter, HTTPException
from app.services.exemple_service import ExampleService
from app.schemas import example
from typing import List

router = APIRouter()
example_service = ExampleService()

@router.get("/examples/{example_id}", response_model=example.Example)
def byId(example_id: int):
    try:
        dta = example_service.byId(example_id) 
        return dta
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/examples/", response_model=List[example.Example])
async def getAll():
    try:
        return example_service.getAll()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/examples/", response_model=example.ExampleCreate)
def create_example(example_data: example.ExampleCreate):
    try:
        return example_service.create_example(example_data.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
