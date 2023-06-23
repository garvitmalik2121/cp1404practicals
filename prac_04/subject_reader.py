"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)  # add parts into list
    input_file.close()
    return data


def print_subject_details(data):
    """Print subject details: subject code, lecturer name, and number of students."""
    for subject in data:
        subject_code = subject[0]
        lecturer_name = subject[1]
        number_of_students = subject[2]
        print(f"{subject_code} is taught by {lecturer_name} and has {number_of_students} students")


main()
