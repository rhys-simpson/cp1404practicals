"""
CP1404 - Unreliable Car class
Rhys Simpson
"""

from prac_08.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that determines its reliability"""

    def __init__(self, name, fuel, reliability):
        """Initialise an Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def __str__(self):
        """Return a string like a Car but with its reliability"""
        return "{}, Reliability: {}".format(super().__str__(), self.reliability)

    def drive(self, distance):
        """Drive like parent Car but check if car can drive based on its reliability"""
        number = random.randint(0, 100)
        if self.reliability < number:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
