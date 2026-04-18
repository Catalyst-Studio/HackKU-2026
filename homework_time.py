from pydantic import BaseModel

class HomeworkTime(BaseModel):
    userID: str
    monday: list
    tuesday: list
    wednesday: list
    thursday: list
    friday: list
    saturday: list
    sunday: list