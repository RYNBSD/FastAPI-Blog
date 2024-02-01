from fastapi import FastAPI
from .src.router import auth, user, blog

app  = FastAPI()

app.include_router(auth.router)