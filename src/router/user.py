from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from model.session import db_session
from uuid import UUID

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{user_id}/info")
async def info(user_id: UUID, db: Session = Depends(db_session)):
    pass


@router.get("/{user_id}/blog")
async def blog(user_id: UUID, db: Session = Depends(db_session)):
    pass


@router.put("/")
async def update(db: Session = Depends(db_session)):
    pass


@router.delete("/")
async def delete(db: Session = Depends(db_session)):
    pass
