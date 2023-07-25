from guitar import Guitar


def main():
    print("My Guitars!")
    guitars = []
    name = input("Name: ")
    while name != "":
        year_of_guitar = int(input("Years: "))
        cost_of_guitar = float(input("Cost: $"))
        print()

        guitar = Guitar(name, year_of_guitar, cost_of_guitar)
        guitars.append(guitar)
        print(f"{guitar} added.")
        print("\nThese are my guitars:")
        name = input("Name: ")

    print()
    print("Formatted Output:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:,.2f}{vintage_string}")


main()
