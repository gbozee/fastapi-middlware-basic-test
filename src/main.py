from typing import Union

from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from .auth import BasicAuthBackend
from starlette.middleware.authentication import AuthenticationMiddleware

middleware = [Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())]

app = FastAPI(middleware=middleware)


@app.get("/")
def read_root(request: Request):
    if request.user.is_authenticated:
        return request.user
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
