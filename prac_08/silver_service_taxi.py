"""
CP1404 Practical - Silver Service Taxi Class
Rhys Simpson
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes ..."""

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi"""
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km *= self.fanciness

    def __str__(self):
        """Return a string of Silver Service Taxi object"""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Get the fare - $4.50 is added for silver service taxis"""
        return super().get_fare() + self.flagfall
