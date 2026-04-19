from typing import Annotated
from flash import flash
from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from fastapi_login import LoginManager

import user
from exceptions import NotAuthenticatedException
from flash import get_flashed_messages


def create_router(manager: LoginManager):
    router = APIRouter()
    templates = Jinja2Templates(directory="templates")
    templates.env.globals['get_flashed_messages'] = get_flashed_messages

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
        resp = RedirectResponse("/home", status_code=303)
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
    def login(request: Request, data: OAuth2PasswordRequestForm = Depends()):
        email = data.username
        password = data.password

        validated_user = user.validate_user(email, password)

        if validated_user is None:
            flash(request, "Invalid email or password", "danger")
            raise NotAuthenticatedException
        else:
            access_token = manager.create_access_token(
                data={"sub": validated_user.userID}
            )
            resp = RedirectResponse("/home", status_code=303)
            resp.set_cookie(key=manager.cookie_name, value=access_token, httponly=True, path='/',
                            max_age=(365 * 24 * 60 * 60))
            return resp

    @router.get("/home")
    async def home(request: Request, current_user: user.User = Depends(manager)):
        subjects = [
            "Math",
            "English",
            "Science",
            "History",
            "Social Studies",
            "Foreign Language",
            "Technology",
            "Arts",
            "Music",
            "Physical Education",
            "Health",
            "Business",
            "Engineering",
            "Philosophy"
        ]
        return templates.TemplateResponse(request, "home.html", {
            "request": request,
            "title": "Home",
            "user": current_user,
            "subjects": subjects
        })

    return router
