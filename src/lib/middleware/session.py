from fastapi import Request, Response
from json import dumps, loads


class Session:
    def __init__(self, cookie_name: str):
        self.cookie_name = cookie_name

    async def middleware(self, req: Request, next):
        cookies = req.cookies
        session = dict()

        for k, v in cookies.items():
            if k == self.cookie_name:
                decrypt_json = self.decrypt(v.encode())
                session = loads(decrypt_json)
                break

        req.session = session
        res: Response = await next(req)

        res.set_cookie(self.cookie_name, dumps(req.session), path="/",
                        httponly=False, secure=False, samesite="strict", max_age=0)

        return res
