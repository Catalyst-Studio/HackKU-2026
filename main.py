from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_login import LoginManager
from datetime import timedelta

import router
import user
from os import getenv, environ

app = FastAPI()
manager = LoginManager(environ["secret"], token_url="/login", use_cookie=True, default_expiry=timedelta(days=5), use_header=False)
manager.cookie_name = "GradePaceLogin"
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router=router.router)


@manager.user_loader()
def get_user(user_id: str):
    return user.get_user(user_id)
