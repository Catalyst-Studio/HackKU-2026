import base64
import hashlib
import uuid
from os import urandom

from assignment import Assignment
from assignment_type import AssignmentType
from class_ import Class
from crud import database
import bcrypt
from pydantic import BaseModel, Field

from homework_time import HomeworkTime
from past_assignment import PastAssignment


def get_user(user_id: str):
    user = database["Users"].find_one({"userID": user_id})
    assignment_types = database["AssignmentTypes"].find({"userID": user_id})
    assignments = database["Assignments"].find({"userID": user_id})
    classes = database["Classes"].find({"userID": user_id})
    homework_times = database["HomeworkTimes"].find({"userID": user_id})
    past_assignments = database["PastAssignments"].find({"userID": user_id})
    assignment_types = [AssignmentType(**doc) for doc in assignment_types]
    assignments = [Assignment(**doc) for doc in assignments]
    classes = [Class(**doc) for doc in classes]
    homework_times = HomeworkTime(**homework_times)
    past_assignments = [PastAssignment(**doc) for doc in past_assignments ]
    return User(
        userID=user["userID"],
        name=user["name"],
        email=user["email"],
        start_of_week=user["start_of_week"],
        salt=user["salt"],
        password=user["password"],
        assignment_types=assignment_types,
        assignments=assignments,
        classes=classes,
        homework_times=homework_times,
        past_assignments=past_assignments
    )


def validate_user(email: str, password: str):
    user = database["Users"].find_one({"email": email})
    if user is None:
        return None
    encrypted_password = encrypt_password(password=password, salt_raw=user["salt"])
    if encrypted_password == user["password"]:
        return User(userID=user["userID"], name=user["name"], email=user["email"], start_of_week=user["start_of_week"], salt=user["salt"], password=user["password"])
    else:
        return None


def encrypt_password(password: str, salt_raw: str):
    salt = base64.b64decode(salt_raw.encode())
    utf_8_password = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(utf_8_password, salt)
    hashed_password_string = base64.b64encode(hashed_password).decode()
    return hashed_password_string


def create_user(name: str, email: str, password: str):
    userid = str(uuid.uuid4())
    salt = bcrypt.gensalt()
    salt_string = base64.b64encode(salt).decode()
    encrypted_password = encrypt_password(password, salt_string)
    user = User(
        userID=userid,
        name=name,
        password=encrypted_password,
        salt=salt_string,
        start_of_week="Monday",
        email=email
    )
    database["Users"].insert_one(user.model_dump())
    return user



class User(BaseModel):
    userID: str
    name: str
    password: str
    salt: str
    start_of_week: str
    email: str

    assignment_types: list[AssignmentType] | None = Field(exclude=True, default=None)
    assignments: list[Assignment] | None = Field(exclude=True, default=None)
    classes: list[Class] | None = Field(exclude=True, default=None)
    homework_times: HomeworkTime | None = Field(exclude=True, default=None)
    past_assignments: list[PastAssignment] | None = Field(exclude=True, default=None)

    def store_class(self, class_: Class):
        database["Classes"].insert_one(class_.model_dump())

    def store_assignment_type(self, assignment_type: AssignmentType):
        database["AssignmentTypes"].insert_one(assignment_type.model_dump())

    def store_homework_time(self, homework_times: HomeworkTime):
        database["HomeworkTimes"].insert_one(homework_times.model_dump())

    def store_assignment(self, assignment: Assignment):
        database["Assignments"].insert_one(assignment.model_dump())
