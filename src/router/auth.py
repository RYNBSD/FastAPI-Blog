from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/sign-up")
async def sign_up():
    pass

@router.post("/sign-in")
async def sign_in():
    pass

@router.post("/sign-out")
async def sign_out():
    pass

@router.post("/me")
async def sign_me():
    pass