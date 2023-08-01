import random
from car import Car


class UnreliableCar(Car):
    """ version of car with an additional reliability attribute"""

    def __init__(self, name, fuel, reliability):
        """ Initialize a reliabilty instance"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car with a certain probability based on reliability."""
        if random.randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
