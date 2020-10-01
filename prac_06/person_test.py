"""
CP1404 Practical - test the person class
Rhys Simpson
"""

from prac_06.person import Person


def main():
    """Program to test Person class"""
    people = []
    print("Store peoples information.")
    number_of_people = int(input("How many people? "))
    for i in range(number_of_people):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        age = int(input("Enter age: "))
        add_person = Person(first_name, last_name, age)
        print(first_name, last_name, "added.")
        people.append(add_person)
    print_people(people)


def print_people(people):
    people.sort()
    for i, person in enumerate(people):
        print("Person {} -\n{}".format(i + 1, person))


main()
