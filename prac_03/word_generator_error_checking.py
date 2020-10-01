"""
CP1404
Random word generator
"""
# TODO error checking
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    word_format = input("Enter a word consisting of c's & v's: ")
    while word_format == "":
        print("Enter a valid word")
        word_format = input("Enter a word consisting of c's & v's: ")
    print(is_valid_format(word_format))


def is_valid_format(word_format):
    for kind in word_format:
        if kind != "c" and kind != "v":
            return False
    else:
        return True


main()
