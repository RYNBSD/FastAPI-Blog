from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from model.session import db_session
from uuid import UUID

router = APIRouter(prefix="/blog", tags=["blog"])


@router.get("/all")
async def all(db: Session = Depends(db_session)):
    pass


@router.get("/{blog_id}")
async def blog(blog_id: UUID, db: Session = Depends(db_session)):
    pass


@router.get("/{blog_id}/likes")
async def blog_likes(blog_id: UUID, db: Session = Depends(db_session)):
    pass


@router.get("/{blog_id}/comments")
async def blog_comments(blog_id: UUID, db: Session = Depends(db_session)):
    pass


@router.patch("/{blog_id}/like")
async def like(blog_id: UUID, db: Session = Depends(db_session)):
    pass


@router.post("/")
async def create_blog(db: Session = Depends(db_session)):
    pass


@router.post("/{blog_id}/comment")
async def create_comment(blog_id: UUID, db: Session = Depends(db_session)):
    pass


@router.put("/{blog_id}")
async def update_blog(blog_id: UUID, db: Session = Depends(db_session)):
    pass


@router.put("/{blog_id}")
async def update_comment(blog_id: UUID, db: Session = Depends(db_session)):
    pass


@router.delete("/{blog_id}")
async def delete_blog(blog_id: UUID, db: Session = Depends(db_session)):
    pass


@router.delete("/{blog_id}/{comment_id}")
async def delete_comment(blog_id: UUID, comment_id: int, db: Session = Depends(db_session)):
    pass
