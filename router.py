from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from fastapi_login.exceptions import InvalidCredentialsException

import user
router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def base(request: Request):
    return RedirectResponse(url="/login")


@router.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse(request, "register.html", {
        "request": request,
        "title": "Register"
    })


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

    if not user:
        # you can return any response or error of your choice
        raise InvalidCredentialsException
    elif password != user["password"]:
        raise InvalidCredentialsException

    return {"status": "Success"}


@router.get("/home")
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {
        "request": request,
        "title": "Home"
    })