"""
CP1404 - Practical
Temperature conversions

Rhys Simpson
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():

    # menu to determine user choice and print results
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def fahrenheit_to_celsius(fahrenheit):
    """ Convert fahrenheit to celsius """
    return 5 / 9 * (fahrenheit - 32)


def celsius_to_fahrenheit(celsius):
    """ Convert celsius to fahrenheit """
    return celsius * 9.0 / 5 + 32


main()
