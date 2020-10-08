"""
CP1404 Practical - Code to test Silver Service Taxi class
Rhys Simpson
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test Silver Service Taxi class"""
    my_taxi = SilverServiceTaxi("Luxury Taxi", 200, 2)
    print(my_taxi)
    my_taxi.drive(18)
    print(my_taxi)
    print("$", my_taxi.get_fare())


main()
