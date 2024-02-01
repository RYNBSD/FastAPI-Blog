from fastapi import APIRouter, Path
from uuid import UUID

router = APIRouter(prefix="/blog", tags=["blog"])


@router.get("/all")
async def all():
    pass


@router.get("/{blog_id}")
async def blog(blog_id: UUID):
    pass


@router.get("/{blog_id}/likes")
async def blog_likes(blog_id: UUID):
    pass


@router.get("/{blog_id}/comments")
async def blog_comments(blog_id: UUID):
    pass


@router.patch("/{blog_id}/like")
async def like(blog_id: UUID):
    pass


@router.post("/")
async def create_blog():
    pass


@router.post("/{blog_id}/comment")
async def create_comment(blog_id: UUID):
    pass


@router.put("/{blog_id}")
async def update_blog(blog_id: UUID):
    pass


@router.put("/{blog_id}")
async def update_comment(blog_id: UUID):
    pass


@router.delete("/{blog_id}")
async def delete_blog(blog_id: UUID):
    pass


@router.delete("/{blog_id}/{comment_id}")
async def delete_comment(blog_id: UUID, comment_id: int):
    pass
