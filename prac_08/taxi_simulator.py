"""
CP1404 Practical - Taxi Simulator
Rhys Simpson
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive\n>>> "


def main():
    """Main program to simulate driving Taxi's"""
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's Drive!")
    choice = input(MENU).lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            print_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            while taxi_choice > len(list(taxis)):
                print("Not a valid choice.")
                print_taxis(taxis)
                taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif choice == "d":
            current_taxi.start_fare()
            distance = int(input("Drive how far? "))
            current_taxi.drive(distance)
            trip_fare = current_taxi.get_fare()
            print("Your {} trip will cost you {}".format(current_taxi.name, trip_fare))
            total_bill += trip_fare
        else:
            print("Invalid choice.")
        print("Bill to date: ${:.2f}".format(total_bill))
        choice = input(MENU).lower()
    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now: ")
    print_taxis(taxis)


def print_taxis(taxis):
    """ """
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
