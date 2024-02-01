from hashlib import md5
from random import randbytes


def new_csrf(length: int = 12) -> dict:
    secret = randbytes(length).decode()
    token = md5(secret).digest().decode()
    return {
        "secret": secret,
        "token": token
    }


def verify_csrf(secret: str, token: str) -> bool:
    hash = md5(secret).digest().decode()
    return hash == token
