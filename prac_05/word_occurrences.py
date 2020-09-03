"""
CP1404 - Practical
Count word occurrences

Rhys Simpson
"""

word_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    number = word_count.get(word, 0)
    word_count[word] = number + 1

words = list(word_count.keys())
words.sort()
max_word_length = max(len(word) for word in words)
for word in words:
    print("{:{}} : {}".format(word, max_word_length, word_count[word]))

