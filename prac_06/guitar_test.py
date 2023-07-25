"""CP1404/CP5632 Practical
 Estimated time: 40 min
 Actual time: 1 hour 20 min"""
from guitar import Guitar
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 5000)

# Testing get_age() method
print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age()}")

# Testing is_vintage() method
print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")