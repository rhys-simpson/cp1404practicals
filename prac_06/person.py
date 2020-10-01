"""
CP1404 Practical
Person class
Rhys Simpson
"""


class Person:
    """Represent a person's details"""

    def __init__(self, first_name, last_name, age=0):
        """Initialise a Person instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return "First Name: {}\nLast Name: {}\nAge: {}".format(self.first_name, self.last_name, self.age)

    def __lt__(self, other):
        return self.age < other.age
