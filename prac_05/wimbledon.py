"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 40 minutes
Actual:  1 hour 30 minutes
"""


def main():
    """
     Main function to read the Wimbledon data file, process the data, and display the results.
     """
    filename = "wimbledon.csv"

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()

    # Process the data
    data = [line.strip().split(",") for line in lines]
    champions, countries = process_data(data)
    display_champions(champions)
    display_countries(countries)


def process_data(data):
    """ Process the Wimbledon data and count the number of wins for each champion
    and collect the unique countries of the champions_to_count.
"""
    champions_to_count = {}
    countries = set()

    for row in data[1:]:
        champion = row[2]
        country = row[1]

        if champion in champions_to_count:
            champions_to_count[champion] += 1
        else:
            champions_to_count[champion] = 1

        countries.add(country)

    return champions_to_count, countries


def display_champions(champions):
    """Display the list of Wimbledon champions and the number of times they have won."""
    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")


def display_countries(countries):
    """Display the list of countries in alphabetical order."""
    sorted_countries = sorted(countries)
    countries_string = ", ".join(sorted_countries)
    print(f"\nThese {len(sorted_countries)} countries have won Wimbledon:")
    print(countries_string)


main()
