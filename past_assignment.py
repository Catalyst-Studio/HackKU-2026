from datetime import datetime
from pydantic import BaseModel
from class_ import Class as _class
import assignment_type


class PastAssignment(BaseModel):
    userID: str
    class_: _class
    type: assignment_type.AssignmentType
    length: int
    name: str
    difficulty: str
    timeCompleted: datetime
    dueDate: datetime