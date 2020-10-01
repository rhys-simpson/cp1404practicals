"""
CP1404 Practical - Program for Car class
Rhys Simpson
"""

from prac_06.car import Car
MENU = "Menu:\nd) Drive\nr) Refuel\nq) Quit"


def main():
    """ """
    print("Let's drive!")
    car_name = input("Enter your car name: ")
    my_car = Car(car_name, 100)
    print(my_car)
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            drive_car(my_car)
        elif choice == "r":
            refuel_car(my_car)
        else:
            print("Invalid menu choice")
        print()
        print(my_car)
        print(MENU)
        choice = input("Enter your choice: ").lower()
    print("\nGoodbye {}'s driver".format(car_name))


def drive_car(my_car):
    """ """
    drive_kms = int(input("How many km do you want to drive? "))
    while drive_kms < 0:
        print("Distance must be >= 0")
        drive_kms = int(input("How many km do you want to drive? "))

    distance_driven = my_car.drive(drive_kms)
    print("The car drove {}km".format(distance_driven), end="")

    if my_car.fuel == 0:
        print(" and ran out of fuel.")


def refuel_car(my_car):
    """ """
    fuel_amount = int(input("How many units of fuel do you want to add to the car? "))
    while fuel_amount < 0:
        print("Fuel amount must be >= 0")
        fuel_amount = int(input("How many units of fuel do you want to add to the car? "))

    my_car.add_fuel(fuel_amount)
    print("Added {} units of fuel.".format(fuel_amount))


main()
