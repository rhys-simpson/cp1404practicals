"""
CP1404 - Practical
Number Loops

Rhys Simpson
"""

# Displays all odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. Displays all multiples of 10 from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. Displays all numbers counting down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. Ask user for a number and display '*' for the number that is inputted
num_stars = int(input("Number of Stars: "))
for i in range(num_stars):
    print('*', end=' ')
print()

# d. Using same number above print '*' in increasing '*' by line
for i in range(1, num_stars + 1):
    print('*' * i)
print()
