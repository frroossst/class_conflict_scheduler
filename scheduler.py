# holds the schedule
# has utility methods to check
# for conflicts, overlap etc.
from typing import List
from models import Class


class Scheduler:
    def __init__(self, taken_classes: List['Class'], wanted_classes: List['Class']) -> None:
        self.taken_classes = taken_classes
        self.wanted_classes = wanted_classes
        self.conflict_graph: dict['Class', List['Class']] = {}

        # Build the conflict graph based on taken and wanted classes
        self.build_conflict_graph()

    def build_conflict_graph(self) -> None:
        """Build the conflict graph for the given classes."""
        all_classes: list[Class] = self.taken_classes + self.wanted_classes
        for i, class1 in enumerate(all_classes):
            self.conflict_graph[class1] = []
            for j, class2 in enumerate(all_classes):
                if i != j and self.check_conflict(class1, class2):
                    self.conflict_graph[class1].append(class2)

    def check_conflict(self, class1: 'Class', class2: 'Class') -> bool:
        """Check if two classes conflict."""
        # Check if the classes share any common day
        shared_days: set = set(class1.days) & set(class2.days)
        if not shared_days:
            return False

        # Check if their times overlap
        if (class1.start_time < class2.end_time and class1.end_time > class2.start_time):
            return True
        return False

    def report(self):
        """Generate a conflict report for each wanted class."""

        # ANSI escape codes for colors
        YELLOW = "\033[33m"
        CYAN = "\033[36m"
        BOLD = "\033[1m\033[37m"
        RED = "\033[31m"
        GREEN = "\033[32m"
        RESET = "\033[0m"

        for wanted_class in self.wanted_classes:
            conflicts = self.conflict_graph.get(wanted_class, [])
            drop_count = len(conflicts)

            # Print class name in yellow
            print(f"{CYAN}{wanted_class.name}{RESET} requires", end=" ")

            if drop_count > 0:
                # Print the number of drops in red if drops exist
                print(f"{RED}{drop_count}{RESET} drops.")
                print(f"{BOLD}-{RESET} {', '.join([YELLOW + conflict.name + RESET for conflict in conflicts])}{RESET}")
            elif drop_count == 0:
                # If no drops, print in green
                print(f"{GREEN}0{RESET} drops required.")

            # If there are no conflicts, print a green message
            if not conflicts:
                print(f"{BOLD}No conflicts, no drops required.{RESET}")

            print()

