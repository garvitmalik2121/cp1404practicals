"""CP1404/CP5632 - Practical
password stars
"""
MINIMUM_LENGTH = 6


def main():
    password = get_valid_password()
    print_stars(password)


def get_valid_password():
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid input. Password should have a minimum length of", MINIMUM_LENGTH)
        password = input("Password: ")
    return password


def print_stars(password):
    for star in range(len(password)):
        print("*", end="")
    print()


main()
