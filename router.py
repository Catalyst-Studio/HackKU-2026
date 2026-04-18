from typing import Annotated

from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

import user


def create_router(manager: LoginManager):
    router = APIRouter()
    templates = Jinja2Templates(directory="templates")

    @router.get("/")
    async def base(request: Request):
        return RedirectResponse(url="/login")

    @router.get("/logout")
    async def logout():
        resp = RedirectResponse("/login")
        resp.delete_cookie(manager.cookie_name)
        return resp

    @router.get("/register")
    async def register_page(request: Request):
        return templates.TemplateResponse(request, "register.html", {
            "request": request,
            "title": "Register"
        })

    @router.post("/register")
    async def register(name: Annotated[str, Form()], data: OAuth2PasswordRequestForm = Depends()):
        email = data.username
        password = data.password
        new_user = user.create_user(name=name, email=email, password=password)
        access_token = manager.create_access_token(
            data={"sub": new_user.userID}
        )
        resp = RedirectResponse("/home")
        resp.set_cookie(key=manager.cookie_name, value=access_token, httponly=True, path='/',
                        max_age=(365 * 24 * 60 * 60))
        return resp

    @router.get("/login")
    def login_page(request: Request):
        return templates.TemplateResponse(request, "login.html", {
            "request": request,
            "title": "Login"
        })

    @router.post("/login")
    def login(data: OAuth2PasswordRequestForm = Depends()):
        email = data.username
        password = data.password

        validated_user = user.validate_user(email, password)

        if user is None:
            raise InvalidCredentialsException
        else:
            access_token = manager.create_access_token(
                data={"sub": validated_user.userID}
            )
            resp = RedirectResponse("/home")
            resp.set_cookie(key=manager.cookie_name, value=access_token, httponly=True, path='/',
                            max_age=(365 * 24 * 60 * 60))
            return resp

    return router