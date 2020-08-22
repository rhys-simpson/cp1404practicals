"""
CP1404 - Practical
Convert temps

Rhys Simpson
"""

import random


def main():
    """ Convert input file to output file"""
    in_file = open("temps_input.txt", "r")
    output_file = open("temps_output", "w")
    for line in in_file:
        result = fahrenheit_to_celsius(float(line))
        print(result, file=output_file)
    in_file.close()
    output_file.close()


def create_input_file(quantity):
    """Write temperatures to file."""
    temperatures_file = open("temps_input.txt", "w")
    for i in range(quantity):
        temperature = random.uniform(-200, 200)
        print(temperature, file=temperatures_file)
    temperatures_file.close()


def fahrenheit_to_celsius(fahrenheit):
    """ Convert fahrenheit to celsius """
    return 5 / 9 * (fahrenheit - 32)


def celsius_to_fahrenheit(celsius):

    return celsius * 9.0 / 5 + 32


main()
