"""
CP1404 Practical - Date class
Rhys Simpson
"""

# TODO
class Date:
    """Represent the date"""

    def __init__(self, day, month, year):
        """ """
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        """ """
        return "Day: {} Month: {} Year: {}".format(self.day, self.month, self.year)

    def add_days(self, number):
        """ """
