"""
CP1404 Practical - Programming languages class
Rhys Simpson
"""


class ProgrammingLanguage:
    """Represent Programming Languages information"""

    def __init__(self, name,  typing, reflection, year):
        """Initialise a ProgrammingLanguage from values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string of ProgrammingLanguage fields"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        """Determine if ProgrammingLanguage has dynamic typing"""
        return self.typing == "Dynamic"
