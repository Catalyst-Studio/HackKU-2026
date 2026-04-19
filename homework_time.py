from collections import defaultdict
from datetime import datetime

from pydantic import BaseModel


def process_homework_times(form_dict: dict, userID: str):
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    availability = defaultdict(list)

    for day in days:
        for i in range(len(form_dict)):
            start = form_dict.get(f"{day}Time1-{i}")
            end = form_dict.get(f"{day}Time2-{i}")
            if start is not None and end is not None:
                availability[day].append({
                    "start": datetime.strptime(start, "%H:%M").time(),
                    "end": datetime.strptime(end, "%H:%M").time()
                })
    availability = dict(availability)
    return HomeworkTime(
        userID=userID,
        monday=availability.get("mon", []),
        tuesday=availability.get("tue", []),
        wednesday=availability.get("wed", []),
        thursday=availability.get("thu", []),
        friday=availability.get("fri", []),
        saturday=availability.get("sat", []),
        sunday=availability.get("sun", [])
    )



class HomeworkTime(BaseModel):
    userID: str
    monday: list
    tuesday: list
    wednesday: list
    thursday: list
    friday: list
    saturday: list
    sunday: list