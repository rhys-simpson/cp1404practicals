"""
CP1404 Practical - Code to test Unreliable Car class
Rhys Simpson
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Run tests for Unreliable Car class"""

    good_car = UnreliableCar("GoodCar", 100, 75)
    bad_car = UnreliableCar("BadCar", 100, 25)

    for i in range(10):
        print("Test -", i + 1)
        print("{}, Drove: {}".format(good_car, good_car.drive(10)))
        print("{}, Drove: {}\n".format(bad_car, bad_car.drive(10)))

    print("Good car drove: {}km".format(good_car.odometer))
    print("Bad car drove: {}km".format(bad_car.odometer))


main()
