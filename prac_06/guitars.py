"""
CP1404 Practical - Client code to use Guitar class
Rhys Simpson
"""

from prac_06.guitar import Guitar


def main():
    """Program to add guitar to list using Guitar class"""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "added.")
        name = input("Name: ")

    # add guitars to list (match sample output)
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print_guitars(guitars)


def print_guitars(guitars):
    """Print guitars list"""
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        is_vintage = "(vintage)" if guitar.is_vintage() else ""
        print("Guitar {}: {:<20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  is_vintage))
    if not guitars:
        print("No guitars")


main()

