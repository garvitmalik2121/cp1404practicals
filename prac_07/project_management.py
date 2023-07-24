"""
practical 1404 prac 7
"""
import datetime
FILE = "project.txt"
class Project:
    "display information about project"""
    def __int__(self, name, start_date, priority, cost_estimate, completion_percentage):

        """Construct a Project object from the given values."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __repr__(self):
        """Return string representation of a Project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Define comparison for sorting based on priority."""
        return self.priority < other.priority