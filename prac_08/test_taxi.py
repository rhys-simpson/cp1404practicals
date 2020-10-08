"""
CP1404 - code to test Taxi class
Rhys Simpson
"""

from prac_08.taxi import Taxi


def main():
    """Test taxi class"""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print("{}, Current fare: ${}".format(my_taxi, my_taxi.get_fare()))
    my_taxi.start_fare()
    my_taxi.drive(100)
    print("{}, Current fare: ${}".format(my_taxi, my_taxi.get_fare()))


main()
