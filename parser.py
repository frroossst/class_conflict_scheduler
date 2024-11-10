from typing import List
import toml

from scheduler import Class, Days

class Parser:
    def __init__(self, file: str) -> None:
        with open(file, "r") as f:
            self.data = toml.load(f)

    def parse(self) -> List[Class]:
        class_list = []
        for course in self.data.get("schedule", []):
            name = course.get("course_name")
            days = self.convert_days(course.get("days", []))
            start_time = course.get("start_time")
            end_time = course.get("end_time")
            if name and days and start_time and end_time:
                class_list.append(Class(name, days, start_time, end_time))
        return class_list

    def convert_days(self, days: List[str]) -> List[Days]:
        day_mapping = {
            "Monday": Days.MONDAY,
            "Tuesday": Days.TUESDAY,
            "Wednesday": Days.WEDNESDAY,
            "Thursday": Days.THURSDAY,
            "Friday": Days.FRIDAY,
            "Saturday": Days.SATURDAY,
            "Sunday": Days.SUNDAY
        }
        return [day_mapping[day] for day in days if day in day_mapping]
