"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
import random


def main():
    score = float(input("Enter score: "))
    print(print_remarks(score))
    score = random.randint(0, 100)
    print(score)
    print(print_remarks(score))


def print_remarks(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


main()
