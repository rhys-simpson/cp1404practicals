"""
CP1404 Practical - Guitar class
Rhys Simpson
"""

import datetime
time = datetime.datetime.now()
VINTAGE_AGE = 50


class Guitar:
    """Represent Guitar models"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar information from values"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return guitar information string"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get guitar age"""
        return time.year - self.year

    def is_vintage(self):
        """Determine if guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE
