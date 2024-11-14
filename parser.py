from models import Class, Days
from typing import List, Dict
import toml

class Parser:
    def __init__(self, file: str) -> None:
        with open(file, "r") as f:
            self.data = toml.load(f)

    def parse(self) -> Dict[str, List[Class]]:
        taken_classes: list = []
        wanted_classes: list = []
        
        # Load preferences
        classes_taken: set = set(self.data.get("preferences", {}).get("classes_taken", []))
        classes_wanted: set = set(self.data.get("preferences", {}).get("classes_wanted", []))

        # Parse schedule and categorize based on preferences
        for course in self.data.get("schedule", []):
            name: str = course.get("code").strip()
            days: list[Days] = self.convert_days(course.get("days", []))
            start_time: str  = course.get("start_time")
            end_time: str = course.get("end_time")

            if name and days and start_time and end_time:
                class_instance: Class = Class(name, days, start_time, end_time)
                
                if name in classes_taken:
                    taken_classes.append(class_instance)
                elif name in classes_wanted:
                    wanted_classes.append(class_instance)
        
        return {
            "taken_classes": taken_classes,
            "wanted_classes": wanted_classes
        }

    def convert_days(self, days: List[str]) -> List[Days]:
        day_mapping: dict[str, Days] = {
            "Monday": Days.MONDAY,
            "Tuesday": Days.TUESDAY,
            "Wednesday": Days.WEDNESDAY,
            "Thursday": Days.THURSDAY,
            "Friday": Days.FRIDAY,
            "Saturday": Days.SATURDAY,
            "Sunday": Days.SUNDAY
        }

        return [day_mapping[day] for day in days if day in day_mapping]
