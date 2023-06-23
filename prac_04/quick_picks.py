import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    num_quick_picks = int(input("How many quick picks? "))
    generate_quick_picks(num_quick_picks)


def generate_quick_picks(num_quick_picks):
    """Generate the specified number of quick picks."""
    for quick_pick in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)


def generate_quick_pick():
    """Generate a single quick pick (line of numbers)."""
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers


def print_quick_pick(quick_pick):
    """Print a quick pick (line of numbers) with proper formatting."""
    formatted_numbers = " ".join("{:2d}".format(number) for number in quick_pick)
    print(formatted_numbers)


main()
