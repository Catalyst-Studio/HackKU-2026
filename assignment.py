from datetime import datetime
from pydantic import BaseModel
import assignment_type
import class_

class Assignment(BaseModel):
    userID: str
    class_: class_.Class
    type: assignment_type.AssignmentType
    length: int
    name: str
    difficulty: str
    estimatedTime: datetime
    dueDate: datetime