"""
CP1404/CP5632 Practical
Programming Language class with tests.
"""
FILE = 'guitars.csv'


class Guitar:
    """Represent information about a guitar."""

    def __init__(self, name, year, cost):
        """Construct a Guitar object from the given values."""
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}), ${self.cost:.2f}"

    def __lt__(self, other):
        """Define comparison for sorting based on year."""
        return self.year < other.year


def main():
    guitars = read_guitars_from_file(FILE)

    guitars.sort()  # Sorting the list of guitars based on the year attribute

    print("Guitars :")
    for guitar in guitars:
        print(guitar)
    print("")
    users_new_guitar = input("Do you want to add a new guitar? (yes/no):")
    while users_new_guitar.lower() == "yes":
        name = input("Enter the name of the guitar: ")
        year = int(input("Enter the year of the guitar: "))
        cost = float(input("Enter the cost of the guitar: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{name} ({year}), ${cost:.2f} has been added.\n")
        users_new_guitar = input("Do you want to add another guitar? (yes/no): ")

    guitars.sort()
    write_guitars_to_file(FILE, guitars)
    print("Guitars saved to guitars.csv.")
    print("Updated Guitar List:")
    for guitar in guitars:
        print(guitar)


def read_guitars_from_file(file_name):
    """Read guitars from the given file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                name, year, cost = line.strip().split(',')
                year = int(year)
                cost = float(cost)
                guitar = Guitar(name, year, cost)
                guitars.append(guitar)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except ValueError:
        print(f"Error: Invalid data format in '{file_name}'.")
    return guitars


def write_guitars_to_file(file_name, guitars):
    """Write guitars to the given file."""
    try:
        with open(file_name, 'w') as file:
            for guitar in guitars:
                file.write(f"{guitar}\n")
    except IOError:
        print(f"Error: Unable to write to file '{file_name}'.")


main()
