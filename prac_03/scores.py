"""
CP1404 - Practical (Practice)
Random Scores

Rhys Simpson
"""

import random


def main():
    # Get number of scores from user
    num_of_scores = int(input("Enter number of scores: "))
    out_file = open("results.txt", "w")
    for i in range(num_of_scores):
        score = random.randint(0, 100)
        print("{} is {}".format(score, determine_grade(score)))
        print("{} is {}".format(score, determine_grade(score)), file=out_file)
    out_file.close()


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


main()
