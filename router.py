from typing import Annotated

from assignment import Assignment
from assignment_type import AssignmentType
from class_ import Class
from flash import flash
from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse, JSONResponse
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
        times = []
        for hour in range(24):
            for minute in range(0, 60, 15):
                times.append(f"{hour:02d}:{minute:02d}")
        return templates.TemplateResponse(request, "home.html", {
            "request": request,
            "title": "Home",
            "user": current_user,
            "subjects": subjects,
            "times": times
        })

    @router.get("/api/classes")
    async def get_classes(request: Request, current_user: user.User = Depends(manager)):
        return JSONResponse(content=[m.model_dump(mode='json') for m in current_user.classes])

    @router.get("/api/assignment-types")
    async def get_assignment_types(request: Request, current_user: user.User = Depends(manager)):
        return JSONResponse(content=[m.model_dump(mode='json') for m in current_user.assignment_types])

    @router.get("/api/assignments")
    async def get_assignments(request: Request, current_user: user.User = Depends(manager)):
        return JSONResponse(content=[m.model_dump(mode='json') for m in current_user.assignments])

    @router.post("/api/assignments")
    async def receive_assignment(
            request: Request,
            assignment_name: Annotated[str, Form()],
            assignment_class: Annotated[str, Form()],
            assignment_due_date: Annotated[str, Form()],
            assignment_difficulty: Annotated[str, Form()],
            assignment_type: Annotated[str, Form()],
            assignment_length: Annotated[int, Form()],
            current_user: user.User = Depends(manager)
    ):
        current_user.store_assignment(
            Assignment(
                userID=current_user.userID,
                name=assignment_name,
                class_=assignment_class,
                dueDate=assignment_due_date,
                difficulty=assignment_difficulty,
                type=assignment_type,
                length=assignment_length
            )
        )

    @router.post("/api/homework-times")
    async def receive_homework_times(request: Request, current_user: user.User = Depends(manager)):
        form_data = await request.form()
        form_dict = dict(form_data)
        return JSONResponse(content={"message": "Homework times received successfully"})

    @router.post("/api/class")
    async def receive_class(request: Request,
                            class_name: Annotated[str, Form()],
                            class_subject: Annotated[str, Form()],
                            class_teacher: Annotated[str, Form()],
                            class_difficulty: Annotated[str, Form()],
                            current_user: user.User = Depends(manager)
                            ):
        current_user.store_class(
            Class(
                userID=current_user.userID,
                name=class_name,
                subject=class_subject,
                teacher=class_teacher,
                difficulty=class_difficulty
            )
        )
        return JSONResponse(content={"message": "Class created successfully"})

    @router.post("/api/assignment-type")
    async def receive_assignment_type(
            request: Request,
            assignment_type_name: Annotated[str, Form()],
            assignment_base_type: Annotated[str, Form()],
            assignment_type_has_set_time: Annotated[bool, Form()],
            current_user: user.User = Depends(manager)
    ):
        current_user.store_assignment_type(
            AssignmentType(
                userID=current_user.userID,
                baseType=assignment_base_type,
                name=assignment_type_name,
                hasSetTime=assignment_type_has_set_time
            )
        )
        return JSONResponse(content={"message": "Assignment type created successfully"})

    return router
