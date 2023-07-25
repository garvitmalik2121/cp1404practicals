"""
practical 1404 prac 7
project management
"""
import datetime

FILE = "projects.txt"


class Project:
    "display information about project"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
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
    display_menu()
    choice = get_choice()
    while choice != "q":
        if choice == "l":
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
        choice = get_choice()

    write_projects_to_file(FILE, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(file_name):
    projects = []
    try:
        with open(file_name, 'r') as file:
            next(file)  # Skip the header line
            for line in file:
                parts = line.strip().split()
                name = " ".join(parts[:-4])
                start_date, priority, cost_estimate, completion_percentage = parts[-4:]
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


def write_projects_to_file(file_name, projects):
    try:
        with open(file_name, 'w') as file:
            file.write("Name   Start Date   Priority   Cost Estimate   Completion Percentage\n")
            for project in projects:
                file.write(f"{project.name}   {project.start_date.strftime('%d/%m/%Y')}   {project.priority}   "
                           f"{project.cost_estimate:.2f}   {project.completion_percentage}\n")
    except IOError:
        print(f"Error: Unable to write to file '{file_name}'.")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    print("\nIncomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in sorted(completed_projects, key=lambda x: x.priority):
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date > filter_date]
        print("\nFiltered projects:")
        for project in sorted(filtered_projects, key=lambda x: x.start_date):
            print(f"  {project}")
    except ValueError:
        print("Invalid date format. Please use the format dd/mm/yyyy.")


def add_new_project(projects):
    print("\nLet's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)
    print("New project added.")


def update_project(projects):
    print_projects(projects)
    try:
        project_choice = int(input("Project choice: "))
        if 0 <= project_choice < len(projects):
            new_completion = input("New Percentage: ")
            projects[project_choice].completion_percentage = int(new_completion)
            new_priority = input("New Priority: ")
            if new_priority:
                projects[project_choice].priority = int(new_priority)
            print("Project updated.")
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Invalid input. Please enter a valid project index.")


def print_projects(projects):
    for index, project in enumerate(projects):
        print(f"{index} {project}")


main()
