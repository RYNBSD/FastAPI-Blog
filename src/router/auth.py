from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from model.session import db_session

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/sign-up")
async def sign_up(db: Session = Depends(db_session)):
    pass


@router.post("/sign-in")
async def sign_in(db: Session = Depends(db_session)):
    pass


@router.post("/sign-out")
async def sign_out():
    pass


@router.post("/me")
async def sign_me(db: Session = Depends(db_session)):
    pass
