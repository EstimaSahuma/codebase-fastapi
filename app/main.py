from fastapi import FastAPI
from app.api.v1.exemple_endpoint import router as v1_router
from app.api.auth_endpoint import router as auth_router

app = FastAPI()

app.include_router(v1_router, prefix="/v1")
app.include_router(auth_router, prefix="/auth")
