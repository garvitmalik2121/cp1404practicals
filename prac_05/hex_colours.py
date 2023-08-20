"""
CP1404/CP5632 Practical
colours name in dictionary
"""
NAME_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "	#f0f8ff", "Aqua": "#00ffff",
                "Ash Grey": "#b2beb5", "Baby Blue": "#89cff0", "Baby Pink": "#f4c2c2", "Banana Yellow": "#ffe135",
                "Barn Red": "#7c0a02", "Black": "#000000", "Blue Bell": "#a2a2d0"}
print(NAME_TO_CODE)
colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        colour_code = NAME_TO_CODE[colour_name]
        print(f"{colour_name} has colour code {colour_code}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()
print("finished")
