from fastapi import Request, Response
from .crypto import Crypto

class Cookie(Crypto):
    def __init__(self, key: str):
        self.key = key
        Crypto.__init__(self, self.key)

    def split_res_cookie(cookie: str):
        return cookie.split(";")[0].split("=")

    async def middleware(self, req: Request, next):
        for k, v in req.cookies.items():
            req.cookies[k] = self.decrypt(v)

        res: Response = await next(req)

        res_cookies = res.headers.get("set-cookie")
        if res_cookies.isinstance(str):
            res_cookies = [res_cookies]

        if res_cookies.isinstance(list):
            for cookie in res_cookies:
                k, v = self.split_res_cookie(cookie)
                res.delete_cookie(k)
                res.set_cookie(k, self.encrypt(v.encode()), path="/",
                            httponly=False, secure=False, samesite="strict", max_age=0)

        return res
