"""
CP1404
Random word generator
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    word = is_valid_format()
    print(word)


def is_valid_format():
    word_format = input("Enter a letter: ")
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        elif kind == "v":
            word += random.choice(VOWELS)
        else:
            return False


main()
