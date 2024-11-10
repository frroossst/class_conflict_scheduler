# holds the schedule
# has utility methods to check
# for conflicts, overlap etc.
from typing import List
from models import Class


class Scheduler:
    def __init__(self, taken_classes: List['Class'], wanted_classes: List['Class']):
        self.taken_classes = taken_classes
        self.wanted_classes = wanted_classes
        self.conflict_graph = {}

        # Build the conflict graph based on taken and wanted classes
        self.build_conflict_graph()

    def build_conflict_graph(self):
        """Build the conflict graph for the given classes."""
        all_classes = self.taken_classes + self.wanted_classes
        for i, class1 in enumerate(all_classes):
            self.conflict_graph[class1] = []
            for j, class2 in enumerate(all_classes):
                if i != j and self.check_conflict(class1, class2):
                    self.conflict_graph[class1].append(class2)

    def check_conflict(self, class1: 'Class', class2: 'Class') -> bool:
        """Check if two classes conflict."""
        # Check if the classes share any common day
        shared_days = set(class1.days) & set(class2.days)
        if not shared_days:
            return False

        # Check if their times overlap
        if (class1.start_time < class2.end_time and class1.end_time > class2.start_time):
            return True
        return False

    def generate_report(self):
        """Generate a conflict report for each wanted class."""
        for wanted_class in self.wanted_classes:
            conflicts = self.conflict_graph.get(wanted_class, [])
            print(f"Wishing to take {wanted_class.name} requires {len(conflicts)} drops.")
            if conflicts:
                print(f"Classes to drop: {', '.join([conflict.name for conflict in conflicts])}")
            else:
                print("No conflicts, no drops required.")