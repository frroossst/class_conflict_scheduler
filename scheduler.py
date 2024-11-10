# holds the schedule
# has utility methods to check
# for conflicts, overlap etc.
from typing import List
from models import Class


class Schedule:

    def __init__(self, classes: List[Class]) -> None:
        self.classes = classes

    def __str__(self) -> str:
        return "\n".join(str(cls) for cls in self.classes)

    def check_conflicts(self) -> bool:
        for i, cls1 in enumerate(self.classes):
            for j, cls2 in enumerate(self.classes):
                if i != j and self._conflict(cls1, cls2):
                    return True
        return False

    def _conflict(self, cls1, cls2) -> bool:
        if cls1.start_time <= cls2.start_time < cls1.end_time:
            return cls1.days.intersection(cls2.days)
        return False

    def check_overlap(self) -> bool:
        for i, cls1 in enumerate(self.classes):
            for j, cls2 in enumerate(self.classes):
                if i != j and self._overlap(cls1, cls2):
                    return True
        return False

    def _overlap(self, cls1, cls2) -> bool:
        if cls1.start_time < cls2.start_time < cls1.end_time:
            return cls1.days.intersection(cls2.days)
        return False

    def check_valid(self) -> bool:
        return not self.check_conflicts() and not self.check_overlap()
