"""CP1404/CP5632 Practical
 Estimated time: 40 min
 Actual time: 1 hour"""
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        formatted_cost = "${:,.2f}".format(self.cost)  # Format cost with comma separator and 2 decimal places
        return "{} ({}) : {}".format(self.name, self.year, formatted_cost)

    def get_age(self):
        current_year = 2022  # Assuming current year is 2022
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50
