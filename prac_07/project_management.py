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


def main():
    projects = load_projects(FILE)
    menu = display_menu
    choice = get_choice
    while choice != "q":
        if choice == "l"
            load_file_name = input("Enter the filename to load projects from: ")
            projects = load_projects(load_file_name)
        elif choice == "s":
            save_file_name = input("Enter the filename to save projects to: ")
            write_projects_to_file(save_file_name, projects)
            print("Projects saved.")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            "Invalid choice "
        display_menu()
        get_choice()


save_changes = input("Do you want to save changes? (yes/no): ").lower()

if save_changes == 'yes':
    write_projects_to_file(FILE, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(file_name):
    projects = []
    try:
        with open(file_name, 'r') as file:
            file_name.readline()  # Skip the header line
            for line in file:
                name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
                project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                projects.append(project)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    return projects


def display_menu():
    print("\n- (L)oad projects",
          "\n- (S)ave projects",
          "\n- (D)isplay projects",
          "\n- (F)ilter projects by date",
          "\n- (A)dd new project",
          "\n- (U)pdate project",
          "\n- (Q)uit")


def get_choice():
    return input(">>> ").lower()


def write_projects_to_file(FILE, projects):
    pass


def display_projects(projects):


def filter_projects_by_date(projects):


def add_new_project(projects):


def update_project(projects):
