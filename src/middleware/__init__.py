from fastapi import Request, HTTPException, status
from util.csrf import verify_csrf


def csrf(fn):
    async def wrapper(req: Request, *args, **kwargs):
        csrf_token = req.headers.get("X-CSRF-Token")
        csrf_secret = req.session["csrf"]["secret"]
        if not csrf_secret or not csrf_secret:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Empty csrf or secret")

        if verify_csrf("", csrf_token):
            return await fn(req, *args, **kwargs)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid CSRF Token")
    return wrapper
