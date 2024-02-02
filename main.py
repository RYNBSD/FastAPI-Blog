from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from time import time
from .src.router import auth, user, blog
from .src.lib.middleware import cookie, session

app = FastAPI()


@app.middleware("http")
async def response_time(req: Request, next):
    start = time()
    res = await next(req)
    end = time() - start
    res.headers["X-Response-Time"] = str(end)
    return res

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(GZipMiddleware, minimum_size=1000)


cookie = cookie.Cookie("secret")
session = session.Session("secret", "session")
@app.middleware("http")(cookie.middleware)
@app.middleware("http")(session.middleware)

@app.add_middleware("http")
async def pass_middleware(req: Request, next):
    return await next(req)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)

app.mount("/", StaticFiles(directory=""), "public")