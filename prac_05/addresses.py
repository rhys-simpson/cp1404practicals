"""
CP1404 - Practical
Dictionary that stores name and addresses

Rhys Simpson
"""

MENU = "Menu:\nN - New name & address\nC - Change address\nP - Print address\nQ - Quit\n>>> "


def main():
    """ """
    name_and_address = {}
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "N":
            name = input("Name: ")
            address = input("Address: ")
        elif choice == "C":

        elif choice == "P":

        else:
            print("Invalid menu choice")
        choice = input(MENU).upper()
    print("Have a nice day!")












main()
# TODO
