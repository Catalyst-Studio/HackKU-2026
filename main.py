from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi_login import LoginManager
from datetime import timedelta

import router
import user
from os import getenv, environ
from exceptions import NotAuthenticatedException

app = FastAPI()
manager = LoginManager(environ["secret"], token_url="/login", use_cookie=True, default_expiry=timedelta(days=5), use_header=False, not_authenticated_exception=NotAuthenticatedException)
manager.cookie_name = "GradePaceLogin"
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router=router.create_router(manager=manager))


@manager.user_loader()
def get_user(user_id: str):
    return user.get_user(user_id)


@app.exception_handler(NotAuthenticatedException)
def auth_exception_handler(request: Request, exc: NotAuthenticatedException):
    return RedirectResponse(url="/login")
