"""
CP1404 Practical

Rhys Simpson
"""


words = []
text = input("Enter a word: ")
word = text.split()
words.append(word)


repeat_words = [word for word in words if word in words]
print("Strings repeated: {}".format(repeat_words))
if not repeat_words:
    print("No repeat strings entered")
