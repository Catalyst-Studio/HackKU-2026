import base64
import hashlib
import uuid
from os import urandom
from crud import database
import bcrypt
from pydantic import BaseModel


def get_user(user_id: str):
    user = database["Users"].find_one({"userID": user_id})
    return User(userID=user["userID"], name=user["name"], email=user["email"], start_of_week=user["start_of_week"], salt=user["salt"], password=user["password"])


def validate_user(email: str, password: str):
    user = database["Users"].find_one({"email": email})
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