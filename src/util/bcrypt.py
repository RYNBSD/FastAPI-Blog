from bcrypt import hashpw, checkpw, gensalt


def hash(password: str) -> bool:
    return hashpw(password.encode(), gensalt())


def compare(hash: str, password: str) -> bool:
    return checkpw(password.encode(), hash.encode())
