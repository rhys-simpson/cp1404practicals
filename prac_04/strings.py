"""
CP1404 Practical

Rhys Simpson
"""

words = []
word = input("Enter a word: ")

if word in words:
    print("Strings repeated {}".format(word))
else:
    print("No repeat strings entered")
