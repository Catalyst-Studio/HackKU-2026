from datetime import datetime
from pydantic import BaseModel

import assignment_type


class PastAssignments(BaseModel):
    userID: str
    class1: class1.Class
    type: assignment_type.AssignmentType
    length: int
    name: str
    difficulty: str
    timeCompleted: datetime
    dueDate: datetime