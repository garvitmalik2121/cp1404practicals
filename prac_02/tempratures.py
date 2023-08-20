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


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = get_valid_temperature()
            fahrenheit = convert_into_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = get_valid_temperature()
            celsius = convert_into_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_into_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def get_valid_temperature():
    temperature = float(input("Temperature: "))
    return temperature


def convert_into_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
