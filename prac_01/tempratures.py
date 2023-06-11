"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
display menu
get choice
while choice != quit option
    if choice == c
        get temperature in Celsius
        convert Celsius to Fahrenheit
    else if choice == f
        get temperature in Fahrenheit
        convert Fahrenheit to Celsius
    else
        display invalid input error message
    display menu
    get choice
print thank you
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":

        fahrenheit = float(input("fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
