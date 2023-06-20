"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer: it will occur when we enter a input type other than int for numerator or the denominator
2. When will a ZeroDivisionError occur?
Answer: it will occur when user enter 0 as input for denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer: At 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("cannot divide by zero ")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("finished")