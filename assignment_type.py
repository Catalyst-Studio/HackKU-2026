from pydantic import BaseModel

class AssignmentType(BaseModel):
    userID: str
    baseType: str
    hasSetTime: bool
    name: str