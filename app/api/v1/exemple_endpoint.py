from fastapi import APIRouter, HTTPException, Depends
from app.services.exemple_service import ExampleService
from app.schemas.example import Example, ExampleCreate
from app.schemas.user import User
from typing import List
from app.utils.auth import get_current_user

router = APIRouter()
example_service = ExampleService()

@router.get("/examples/{example_id}", response_model=Example)
def byId(example_id: int, current_user: User = Depends(get_current_user)):
    try:
        dta = example_service.byId(example_id) 
        return dta
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/examples/", response_model=List[Example])
async def getAll(current_user: User = Depends(get_current_user)):
    try:
        return example_service.getAll()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/examples/", response_model=ExampleCreate)
def create_example(example_data: ExampleCreate, current_user: User = Depends(get_current_user)):
    try:
        return example_service.create_example(example_data.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
