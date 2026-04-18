from pydantic import BaseModel

class Class(BaseModel):
    userID: str
    subject: str
    difficulty: str
    teacher: str
    name: str