from hashlib import md5
from random import randbytes


async def new_csrf(length: int = 12) -> dict:
    secret = str(randbytes(length))
    token = str(md5(secret).digest())
    return {
        "secret": secret,
        "token": token
    }


async def verify_csrf(secret: str, token: str) -> bool:
    hash = str(md5(secret).digest())
    return hash == token
