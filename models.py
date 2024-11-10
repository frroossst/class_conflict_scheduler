from datetime import datetime
from enum import Enum
from typing import List

class Days(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    def __str__(self) -> str:
        case = {
            Days.MONDAY: "Mon",
            Days.TUESDAY: "Tue",
            Days.WEDNESDAY: "Wed",
            Days.THURSDAY: "Thu",
            Days.FRIDAY: "Fri",
            Days.SATURDAY: "Sat",
            Days.SUNDAY: "Sun"
        }
        if day := case.get(self):
            return day
        raise ValueError("Invalid day")

class Class:
    name: str
    # list of days
    days: List[Enum]
    # start time
    start_time: datetime
    # end time
    end_time: datetime

    def __init__(self, name, days, start_time, end_time, *args) -> None:
        # check for valid name
        if not name:
            raise ValueError("Name cannot be empty")
        
        # check for valid days
        if not days or not all(isinstance(day, Days) for day in days):
            raise ValueError("Days cannot be empty")

        # check for valid start time
        if not start_time:
            raise ValueError("Start time cannot be empty")
        
        # check for valid end time
        if not end_time:
            raise ValueError("End time cannot be empty")
        
        # check for valid end time
        if end_time <= start_time:
            raise ValueError("End time must be greater than start time")

        self.name = name
        self.days = days
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.end_time = datetime.strptime(end_time, "%H:%M")

    def __str__(self) -> str:
        return (
            f"Class: {self.name}\n"
            f"Days: {', '.join(str(day) for day in self.days)}\n"
            f"Time: {self.start_time.strftime('%H:%M')} to {self.end_time.strftime('%H:%M')}"
        )

    def pretty(self) -> str:
        ITALICS = "\033[3m"
        RESET = "\033[0m"

        """
        CLASS NAME (in cyan)
            Days: Mon, Tue, Wed (in italics)
            Time: 09:00 to 10:00
        """
        
        return (
            f"{self.name}\n"
            f"\t{ITALICS}{', '.join(str(day) for day in self.days)}{RESET}\n"
            f"\t{self.start_time.strftime('%H:%M')} to {self.end_time.strftime('%H:%M')}"
        )
