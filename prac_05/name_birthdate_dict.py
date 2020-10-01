"""
CP1404 Practical
Convert parallel list to dictionary
Rhys Simpson
"""

import datetime
time = datetime.datetime.now()

name_birthdate = {}

for i in range(5):
    name = input("Enter name: ")
    birthdate = input("Enter your birthdate (dd/mm/yyyy): ")
    name_birthdate[name] = birthdate

for name, birthdate in name_birthdate.items():
    parts = birthdate.split('/')
    birth_year = int(parts[2])
    print("{} is {} years old".format(name, time.year - birth_year))
