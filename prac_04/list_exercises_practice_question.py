"""
CP1404 Practical
List practice

Rhys Simpson
"""

numbers = []
total = 1
number = int(input("Enter number {}: ".format(total)))
numbers.append(number)
while number > 0:
    total += 1
    number = int(input("Enter number {}: ".format(total)))
    numbers.append(number)
if number < 0:
    del numbers[-1]
    print("That number is invalid (must be greater than 0)")
    print("The first number is {}.".format(numbers[0]))
    print("The last number is {}.".format(numbers[-1]))
    print("The smallest number is {}.".format(min(numbers)))
    print("The largest number is {}.".format(max(numbers)))
    print("The average of the numbers is {:4}.".format(sum(numbers) / len(numbers)))
