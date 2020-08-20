"""
CP1404 - Practical
Program to determine score status

Rhys Simpson
"""

import random


def main():
    # Get user score and print corresponding grade
    score = float(input("Enter score: "))
    print(determine_grade(score))


# Determine grade
def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


# c. wasn't sure if we were suppose to add another function for random score
score = random.uniform(1, 100)
print("Random score was: {:,.2f}".format(score))
print(determine_grade(score))

main()
