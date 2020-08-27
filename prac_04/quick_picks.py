"""
CP1404 Practical
Quick pick lottery ticket generator

Rhys Simpson
"""

import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6

picks = int(input("How many quick picks? "))
while picks < 0:
    print("Must have more than 0 picks")
    picks = int(input("How many quick picks? "))

for i in range(picks):
    numbers = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in numbers:
            number = random.randint(MINIMUM, MAXIMUM)
        numbers.append(number)
    numbers.sort()
    print(" ".join("{:2}".format(number) for number in numbers))
