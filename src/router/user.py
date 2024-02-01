from fastapi import APIRouter
from uuid import UUID

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/{user_id}/info")
async def info(user_id: UUID):
    pass


@router.get("/{user_id}/blog")
async def blog(user_id: UUID):
    pass


@router.put("/")
async def update():
    pass


@router.delete("/")
async def delete():
    pass
