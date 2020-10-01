"""
CP1404 - Practical
Dictionary that stores name and addresses

Rhys Simpson
"""

MENU = "Menu:\nN - New name & address\nC - Change address\nP - Print address\nQ - Quit\n>>> "


def main():
    """ """
    name_and_address = {"Jim": "5 Town Street", "Bob": "2 Small Street"}
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "N":
            add_new_entry(name_and_address)
        elif choice == "C":
            change_address(name_and_address)
        elif choice == "P":
            print_address(name_and_address)
        else:
            print("Invalid menu choice")
        choice = input(MENU).upper()
    print("Have a nice day!")
    quit()


def add_new_entry(name_and_address):
    name = input("Name: ")
    while name == "":
        print("Input can not be blank")
        name = input("Name: ")
    address = input("Address: ")
    while address == "":
        print("Input can not be blank")
        address = input("Address: ")
    name_and_address[name] = address


def change_address(name_and_address):
    name = input("Enter name: ")
    if name in name_and_address:
        new_address = input("Enter new address: ")
        name_and_address[name] = new_address


def print_address(name_and_address):
    name = input("Enter name: ")
    if name in name_and_address:
        print(name, "address is", name_and_address[name])


main()

