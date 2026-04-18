from datetime import datetime
from pydantic import BaseModel
import assignment_type
import class1

class Assignment(BaseModel):
    userID: str
    class1: class1.Class
    type: assignment_type.AssignmentType
    length: int
    name: str
    difficulty: str
    estimatedTime: datetime
    dueDate: datetime